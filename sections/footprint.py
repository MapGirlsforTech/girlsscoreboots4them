import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
import h5py
from translations import translate
from utils import parrafo, title, subtitle
from keras.models import load_model  # TensorFlow is required for Keras to work
from keras.layers import Input
from keras.models import Model
from keras.layers import TFSMLayer


# st.header(translate("footprint"))

# Necesario porque arregla un error en el modelo.
# f = h5py.File("model/keras_model.h5", mode="r+")
# model_config_string = f.attrs.get("model_config")
# if model_config_string.find('"groups": 1,') != -1:
#     model_config_string = model_config_string.replace('"groups": 1,', '')
# f.attrs.modify('model_config', model_config_string)
# f.flush()
# model_config_string = f.attrs.get("model_config")
# assert model_config_string.find('"groups": 1,') == -1

# Title
title(translate("footprint_test.title"))

parrafo(translate("footprint_test.text"))

# load model, set cache to prevent reloading


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
layer = TFSMLayer("model",call_endpoint='serving_default')
input_tensor = Input(shape=(224, 224, 3))
model = Model(inputs=input_tensor, outputs=layer(input_tensor))

# # Load the labels
class_names = open("model/labels.txt", "r").readlines()

# # Create the array of the right shape to feed into the keras model
# # The 'length' or number of images you can put into the array is
# # determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


uploaded_file = st.file_uploader("Choose an image file", type="jpg")
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    raw_output = model.predict(data)
    prediction = list(raw_output.values())[0][0]
    print(list(class_names))
    
    print('--------')
    print(prediction)
    print('--------')
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[index]

    # Print prediction and confidence score
    subtitle(f"{class_name[2:]} {"{:.2%}".format(confidence_score)}")
    st.image(uploaded_file)


