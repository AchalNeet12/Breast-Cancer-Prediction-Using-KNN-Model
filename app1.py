import streamlit as st
import pickle
import numpy as np
import base64

# Set page configuration for compact view (this must be the first Streamlit command)
st.set_page_config(page_title="Breast Cancer Prediction", layout="centered")

# Function to set background image and text color
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}"); 
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        color: white; /* Set all text color to white */
    }}
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {{
        color: white; /* Ensure headers are also white */
    }}
    .stApp .stMarkdown p {{
        color: white; /* Set all paragraph text to white */
    }}
    .stButton button {{
        background-color: #0078D7; /* Optional: Adjust button color */
        color: white;
        border-radius: 5px;
        border: none;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call the function to set the background (provide the correct image path)
set_background("img1.jpeg")

# Load the trained KNN model
model_filename = 'KNN_4_model.pkl'
with open(model_filename, 'rb') as file:
    knn_model = pickle.load(file)

# Main title and description
st.title("Breast Cancer Prediction ♋ ")
st.write("""
This app helps you predict whether a breast tumor is **Benign** (non-cancerous) or **Malignant** (cancerous) by analyzing key features. Use the sliders in the sidebar to enter the details, then click **Predict** to see the result.
""")

# Sidebar with input features, description, and instructions
with st.sidebar:
    st.markdown("""
    <h2 style="font-size: 18px; font-weight: bold; color: #f0f0f0;">📊About the Model</h2>
    <p style="font-size: 14px; color: #f0f0f0; line-height: 1.2;">This model classifies breast tumors as <strong>Benign</strong> (non-cancerous) or <strong>Malignant</strong> (cancerous) based on features like cell shape and size.</p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <h3 style="font-size: 16px; font-weight: bold; color: #f0f0f0;">📝Instructions</h3>
    <p style="font-size: 14px; color: #f0f0f0; line-height: 1.3;">
        <strong>Benign:</strong> Non-cancerous tumors that do not spread.<br>
        <strong>Malignant:</strong> Cancerous tumors that can spread.
    </p>
    """, unsafe_allow_html=True)

    # Input fields using sliders
    st.subheader("🔍Input Features")
    clump_thickness = st.slider('🔑 Clump Thickness', 1, 10, 1)
    uniformity_cell_size = st.slider('🔑 Uniformity of Cell Size', 1, 10, 1)
    uniformity_cell_shape = st.slider('🔑Uniformity of Cell Shape', 1, 10, 1)
    marginal_adhesion = st.slider('🔑Marginal Adhesion', 1, 10, 1)
    single_epithelial_cell_size = st.slider('🔑Single Epithelial Cell Size', 1, 10, 1)
    bare_nuclei = st.slider('🔑Bare Nuclei', 1, 10, 1)
    bland_chromatin = st.slider('🔑Bland Chromatin', 1, 10, 1)
    normal_nucleoli = st.slider('🔑Normal Nucleoli', 1, 10, 1)
    mitoses = st.slider('🔑Mitoses', 1, 10, 1)

# Collect input features into an array
input_data = np.array([
    clump_thickness,
    uniformity_cell_size,
    uniformity_cell_shape,
    marginal_adhesion,
    single_epithelial_cell_size,
    bare_nuclei,
    bland_chromatin,
    normal_nucleoli,
    mitoses
]).reshape(1, -1)

# Prediction button
if st.button("**📈Predict**"):
    try:
        # Make prediction
        prediction = knn_model.predict(input_data)[0]
        # Map numeric prediction to meaningful labels
        diagnosis = "Malignant" if prediction == 1 else "Benign"
        st.success(f"Prediction: {diagnosis}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
