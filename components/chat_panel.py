import streamlit as st
from openai import OpenAI
from translations import translate

# =========================
# Config cliente
# =========================
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# =========================
# Helpers internos
# =========================
def _get_messages(state_key: str) -> list[dict]:
    if state_key not in st.session_state:
        st.session_state[state_key] = []
    return st.session_state[state_key]


def _add_message(state_key: str, role: str, content: str) -> None:
    st.session_state[state_key].append({
        "role": role,
        "content": content
    })


def _has_red_flags(text: str) -> bool:
    flags_es = [
        "dolor fuerte",
        "mucho dolor",
        "inflamación",
        "inflamacion",
        "hinchazón",
        "hinchazon",
        "lesión",
        "lesion",
        "torcedura",
        "no puedo caminar",
        "no puedo apoyar",
        "fiebre",
        "empeora",
        "empeoró",
        "empeoro",
        "entumecimiento"
    ]
    flags_en = [
        "severe pain",
        "much pain",
        "inflammation",
        "swelling",
        "injury",
        "sprain",
        "can't walk",
        "can't bear weight",
        "fever",
        "worsens",
        "getting worse",
        "numbness"
    ]
    lower = text.lower()
    return any(flag in lower for flag in flags_es + flags_en)


def _build_system_prompt(foot_type: str, confidence: float) -> str:
    if st.session_state.language == "es":
        return f"""
            Eres un asistente educativo sobre tipos de pisada.

            Contexto:
            - Tipo de pisada detectada por la app: {foot_type}
            - Confianza estimada del modelo: {confidence:.2f}

            Reglas:
            - Responde en español.
            - Usa lenguaje simple para adolescentes de 13 años.
            - Da solo orientación general y educativa.
            - No des diagnósticos médicos.
            - No indiques tratamientos personalizados.
            - No recomiendes medicamentos.
            - Si la persona menciona dolor fuerte, lesión, inflamación, fiebre,
            empeoramiento o dificultad para caminar, indica consulta profesional.
            - Máximo 120 palabras.
            """
    else:
        return f"""
            You are an educational assistant on types of footprint. 
            Context: 
            - Type of footprint detected by the app: {foot_type} 
            - Estimated model confidence: {confidence:.2f} 

            Rules: 
            - Answer in English. 
            - Use simple language for 13-year-olds. 
            - Gives only general and educational guidance. 
            - Do not give medical diagnoses. 
            - Do not indicate personalized treatments. 
            - Do not recommend medications. 
            - If the person mentions severe pain, injury, inflammation, fever, worsening or difficulty walking, indicates professional consultation. 
            - Maximum 120 words.
        """ 
    
    


def _generate_answer(
    foot_type: str,
    confidence: float,
    messages: list[dict],
    user_message: str
) -> str:
    if _has_red_flags(user_message):
        if st.session_state.language == "es":
            return (
                "Esta app brinda orientación general y no reemplaza una consulta médica. "
                "Si hay dolor fuerte, inflamación, lesión o dificultad para caminar, "
                "conviene consultar con un médico, traumatólogo, podólogo o fisioterapeuta."
            )   
        else:
            return (
                "This app provides general guidance and does not replace a medical consultation. "
                "If there is severe pain, inflammation, injury, or difficulty walking, "
                "it is advisable to consult a doctor, traumatologist, podiatrist, or physiotherapist."
            )

    input_items = [
        {
            "role": "system",
            "content": _build_system_prompt(foot_type, confidence)
        }
    ]

    for msg in messages[-6:]:
        input_items.append({
            "role": msg["role"],
            "content": msg["content"]
        })

    input_items.append({
        "role": "user",
        "content": user_message
    })

    response = client.responses.create(
        model="gpt-5.4-mini",
        input=input_items
    )

    return response.output_text.strip()


def _set_welcome_message(state_key: str, foot_type: str, confidence: float) -> None:
    messages = _get_messages(state_key)
    initial_message = (
        f"The app detected a **{foot_type.strip()}** gait "
        f"with an estimated confidence of **{confidence:.0%}**. "
        "I can explain what it means and give you general advice."
    ) if st.session_state.language == "en" else (
        f"La app detectó una pisada **{foot_type.strip()}** "
        f"con una confianza estimada de **{confidence:.0%}**. "
        "Puedo explicarte qué significa y darte consejos generales."
    )

    if not messages:
        _add_message(
            state_key,
            "assistant",
            initial_message
        )


def _render_history(state_key: str) -> None:
    for msg in _get_messages(state_key):
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


def _handle_prompt(state_key: str, foot_type: str, confidence: float, prompt: str) -> None:
    _add_message(state_key, "user", prompt)

    answer = _generate_answer(
        foot_type=foot_type,
        confidence=confidence,
        messages=_get_messages(state_key),
        user_message=prompt
    )

    _add_message(state_key, "assistant", answer)


def _render_quick_actions(state_key: str, foot_type: str, confidence: float) -> None:
    col1, col2, col3 = st.columns(3)

    if col1.button("Qué significa", key=f"{state_key}_meaning"):
        _handle_prompt(
            state_key,
            foot_type,
            confidence,
            "¿Qué significa este tipo de pisada?"
        )
        st.rerun()

    if col2.button("Consejos generales", key=f"{state_key}_tips"):
        _handle_prompt(
            state_key,
            foot_type,
            confidence,
            "Dame consejos generales según este tipo de pisada."
        )
        st.rerun()

    if col3.button("Cuándo consultar", key=f"{state_key}_doctor"):
        _handle_prompt(
            state_key,
            foot_type,
            confidence,
            "¿Cuándo conviene consultar a un especialista?"
        )
        st.rerun()


# =========================
# API pública del módulo
# =========================
def render_chat_panel(
    foot_type: str,
    confidence: float,
    state_key: str = "chat_messages"
):
    st.subheader(translate("footprint_test.chat_title"))

    st.warning(translate("footprint_test.chat_warning"))

    _set_welcome_message(state_key, foot_type, confidence)

    # _render_quick_actions(state_key, foot_type, confidence)
    _render_history(state_key)

    user_text = st.chat_input(
        translate("footprint_test.chat_placeholder"),
        key=f"{state_key}_input"
    )

    if user_text:
        with st.chat_message("user"):
            st.markdown(user_text)

        _add_message(state_key, "user", user_text)

        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                answer = _generate_answer(
                    foot_type=foot_type,
                    confidence=confidence,
                    messages=_get_messages(state_key),
                    user_message=user_text
                )
                st.markdown(answer)

        _add_message(state_key, "assistant", answer)

    if st.button(translate("footprint_test.chat_clear_button"), key=f"{state_key}_clear"):
        st.session_state[state_key] = []
        st.rerun()