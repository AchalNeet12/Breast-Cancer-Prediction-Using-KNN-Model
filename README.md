# Breast Cancer Prediction Using K-Nearest Neighbors (KNN)
---
---
## 📋 Project Overview:
#### The Breast Cancer Prediction app is designed to assist in identifying whether a breast tumor is Benign (non-cancerous) or Malignant (cancerous). It uses a machine learning model trained on historical data of tumor features to classify the tumor. This tool provides an easy-to-use interface for users to input tumor details and get predictions instantly.
---
## 📌 K-Nearest Neighbors (KNN):
The K-Nearest Neighbors (KNN) algorithm is a simple and effective supervised machine learning technique.
- **How it Works:**
  - KNN classifies a new data point based on its proximity to other data points in the dataset.
  - It calculates the distance (e.g., Euclidean distance) between the new data point and its nearest neighbors.
  - The majority class among the neighbors determines the classification result.
    
  ![image](https://raw.githubusercontent.com/artifabrian/dynamic-knn-gpu/master/knn.png)
---
## 🔍 Dataset:
The dataset used for this project is the Breast Cancer Wisconsin (Diagnostic) Dataset, which contains real-world data on breast tumors.
  - **Features:** The dataset includes numeric features that describe various characteristics of cell nuclei present in breast cancer biopsies.
  - **Labels:**
           -  **Benign (0):** Tumors that are non-cancerous and do not spread to other parts of the body.
           -  **Malignant (1):** Cancerous tumors that can invade nearby tissues or spread.
---
## 🔑 Key Features:
   - **Clump Thickness:** Uniformity of the cell clumps.
   - **Uniformity of Cell Size:** Variation in cell size.
   - **Uniformity of Cell Shape:** Consistency in cell shape.
   - **Marginal Adhesion:** How well cells stick together.
   - **Single Epithelial Cell Size:** Size of single epithelial cells.
   - **Bare Nuclei:** Count of nuclei without cytoplasm.
   - **Bland Chromatin:** Consistency of chromatin in the nucleus.
   - **Normal Nucleoli:** Size and visibility of nucleoli.
   - **Mitoses:** Frequency of cell division.
---
## 🛠️ Project Components:
1. **Data Preprocessing**:
  - **Data Cleaning:** Handling missing values in features like Bare Nuclei to ensure a consistent dataset.
  - **Normalization:** Scaling the features to ensure they are on the same range, which helps the machine learning algorithm perform better.
  - **Label Encoding:** Encoding the diagnosis (Benign or Malignant) into numeric labels (0 or 1).
  - **Feature Selection:** Selecting the most relevant features to avoid overfitting and improve model accuracy.
  -   Divided the dataset into 80% training and 20% testing subsets for validation.
2. **KNN Model Development:**
  - mplemented K-Nearest Neighbors (KNN), optimizing results with k=3, k=4, k=5 upto k=9
  - Used metrics like Confusion Matrix, Accuracy, Precision, Recall, and F1-Score for thorough evaluation.
3. **Interactive Streamlit Application:**
  - Designed a user-friendly app where users can adjust sliders for tumor features like cell shape, size, and adhesion.
  - Integrated the trained KNN model to predict and display whether the tumor is benign or malignant.
---
## 🤖 Technology Used:
1. **Programming Language:**
   - Python
2. **Libraries and Frameworks:**
   - **Streamlit:** For creating the user interface and web app.
   - **NumPy:** For numerical computations.
   - **Pickle:** For loading the pre-trained KNN model.
   - **Base64:** For encoding images for use as backgrounds.
3. **Machine Learning Algorithm:**
   - K-Nearest Neighbors (KNN).
4. **Deployment:**
   - Streamlit makes it easy to host and interact with the app locally or on the web.
---
## 📊 Model Results:
- **Best Model Accuracy**: 97.86% (with `k=4`)
- **Confusion Matrix for k=3**:
        
          [[83 2] 
          [ 2 53]]
  
- **Precision**: 100%
- **Recall**: 96.59%
- **F1-Score**: 98.27%
- **Null Accuracy**: 60.71%
---
## 📝 Conclusion:
This project combines robust data preprocessing, an optimized KNN model, and an intuitive Streamlit interface to deliver accurate predictions and a user-friendly experience. Its modular design ensures scalability, ease of updates, and potential for future enhancements, making it a valuable tool in healthcare technology.





