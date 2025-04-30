import streamlit as st

st.cache_data.clear()
st.cache_resource.clear()
translations = {
    "en": {
        "home_tab": "Home",
        "image_identifier": "Image Identifier",
        "about_us": {
            "title": "About Us",
            "contact_us": "Contact Us",
            "presentation": "Hello, we are **Maite**, **Ana** and **Pilar**, we live in Las Rozas in Madrid (Spain) and together we form the MAP Girls for Tech team.",
            "information": """
                We participated for the third consecutive year in the Technovation Girls project, whose objective is to bring technology closer to girls and young people from 8 to 18 years old, the idea is to increase with this initiative the presence of women in STEM careers.\n\n
                We must look for a problem in our community that meets one or more of the UN's 2030 Sustainable Development Goals. For 12 weeks we must work to provide a solution to this problem and create a mobile App or a Web App with said solution.\n\n
                Teams of girls from all over the world divided into three categories, Beginner, Junior and Senior, participate and compete in this program.\n\n 
                Girls learn among many other things to program, train AI models, edit videos and expose our idea and work in public.\n\n
                You can learn more about this program through the following link:\n\n
        """,
            "program_link": "Technovation Girls Program",
            "problematic": "One problem that has caught our attention is that there are no women's sports shoes for soccer players. It is crucial to use appropriate footwear when playing sports, since the use of sports shoes not suitable for women's feet can cause serious injuries. This has happened to our partner Pilar, as well as many other women, who due to the lack of footwear adapted to their foot, suffer injuries, sometimes significant, since they are forced to resort to male footwear. This is Pilar's testimony:",
            "quote": '"I have played soccer since I was 5 years old and I love sports, but I have never found boots specifically designed for girls. I have suffered from several ankle injuries, but my last injury has been the most serious of all, specifically in the knee and I have had to spend 4 months in total rest."',
            "summary": "Faced with this problem, the lack of sports shoes suitable for women's feet in many women's sports is where we are going to focus our project this season.",
        },
        "rules": {
            "title": "Rules",
            "first_rule": "1. **Promotion of Empowerment:** All comments and posts must promote support and respect for women in sports.",
            "second_rule": "2. **Inclusive Environment:** We accept and value diversity in all its forms. Discrimination based on gender, race, sexual orientation, or any other reason will not be tolerated.",
            "third_rule": "3. **Constructive Approach:** Criticism or suggestions must be constructive and respectful. The goal is to grow and learn together.",
            "fourth_rule": "4. **Beware of Rumors:** Share verified information and avoid spreading rumors or misinformation about sporting events or individuals.",
            "fifth_rule": "5. **Mental Health Protection:** Any content that promotes harmful behaviors, such as unhealthy obsession with weight or derogatory comments about body image, is prohibited.",
            "sixth_rule": "6. **Celebrate Achievements:** Share inspiring stories, achievements, and moments in sports. Let’s celebrate every victory, big or small!",
            "seventh_rule": "7. **Safe Space:** Personal attacks, offensive comments, and any form of harassment are prohibited to foster an environment where everyone feels comfortable participating.",
            "eighth_rule": "8. **Motivation and Resources:** Share ideas, tips, and resources so everyone can improve and enjoy their sports practice.",
        },
        "clothing_complements": "Clothing and Accessories",
        "merchandising": "Merchandising",
        "experiencies": "Experiences",
        "footwear_shop": "Footwear Shops",
        "introduce_yourself": {
            "title": "Introduce Yourself",
            "subtitle": "Welcome to forum: Boots for Her, Girls Score!!!",
            "welcome_message": """
                What a joy to have you here!\n\n
                This space has been created by women and for women who share a passion: sports in all its forms.\n\n
                Whether you are a professional athlete, amateur, coach, student, or simply a sports enthusiast in all its disciplines, here you will find a community that supports you, inspires you, and understands you.\n\n
                Sports have no gender, but the industry does not consider all our needs. We deserve sports footwear options designed for us and our anatomy, with the same technology, innovation, and variety offered to our male counterparts.\n\n
                Share your experiences.\n\n
                Exchange advice and training tips.\n\n
                Talk about nutrition, health, and wellness.\n\n
                Connect with other women like you.\n\n
                Here we celebrate your achievements, learn from challenges, and grow together.\n\n
                Thank you for being part of this powerful and authentic community!\n\n
                Welcome, this is your space!""",
        },
        "documentation": {
            "title": "Past and Future",
            "subtitle": "**Key facts about the evolution of women's sports footwear:**",
            "bullet_1": "1. **Origins and early models:** Although sports footwear began to develop in the 19th century, the first models were designed exclusively for men. Women had to adapt men's shoes or wear models that were poorly suited to their needs.",
            "bullet_2": "2. **First sports shoes for women:** It was not until the 1920s and 1930s that sneakers specifically for women started being manufactured. However, the offerings remained limited, and many sports disciplines lacked suitable options.",
            "bullet_3": "3. **Technological innovations and expansion:** Beginning in the 1960s, brands like Adidas and Nike started developing more specialized models for women. Improvements were made in cushioning, support, and lighter materials.",
            "bullet_4": "4. **Revolution in the 1970s and 1980s:** With the growth of fitness and running among women, sports brands began developing models with technology adapted to female anatomy. The perception of women's sports footwear shifted from being a secondary product to a real necessity.",
            "bullet_5": "5. **Cultural and social impact:** The fight for adequate sports footwear for women is not just a fashion issue but one of equity in sports. The lack of options reflects a gender gap in the sports industry that still needs to be addressed.",
            "bullet_6": "6. **Current challenges:** Despite advancements, many sports disciplines still lack footwear options designed specifically for female anatomy. This affects athletes' performance and comfort.",
            "bullet_7": "7. **Empowerment and representation:** In recent decades, women's sports footwear has become a symbol of empowerment. Female athletes have demanded greater representation and options designed for their performance, driving changes in the industry.",
        },
        "questionnaire": {
            "title": "Questionnaire",
            "thanks_message": "Thanks for answering our questionnaire.",
            "charts_title": "Graphical Visualization of the Questionnaire",
            "charts": {
                "femaleSportsShoesAvailability": "Did you know that there are no women's sports shoes for all sports categories?",
                "sportPracticed": "What sport do you practice?",
                "femaleShoesExistence": "Are there women's shoes available for the sport you play?",
                "shoeComfort": "Do your shoes feel comfortable?",
                "injuriesDueToShoes": "Have you suffered any injuries due to the shoes/boots you use?",
                "comfortEnhancementMethods": "Do you use anything to improve the comfort or fit of your footwear?",
                "wishForFemaleSportsShoes": "Would you like to have sports shoes designed for women's feet in all sports?",
                "knowledgeOfFootType": "Do you know your foot type?",
                "appToAddressFemaleSportsShoesIssue": "Would you like a mobile or web app that raises awareness about the lack of women's sports footwear and helps solve the issue?",
                "sportsSurfaceType": "On what type of surface do you practice your sport?",
            },
        },
        "ods": {
            "title": "SDGs",
            "objectives_to_change_the_world": {
                "title": "17 goals to transform our world",
                "first_text": "In 2015, the UN approved the 2030 Agenda for Sustainable Development, an opportunity for countries and societies to embark on a new path to improve the lives of all people, leaving no one behind.",
                "second_text": "The Agenda includes 17 Sustainable Development Goals, which establish that poverty eradication must go hand in hand with strategies that foster economic growth and address a range of social needs such as education, healthcare, social protection, and employment opportunities, while also combating climate change and protecting the environment.",
            },
            "how_we_apply": {
                "title": "Our App aligns with the following SDGs:",
                "third_ods": {
                    "title": "SDG number 3: Good Health and Well-being",
                    "text": "Our project addresses the issue of sports, aiming to raise awareness among users about one of the growing concerns in this field. Therefore, our web app seeks to enhance the experience of practicing sports and consequently improve the well-being and health of female athletes.",
                },
                "fifth_ods": {
                    "title": "SDG number 5: Gender Equality",
                    "text": "Nowadays, it is much easier to find footwear adapted to the male foot than to the female foot. This directly affects female athletes' performance as they suffer injuries more easily, and in some cases, these injuries are severe.",
                },
                "nineth_ods": {
                    "title": "SDG number 9: Industry, Innovation, and Infrastructure",
                    "text": "The development of this project is entirely innovative. After conducting an exhaustive study, we found no suitable sports footwear for women across many sports. Making the industry aware of this issue will drive innovation in the women's sports footwear sector.",
                },
                "tenth_ods": {
                    "title": "SDG number 10: Reduced Inequalities",
                    "text": "Our project aligns with this SDG because, just as there is sports footwear for men in all the necessary modalities, there should also be equivalent sports footwear for women. The lack of proper footwear contributes to the undervaluation of female athletes.",
                },
            },
        },
        "footprint_test": {
            "title": "Footprint Test",
            "text": '''
                This tool designed with Artificial Intelligence, can help you to know your type of footprint.\n\n
                To do this you must obtain an image of your footprint and drag it to the classifier.\n\n 
                After analyzing it, it will indicate with its corresponding probability, which is your type of footprint.\n\n
                `Important: This test is indicative, to obtain a clinically correct result, it must be performed by a qualified professional.`
            '''
            },
        "footwear": "Footwear",
        "foro": {
            "title": "Forum",
            "description": "A place to discuss and share ideas.",
            "comments": "Comments",
        },
        "home": {
            "title": "Boots for Her. Girls Score!!!",
            "presentation": """
            Hello, we are **Maite**, **Ana**, and **Pilar**, and together we form the team MAP Girls for Tech. We are participating for the third consecutive year in the Technovation Girls project, whose goal is to bring technology closer to girls and young women aged 8 to 18. The idea is to increase the presence of women in STEM careers through this initiative.
            
            We must find a problem in our community that meets one or more of the UN Sustainable Development Goals 2030. During 12 weeks we must work to give a solution to that problem and create a mobile App or a Web App with that solution.
            
            In this program, teams of girls from all over the world participate and compete in three categories, Beginner, Junior and Senior.

            We girls learn among many other things to program, train AI models and to present our ideas and work in public.

            You can learn more about this program through the following link:
            """,
            "linkToProgram": "Technovation Girls Program",
            "introductionToTestimony": "One problem that has come to our attention is that there are no women's sports shoes for female soccer players. It is crucial to use appropriate footwear when playing sports, as the use of sports shoes that are not suitable for women's feet can cause serious injuries. This has happened to our colleague Pilar, as well as to many other women, who due to the lack of footwear adapted to their feet suffer injuries, sometimes serious, as they are forced to resort to men's footwear. This is Pilar's testimony:",
            "testimony": "“I have played soccer since I was 5 years old and I love sports, but I have never found boots designed specifically for girls. I have suffered from several ankle injuries, but my last injury was the most serious of all, specifically to my knee and I had to be on total rest for 4 months.”",
            "projectFocus": "Faced with this problem, the lack of sports footwear suitable for women's feet in many women's sports, is where we are going to focus our project this season.",
            "questionnaire": "We have created a questionnaire with a series of questions that will help us shape the project and try to find a solution to this problem.",
            "questionnaireLink": "Go to Questionnaire",
            "needYourHelp": "WE NEED YOUR HELP!!!!!",
            "thankYou": "Thank you very much",
            "questionnaireRequest": "Could you answer our questionnaire?",
            "introduction": """
                The previous testimony is from our partner Pilar, who has suffered the most serious injury from her sports career.\n\n
                We meet here because we share a need that cannot continue to be ignored: the absence of women's sports shoes for all disciplines. Sports footwear available on the market, mostly made for male anatomy, does not adequately adapt to the morphology of the female foot. It is not just a matter of design and health, it is a matter of fairness, representation and respect for our needs as athletes, as women and as people.\n\n
                Here, we will share experiences, knowledge and strategies to require sports brands, designers and institutions to recognize and address this need.\n\n 
                **This forum is our starting point for change.**\n\n
            """,
        },
        "footprint_types": {
            "title": "Footprint Types",
            "types_title": "There are three types of footprints:",
            "types": """
    **Pronator:** It is the one in which the foot is supported by the internal zone. It is the footprint that corresponds to the flat feet and in which all the load of the body falls towards the internal zone of the foot. In the study of the footprint we observe a very wide footprint and a flattening of the foot.\n\n
    **Supinator:** It is the footprint in which the foot is supported by the external area. It corresponds to the cavus feet, in which a very high internal arch and a very large support by the external edge is usually observed. They usually present overloads in the heel and forefoot area.\n\n
    **Neutral:** This is the stride in which the support is evenly distributed. The heel is centered and the weight is distributed correctly during the step.\n\n
        """,
            "second_text": """
        Women's feet are not only shaped differently, but they are also lighter than men's, and the way they run and move is different.\n\n
        The fact that there are no sports shoes specifically designed for women in all sports may contribute to a number of injuries due to anatomical differences between men and women.\n\n
        Athletic footwear designed for men does not always fit the morphology of the female foot well, which can increase the risk of injury.\n\n
        """,
            "reasons_title": "Reasons why this may occur:",
            "reason_1": """
        **1. Differences in the shape of the foot:**\n\n
        Women's feet tend to be narrower at the heel and wider in the toe area compared to men's feet. If footwear is not designed to conform to this shape, there may be an uncomfortable or improper fit, increasing the risk of:\n\n
        Blisters and chafing: A poor fit can generate friction in specific areas, resulting in skin lesions such as blisters.\n\n
        Foot and joint pain: An improper fit can cause foot or leg pain by not properly distributing forces during movement.\n\n
        """,
            "reason_2": """
         **2. Foot size and distribution:**\n\n
         Women, on average, have smaller and lighter feet than men. This can affect support and stability when wearing athletic shoes designed for men, which are generally made with a weight distribution and design that does not take these differences into account. This can lead to:\n\n
         Lack of arch support: Boots designed for men may not provide adequate arch support for women's feet, which can contribute to ligament and tendon injuries.\n\n
         Stress on knees and hips: The mismatch in boots can alter the biomechanics of movement when running or changing direction, which can increase pressure on the knees and hips, leading to injuries such as sprains or tendonitis.\n\n
        """,
            "reason_3": """
         **3. Ankle injuries:**\n\n
         Women tend to have greater joint flexibility, especially in the ankles. If footwear does not provide adequate support, this can make the ankles more prone to injuries such as:\n\n
         Ankle sprains: Shoes that do not fit properly or do not have sufficient lateral support can increase the risk of ankle sprains, which are common in soccer due to rapid changes of direction and physical demands.\n\n
        """,
            "reason_4": """
         **4. Impact on performance:**\n\n
         Poorly fitted running shoes can affect performance by not providing the right level of comfort and support. This can cause the athlete to change her posture or running form to accommodate the shoe, which increases the risk of overloading certain parts of the body (e.g., knees, back, hips), which can lead to chronic injuries.\n\n
         """,
            "reason_5": """
         **5. Injuries due to lack of cushioning:**\n\n
         Women tend to be more prone to impact-related injuries due to the difference in body weight distribution. If the footwear does not have sufficient cushioning or if they are designed with a structure that is less suitable for women, problems can arise such as:\n\n
         Bone stress injuries (stress fractures): Lack of adequate shock absorption can increase the risk of stress fractures, especially in the feet and legs.\n\n
         Joint pain: The lack of good cushioning can cause discomfort in the knees or back due to repetitive blows during sports practice.\n\n
         """,
            "reason_summary": """
         **In summary:**\n\n
         The use of athletic shoes not designed for the female anatomy may increase the risk of injury, as they do not provide adequate support, fit or comfort for female athletes.\n\n
         Differences in foot shape and size, joint flexibility, and body weight distribution between men and women are factors that may contribute to these risks.\n\n
         For this reason, it is essential that women's athletic footwear is designed with the specific needs of women in mind to reduce the risk of injury and improve performance.\n\n
         """,
        },
    },
    "es": {
        "home_tab": "Inicio",
        "image_identifier": "Identificador de pisada",
        "forum": "Foro",
        "about_us": {
            "title": "Sobre nosotras",
            "contact_us": "Contact Us",
            "presentation": "Hola, somos **Maite**, **Ana** y **Pilar**, vivimos en Las Rozas de Madrid (España) y juntas formamos el equipo MAP Girls for Tech.",
            "information": """
                Participamos por tercer año consecutivo en el proyecto Technovation Girls, cuyo objetivo es acercar la tecnología a las chicas y jóvenes de 8 a 18 años, la idea es aumentar con esta iniciativa la presencia de mujeres en las carreras STEM.\n\n
                Debemos buscar un problema en nuestra comunidad que cumpla uno o varios de los Objetivos  de Desarrollo Sostenible 2030 de la ONU. Durante 12 semanas debemos trabajar para darle una solución a dicho problema y crear una App móvil o una Web App con dicha solución.\n\n
                En este programa participan y compiten equipos de chicas de todo el mundo divididas en tres categorías, Beginner, Junior y Senior.\n\n
                Las chicas aprendemos entre otras muchas cosas a programar, entrenar modelos de IA, editar videos y a exponer nuestra idea y trabajo en público.\n\n
                Podéis conocer más sobre este programa a través del siguiente enlace:\n\n
                """,
            "program_link": "Programa Technovation Girls",
            "problematic": "Un problema que nos ha llamado la atención es que no hay calzado deportivo femenino para las jugadoras de fútbol. Es crucial utilizar un calzado adecuado al practicar deporte, ya que el uso de calzado deportivo no adecuado al pie femenino puede causar graves lesiones. Esto le ha pasado a nuestra compañera Pilar, así como dea otras muchas mujeres, que debido a la falta de calzado adaptado a su pie sufre lesiones, en ocasiones importantes, ya que se ven  obligadas a recurrir al calzado masculino. Este es el testimonio de Pilar:",
            "quote": '"He jugado al fútbol desde los 5 años y me encantan los deportes, pero nunca he encontrado botas diseñadas especificamente para chicas. He sufrido de varias lesiones en los tobillos, pero mi última lesión ha sido la más grave de todas, concretamente en la rodilla y he tenido que estar 4 meses en reposo total."',
            "summary": "Ante esta problemática, la falta de calzado deportivo adecuado al pie de la mujer en muchos deportes femeninos, es hacia donde vamos a enfocar nuestro proyecto esta temporada.",
        },
        "rules": {
            "title": "Normas",
            "first_rule": "1. **Promoción del empoderamiento:** Todos los comentarios y publicaciones deben promover el apoyo y el respeto hacia las mujeres en el deporte.",
            "second_rule": "2. **Ambiente inclusivo:** Aceptamos y valoramos la diversidad en todas sus formas. Discriminación por género, raza, orientación sexual u otro motivo no será tolerada.",
            "third_rule": "3. **Enfoque constructivo:** Las críticas o sugerencias deben ser constructivas y respetuosas. La idea es crecer y aprender juntas.",
            "fourth_rule": "4. **Cuidado con los rumores:** Comparte información verificada y evita difundir rumores o desinformación sobre eventos deportivos o personas.",
            "fifth_rule": "5. **Protección de la salud mental:** Está prohibido cualquier contenido que fomente conductas perjudiciales, como obsesión insana con el peso o comentarios despectivos sobre la imagen corporal.",
            "sixth_rule": "6. **Celebrar los logros:** Comparte historias, logros y momentos inspiradores dentro del deporte. ¡Celebremos juntas cada victoria, grande o pequeña!",
            "seventh_rule": "7. **Espacio seguro:** Se prohíben los ataques personales, los comentarios ofensivos y cualquier tipo de acoso, fomentando un ambiente donde todas se sientan cómodas participando.",
            "eighth_rule": "8. **Motivación y recursos:** Comparte ideas, consejos y recursos para que todas puedan mejorar y disfrutar de su práctica deportiva.",
        },
        "clothing_complements": "Ropa deportiva y Complementos",
        "merchandising": "Merchandising",
        "experiencies": "Experiencias",
        "footwear_shop": "Tiendas de calzado",
        "introduce_yourself": {
            "title": "Presentate",
            "subtitle": "Bienvenida al foro: Boots for Her, Girls Score!!!",
            "welcome_message": """
                ¡Qué alegría tenerte aquí!\n\n
                Este espacio ha sido creado por mujeres y para mujeres que comparten una pasión: el deporte en todas sus formas.\n\n
                Ya seas atleta profesional, amateur, entrenadora, estudiante o simplemente una amante del deporte en todas sus disciplinas, aquí encontrarás una comunidad que te apoya, te inspira y te entiende.\n\n
                El deporte no tiene género, pero la industria no tiene en cuenta todas nuestras necesidades, merecemos opciones de calzado deportivo diseñado para nosotras y nuestra anatomía, con la misma tecnología, innovación y variedad que se ofrece a nuestros compañeros masculinos.\n\n
                Comparte tus experiencias.\n\n
                Intercambia consejos y entrenamientos.\n\n
                Habla de nutrición, salud y bienestar.\n\n
                Conecta con otras mujeres como tú.\n\n
                Aquí celebramos tus logros, aprendemos de los desafíos y crecemos juntas.\n\n
                ¡Gracias por ser parte de esta comunidad poderosa y auténtica!\n\n
                ¡Bienvenida, este es tu espacio!""",
        },
        "documentation": {
            "title": "Pasado y Futuro",
            "subtitle": "**Datos clave sobre la evolución del calzado deportivo femenino:**",
            "bullet_1": "1. **Orígenes y primeros modelos:** Aunque el calzado deportivo comenzó a desarrollarse en el siglo XIX, los primeros modelos estaban diseñados exclusivamente para hombres. Las mujeres tenían que adaptar calzado masculino o usar modelos poco adecuados para sus necesidades.",
            "bullet_2": "2. **Primeras zapatillas deportivas para mujeres:** No fue hasta las décadas de 1920 y 1930 que comenzaron a fabricarse zapatillas deportivas específicamente para mujeres. Sin embargo, la oferta seguía siendo limitada y muchas disciplinas deportivas no contaban con opciones adecuadas.",
            "bullet_3": "3. **Innovaciones tecnológicas y expansión:** A partir de los años 60, marcas como Adidas y Nike empezaron a desarrollar modelos más especializados para mujeres. Se introdujeron mejoras en amortiguación, soporte y materiales más ligeros.",
            "bullet_4": "4. **Revolución en los años 70 y 80:** Con el crecimiento del fitness y el running entre las mujeres, las marcas deportivas empezaron a desarrollar modelos con tecnología adaptada a la anatomía femenina. La percepción del calzado deportivo femenino pasó de ser un producto secundario a una necesidad real.",
            "bullet_5": "5. **Impacto cultural y social:** La lucha por un calzado deportivo adecuado para mujeres no es solo una cuestión de moda, sino de equidad en el deporte. La falta de opciones refleja una brecha de género en la industria deportiva que aún necesita ser abordada.",
            "bullet_6": "6. **Desafíos actuales:** A pesar de los avances, muchas disciplinas deportivas aún carecen de opciones de calzado diseñadas específicamente para la anatomía femenina. Esto afecta el rendimiento y la comodidad de las atletas.",
            "bullet_7": "7. **Empoderamiento y representación:** En las últimas décadas, el calzado deportivo femenino ha sido un símbolo de empoderamiento. Las atletas han exigido mayor representación y opciones diseñadas para su rendimiento, impulsando cambios en la industria.",
        },
        "questionnaire": {
            "title": "Cuestionario",
            "thanks_message": "Gracias por responder a nuestro cuestionario.",
            "charts_title": "Visualización Gráfica del Cuestionario",
            "charts": {
                "femaleSportsShoesAvailability": "¿Sabías que no existe calzado deportivo femenino para todas las categorías deportivas?",
                "sportPracticed": "¿Qué deporte practicas?",
                "femaleShoesExistence": "¿Existe calzado femenino para el deporte que practicas?",
                "shoeComfort": "¿Tu calzado te resulta cómodo?",
                "injuriesDueToShoes": "¿Has tenido alguna lesión debida a las zapatillas / botas que utilizas?",
                "comfortEnhancementMethods": "¿Utilizas algo para mejorar la comodidad o ajuste del calzado que usas?",
                "wishForFemaleSportsShoes": "¿Querrías que existiese calzado deportivo adaptado al pie femenino en todas las modalidades deportivas?",
                "knowledgeOfFootType": "¿Conoces tu tipo de pisada?",
                "appToAddressFemaleSportsShoesIssue": "¿Te gustaría que existiera una App para móvil o Web App que diera visibilidad al problema del calzado deportivo femenino y ayude a solucionarlo?",
                "sportsSurfaceType": "¿En qué tipo de superficie practicas tu deporte?",
            },
        },
        "ods": {
            "title": "ODS",
            "objectives_to_change_the_world": {
                "title": "17 objetivos para transformar nuestro mundo",
                "first_text": "En 2015, la ONU aprobó la Agenda 2030 sobre el Desarrollo Sostenible, una oportunidad para que los países y sus sociedades emprendieran un nuevo camino con el que mejorar la vida de todas las personas, sin dejar a nadie atrás.",
                "second_text": "La Agenda cuenta con 17 Objetivos de Desarrollo Sostenible, que establecen que la erradicación de la pobreza debe ir de la mano de estrategias que fomenten el crecimiento económico y abordan una serie de necesidades sociales como la educación, la sanidad, la protección social y las perspectivas de empleo, al tiempo que se combate el cambio climático y se protege el medio ambiente.",
            },
            "how_we_apply": {
                "title": "Nuestra App aplica con los siguientes ODS:",
                "third_ods": {
                    "title": "ODS número 3: Salud y bienestar",
                    "text": "Nuestro proyecto toca el tema del deporte, tratando de concienciar a los usuarios sobre unos de los problemas que están cobrando mayor importancia en este ámbito. Por tanto, nuestra web App pretende mejorar la experiencia al practicar deporte y por tanto, el bienestar y la salud de las mujeres deportistas",
                },
                "fifth_ods": {
                    "title": "ODS número 5: Igualdad de género",
                    "text": "A día de hoy, es mucho más fácil encontrar un calzado adaptado al pie masculino que al femenino. Esto afecta directamente al rendimiento de las deportistas femeninas porque se lesionan con más facilidad y siendo graves  en algunas ocasiones estas lesiones.",
                },
                "nineth_ods": {
                    "title": "ODS número 9: Industria, innovación e infraestructura",
                    "text": "El desarrollo de este proyecto es completamente innovador. Después de realizar un exhaustivo estudio, no hemos encontrado calzado deportivo femenino para un gran número de deportes. Hacer ver a la industria este problema supondrá una innovación en la industria deportiva femenina.",
                },
                "tenth_ods": {
                    "title": "ODS número 10: Reducción de las desigualdades",
                    "text": "Nuestro proyecto cumple este ODS porque igual que hay calzado deportivo para hombres en todas las modalidades que lo requieren, también tendría que haber calzado deportivo femenino en las mismas condiciones. Esto hace que las mujeres estén infravaloradas.",
                },
            },
        },
        "footprint": "Test de Pisada",
        "foro": {
            "title": "Foro",
            "description": "Lugar para discutir y compartir ideas.",
            "comments": "Comentarios",
        },
        "home": {
            "title": "Boots for Her. Girls Score!!!",
            "presentation": """
            Hola, somos **Maite**, **Ana** y **Pilar** y juntas formamos el equipo MAP Girls for Tech. Participamos por tercer año consecutivo en el proyecto Technovation Girls, cuyo objetivo es acercar la tecnología a las chicas y jóvenes de 8 a 18 años, la idea es aumentar con esta iniciativa la presencia de mujeres en las carreras STEM.
            
            Debemos buscar un problema en nuestra comunidad que cumpla uno o varios de los Objetivos  de Desarrollo Sostenible 2030 de la ONU. Durante 12 semanas debemos trabajar para darle una solución a dicho problema y crear una App móvil o una Web App con dicha solución.
            
            En este programa participan y compiten equipos de chicas de todo el mundo divididas en tres categorías, Beginner, Junior y Senior.

            Las chicas aprendemos entre otras muchas cosas a programar, entrenar modelos de IA y a exponer nuestra idea y trabajo en público.

            Podéis conocer más sobre este programa a través del siguiente enlace:
            """,
            "linkToProgram": "Programa Technovation Girls",
            "introductionToTestimony": "Un problema que nos ha llamado la atención es que no hay calzado deportivo femenino para las jugadoras de fútbol. Es crucial utilizar un calzado adecuado al practicar deporte, ya que el uso de calzado deportivo no adecuado al pie femenino puede causar graves lesiones. Esto le ha pasado a nuestra compañera Pilar, así como dea otras muchas mujeres, que debido a la falta de calzado adaptado a su pie sufre lesiones, en ocasiones importantes, ya que se ven  obligadas a recurrir al calzado masculino. Este es el testimonio de Pilar:",
            "testimony": "“He jugado al fútbol desde los 5 años y me encantan los deportes, pero nunca he encontrado botas diseñadas especificamente para chicas. He sufrido de varias lesiones en los tobillos, pero mi última lesión ha sido la más grave de todas, concretamente en la rodilla y he tenido que estar 4 meses en reposo total.”",
            "projectFocus": "Ante esta problemática, la falta de calzado deportivo adecuado al pie de la mujer en muchos deportes femeninos, es hacia donde vamos a enfocar nuestro proyecto esta temporada.",
            "questionnaire": "Hemos creado un cuestionario con una serie de preguntas que nos ayudarán a darle forma  al proyecto y tratar de buscar una solución a este problema.",
            "questionnaireLink": "Ir al Cuestionario",
            "needYourHelp": "¡¡¡NECESITAMOS VUESTRA AYUDA!!!",
            "thankYou": "Muchas Gracias",
            "questionnaireRequest": "¿Podrías contestar nuestro cuestionario?",
            "introduction": """
                El anterior testimonio es de nuestra compañera Pilar, que ha sufrido la lesión más grave de su trayectoria deportiva.\n\n
                Nos reunimos aquí porque compartimos una necesidad que no puede seguir siendo ignorada: la ausencia de calzado deportivo femenino para todas las disciplinas. El calzado deportivo disponible en el mercado, hecho en su mayoría para la anatomía masculina, no se adapta adecuadamente a la morfología del pie femenino. No es solo una cuestión de diseño y salud, es una cuestión de equidad, de representación y de respeto por nuestras necesidades como atletas, como mujeres y como personas.\n\n
                Aquí, compartiremos experiencias, conocimientos y estrategias para exigir a las marcas, diseñadores e instituciones deportivas que reconozcan y atiendan esta necesidad.\n\n
                **Este foro es nuestro punto de partida para el cambio.**\n\n
            """,
        },
        "footprint_types": {
            "title": "Tipos de Pisada",
            "types_title": "Existen tres tipos de pisadas:",
            "types": """
    **Pronadora:** Es aquella en la que el pie apoya por la zona interna. Es la pisada que secorresponde con los pies planos y en la que toda la carga del cuerpo recae hacia la zona interna del pie. En el estudio de la pisada observamos una huella muy ensanchada y un aplanamiento del pie.\n\n
    **Supinadora:** Es la pisada en la que el pie apoya por la zona externa. Se corresponde con los pies cavos, en los que se suele observar un arco interno muy elevado y un apoyo muy grande por el borde externo. Suelen presentar sobrecargas en la zona de talón y antepié.\n\n
    **Neutra:** Es la pisada en la que el apoyo se distribuye de manera homogénea. El talón apoya centrado y el peso se distribuye de manera correcta durante el paso.\n\n
        """,
            "second_text": """
        Los pies de las mujeres no solo tienen una forma diferente, sino que también son más livianos que los de los hombres y su forma de correr y moverse, es diferente.\n\n
        El hecho de que no existan calzado deportivo específicamente diseñado para mujeres en todas las modalidades deportivas, puede contribuir a una serie de lesiones debido a las diferencias anatómicas entre hombres y mujeres.\n\n
        El calzado deportivo diseñado para hombres no siempre se ajusta bien a la morfología del pie femenino, lo que puede aumentar el riesgo de lesiones.\n\n
        """,
            "reasons_title": "Razones por las que esto puede ocurrir:",
            "reason_1": """
        **1. Diferencias en la forma del pie:**\n\n
        Los pies de las mujeres tienden a ser más estrechos en el talón y más anchos en la zona de los dedos en comparación con los pies de los hombres. Si el calzado no está diseñado para ajustarse a esta forma, puede haber un ajuste incómodo o inadecuado, lo que aumenta el riesgo de:\n\n
        Ampollas y rozaduras: Un mal ajuste puede generar fricción en áreas específicas, lo que resulta en lesiones cutáneas como ampollas.\n\n
        Dolores en los pies y las articulaciones: Un ajuste inadecuado puede causar dolor en el pie o en la pierna, ya que no distribuye de manera adecuada las fuerzas durante el movimiento.\n\n
        """,
            "reason_2": """
         **2. Tamaño y distribución del pie:**\n\n
         Las mujeres, en promedio, tienen pies más pequeños y ligeros que los hombres. Esto puede afectar el soporte y la estabilidad al usar calzado deportivo diseñado para hombres, que generalmente están hechas con una distribución del peso y un diseño que no toma en cuenta estas diferencias. Esto puede llevar a:\n\n
         Falta de soporte en el arco: Las botas diseñadas para hombres pueden no proporcionar un soporte adecuado en el arco del pie femenino, lo que puede contribuir a lesiones en los ligamentos y tendones.\n\n
         Estrés en las rodillas y caderas: El desajuste en las botas puede alterar la biomecánica del movimiento al correr o cambiar de dirección, lo que puede aumentar la presión en las rodillas y las caderas, favoreciendo lesiones como esguinces o tendinitis.\n\n
        """,
            "reason_3": """
         **3. Lesiones en el tobillo:**\n\n
         Las mujeres tienden a tener una mayor flexibilidad en las articulaciones, especialmente en los tobillos. Si el calzado no ofrece un soporte adecuado, esto puede hacer que los tobillos sean más propensos a lesiones como:\n\n
         Esguinces de tobillo: Un calzado que no se ajusta correctamente o que no tiene suficiente soporte lateral puede aumentar el riesgo de esguinces, que son comunes en el fútbol debido a los cambios rápidos de dirección y la exigencia física.\n\n
        """,
            "reason_4": """
         **4. Impacto en el rendimiento:**\n\n
         El calzado deportivo mal ajustado puede afectar el rendimiento al no proporcionar el nivel adecuado de comodidad y soporte. Esto puede hacer que la deportista cambie su postura o forma de correr para adaptarse al calzado, lo que aumenta el riesgo de sobrecargar ciertas partes del cuerpo (por ejemplo, las rodillas, la espalda o las caderas), lo que puede derivar en lesiones crónicas.\n\n
         """,
            "reason_5": """
         **5. Lesiones por falta de amortiguación:**\n\n
         Las mujeres tienden a ser más propensas a sufrir lesiones relacionadas con el impacto debido a la diferencia en la distribución del peso corporal. Si el calzado no tiene suficiente amortiguación o si están diseñadas con una estructura menos adecuada para las mujeres, pueden surgir problemas como:\n\n
         Lesiones por estrés en los huesos (fracturas por sobrecarga): La falta de absorción adecuada de impactos puede aumentar el riesgo de fracturas por sobrecarga, especialmente en los pies y las piernas.\n\n
         Dolores articulares: La falta de una buena amortiguación puede generar molestias en las rodillas o la espalda debido a los golpes repetitivos durante la practica deportiva.\n\n
         """,
            "reason_summary": """
         **En resumen:**\n\n
         El uso de calzado deportivo no diseñado para la anatomía femenina puede aumentar el riesgo de lesiones, ya que no brindan el soporte, el ajuste o la comodidad adecuados para las deportistas.\n\n
         Las diferencias en la forma y tamaño de los pies, la flexibilidad articular, y la distribución del peso corporal entre hombres y mujeres son factores que pueden contribuir a estos riesgos.\n\n
         Por esta razón, es fundamental que el calzado deportivo femenino se diseñe teniendo en cuenta las necesidades específicas de las mujeres para reducir el riesgo de lesiones y mejorar el rendimiento.\n\n
         """,
        },
        "footprint_test": {
        "title": "Test de pisada",
        "text": '''
            Esta herramienta diseñada con Inteligencia Artificial, puede ayudarte a conocer tu tipo de pisada.\n\n
            Para ello deberás obtener una imagen de tu pisada y arrastarla al clasificador.\n\n 
            Trás analizarla, te indicará con su correspondiente probabilidad, cual es tu tipo de pisada.\n\n
            `Importante: Este test, es orientativo, para obtener un resultado clinicamente correcto, deberá ser realizado por un profesional cualificado.`
        '''
        },
    },
}


def translate(key):
    # """Obtiene la traducción desde la estructura anidada."""
    keys = key.split(".")

    translation = translations.get(st.session_state.language, {})

    for k in keys:
        if hasattr(translation, "get"):
            translation = translation.get(k, None)
        if translation is None:
            return f"Translation for '{k}' not found"

    return translation
