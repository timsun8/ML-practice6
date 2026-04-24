import streamlit as st
import requests

st.title("Iris Prediction App")

st.write("Enter iris flower measurements to get a model prediction.")

sepal_length = st.number_input("Sepal length", min_value=0.0, value=5.1)
sepal_width = st.number_input("Sepal width", min_value=0.0, value=3.5)
petal_length = st.number_input("Petal length", min_value=0.0, value=1.4)
petal_width = st.number_input("Petal width", min_value=0.0, value=0.2)

if st.button("Predict"):
    input_data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=input_data
    )

    if response.status_code == 200:
        prediction = response.json()["prediction"]

        labels = ["Setosa", "Versicolor", "Virginica"]
        st.success(f"Prediction: {labels[prediction]}")
    else:
        st.error("Prediction failed. Make sure FastAPI is running.")

