# ML Model Deployment with FastAPI and Docker

This project demonstrates how to train a simple machine learning model and deploy it as an API using FastAPI and Docker.

## Project Overview

- A Logistic Regression model is trained on the Iris dataset.
- The trained model is saved as model.joblib.
- A FastAPI application is created to serve predictions.
- The application is containerized using Docker.

## Project Structure

ml-fastapi-docker/
│
├── main.py
├── train.py
├── model.joblib
├── requirements.txt
├── Dockerfile
├── README.md

## Step 1: Train the Model

Run:
python train.py

This will train the model and save it as model.joblib.

## Step 2: Run API Locally

Run:
uvicorn main:app --reload

Open in browser:
http://127.0.0.1:8000/
http://127.0.0.1:8000/docs

## Step 3: Test Prediction Endpoint

Go to /docs and use POST /predict.

Example input:
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

Example response:
{
  "prediction": 0
}

## Step 4: Build Docker Image

Run:
docker build -t ml-api .

## Step 5: Run Docker Container

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
Docker  

## Result

The model is successfully deployed as an API and works both locally and inside a Docker container.