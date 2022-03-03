import streamlit as st
import time
from VGG import VGG
from MobileNetV2 import MobileNetV2
from EfficientNetB3 import EfficientNetB3
import numpy as np

LABEL_DICT = {0: 'Cassava Bacterial Blight (CBB)',
              1: 'Cassava Brown Streak Disease (CBSD)',
              2: 'Cassava Green Mottle (CGM)',
              3: 'Cassava Mosaic Disease (CMD)',
              4: 'Healthy'}

st.title("Cassava Disease Detection")

method = st.selectbox('Capture or Upload an Image', ('Upload Image', 'Capture Image'))

if method == 'Upload Image':
    image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
else:
    image_file = st.camera_input("Capture Image")

if image_file:
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.001)
        progress_bar.progress(i + 1)
    st.info('Image Uploaded successfully!')
    st.image(image_file.getvalue())

option = st.selectbox('Choose the Model ', ('Choose a model', 'MobileNetV2', 'EfficientNet', 'VGG16'))

if option == 'MobileNetV2':
    model = MobileNetV2.load_model()
    if image_file is not None:

        with st.spinner('Wait for it...'):
            image = MobileNetV2.preprocessing(image_file.getvalue())

            prediction = model.predict(image)

            prediction = np.argmax(prediction)

            st.balloons()
        st.success(f"""Prediction: {LABEL_DICT[prediction]}""")


if option == 'EfficientNet':
    model=EfficientNetB3.load_model()
    if image_file is not None:

        with st.spinner('Wait for it...'):
            image = EfficientNetB3.preprocessing(image_file.getvalue())

            prediction = model.predict(image)

            prediction = np.argmax(prediction)

            st.balloons()
        st.success(f"""Prediction: {LABEL_DICT[prediction]}""")
elif option == 'VGG16':
    model = VGG.load_model()
    if image_file is not None:

        with st.spinner('Wait for it...'):
            image = VGG.preprocessing(image_file.getvalue())

            prediction = model.predict(image)

            prediction = np.argmax(prediction)

            st.balloons()
        st.success(f"""Prediction: {LABEL_DICT[prediction]}""")
else:
    st.info('Please Select a model!')
