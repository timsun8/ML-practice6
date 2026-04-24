# ML Model Deployment with FastAPI, Docker, MLflow and Streamlit

This project demonstrates a complete machine learning pipeline:
model training, experiment tracking, API deployment, and a simple user interface.

## Project Overview

- A Logistic Regression model is trained on the Iris dataset.
- MLflow is used for experiment tracking and model registry.
- A FastAPI application serves model predictions.
- A Streamlit frontend provides a user interface.
- The application is containerized using Docker.

## Project Structure

ml-fastapi-docker/
│
├── main.py            # FastAPI application
├── train.py           # Model training + MLflow logging
├── app.py             # Streamlit frontend
├── model.joblib       # Saved trained model
├── requirements.txt   # Dependencies
├── Dockerfile         # Docker configuration
├── README.md

## Step 1: Train the Model with MLflow

Run:
python train.py

This will:
- train the model
- log parameters and metrics (accuracy, F1, etc.)
- save the model
- register it in MLflow (Model Registry)

## Step 2: Run MLflow UI

Run:
mlflow ui

Open:
http://127.0.0.1:5000

You will see:
- experiments
- runs
- metrics
- registered models and versions

## Step 3: Run FastAPI

Run:
python -m uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs

Test POST /predict using JSON input.

## Step 4: Run Streamlit Frontend

Run:
streamlit run app.py

Open:
http://localhost:8501

Enter feature values and get predictions via UI.

## Step 5: Build Docker Image

Run:
docker build -t ml-api .

## Step 6: Run Docker Container

Run:
docker run -p 8000:8000 ml-api

Then open:
http://127.0.0.1:8000/
http://127.0.0.1:8000/docs

## API Endpoints

GET /
Returns a message confirming the API is running.

POST /predict
Accepts input features and returns the predicted class.

## Technologies Used

Python  
scikit-learn  
FastAPI  
Uvicorn  
Streamlit  
MLflow  
Docker  

## Result

The project implements a full ML workflow:
- model training
- experiment tracking
- model versioning
- API deployment
- user interface

It demonstrates a simple but complete ML system.