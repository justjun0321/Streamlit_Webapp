import easyocr as ocr
import streamlit as st
from PIL import Image
import numpy as np

# Page Title
st.title('Easy OCR - Extract Key Information from Images')

#subtitle
st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit` to filter key info for you!")

st.markdown("")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])

Dates = []
Name = []
Location = []

@st.cache
def load_model():
    reader = ocr.Reader(['en','ch_tra','ja'],model_storage_directory='.')
    return reader

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("Processing"):


        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            # Dates' part
            if re.search(r'\d+-\d+-\d+', text[1]):
                Dates.append(re.search(r'\d+-\d+-\d+', text[1]).group(0))
            if re.search(r'\d+\.\d+\.\d+', text[1]):
                Dates.append(re.search(r'\d+\.\d+\.\d+', text[1]).group(0))
            if re.search(r'\d+-\d+-\d+', text[1]):
                Dates.append(re.search(r'\d+/\d+/\d+', text[1]).group(0))

            # Name part
            if re.findall(r'[A-Z]\w+', 'Cynthia John'):
                Name = Name + re.findall(r'[A-Z]\w+', 'Cynthia John')

            result_text.append(text[1])


        st.write(result_text)
    #st.success("Here you go!")
    st.balloons()
else:
    st.write("Upload an Image")

st.caption("Kudos to @1littlecoder !!!")
