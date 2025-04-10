# 🎈 MAP Girls for Tech

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mapgirlsfortech.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

### Troubleshooting

Tensorflow need python 3.12 64bits because tensorflow pip wheel reaches to 3.12 - Download it from the oficial Python page - 
https://www.python.org/downloads/windows/

TensorFlow is not yet in the PyPI repository, so you have to specify the URL to the appropriate “wheel file” for your operating system and Python version.
pip install https://files.pythonhosted.org/packages/5c/98/d145af334fd5807d6ba1ead447bf0c57a36654ea58e726d70c0d09cae913/tensorflow-2.19.0-cp312-cp312-win_amd64.whl

More versions: https://pypi.org/project/tensorflow/#files