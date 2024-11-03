import streamlit as st
import joblib

# load the pre-trained model
model = joblib.load('diabetes_Logistic.model')

# Set the title of the Streamlit app
st.title("Diabetic patient Outcome Prediction")

# Create two columns for input fields
col1, col2 = st.columns(2)

# Collect user input through the input fields
Pregnancies = col1.number_input(label="Enter the Pregnancies of diabetic patients", min_value=0, max_value = 15)
Glucose = col2.number_input(label="Enter the Glucose of diabetic patients", min_value=0, max_value = 200)
BloodPressure = col1.number_input(label="Enter the BloodPressure of diabetic patients", min_value=0, max_value= 122)
SkinThickness = col2.number_input(label="Enter the SkinThickness of diabetic patients", min_value=0, max_value=56 )
Insulin = col1.number_input(label="Enter the Insulin of the diabetic patients", min_value=0, max_value= 846)
BMI = col2.number_input(label="Enter the BMI of the diabetic patients", min_value=0, max_value= 53.2)
DiabetesPedigreeFunction = col1.number_input(label="Enter the DiabetesPedigreeFunction of the diabetic patients", min_value=-0.06)
Age = col2.number_input(label="Enter the Age of the diabetic patients", min_value=0,max_value=80) 

# Define a button to submit the input and predict the result
if st.button("Predict"):
    # Use the model to make a prediction
    prediction = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    # Display the prediction result
    if prediction == 1:
        st.success("The model predicts that the diabetic patients would have survived.")
    else:
        st.warning("The model predicts that the diabetic patients would not have survived.")
        

