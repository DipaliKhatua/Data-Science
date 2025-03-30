# House Price Prediction - Machine Learning Project

## Author: Dipali Khatua

## Project Overview

This project is a demonstration of end-to-end machine learning model development and deployment for house price prediction. The objective is to build and deploy a machine learning model that predicts house prices based on various features.

## Task Requirements

1. **Data Preprocessing**

   - Load the dataset from `sklearn.datasets.fetch_california_housing`
   - Handle missing values
   - Perform feature engineering (scaling, encoding, feature selection)
   - Visualize correlations between features and the target variable

2. **Model Training & Evaluation**

   - Split data into training and testing sets
   - Train regression models such as Random Forest Regressor
   - Evaluate using RMSE, MAE, and R² scores
   - Optimize the model with hyperparameter tuning
   - Save the trained model using Joblib

3. **Model Deployment**

   - Create a REST API using Flask
   - Develop a `/predict` endpoint for price prediction
   - Test the API using Postman/Thunderclient
   - Develop a basic front-end web UI to interact with the API

## Project Structure

```
├── house_price_prediction.ipynb  # Jupyter Notebook with ML model
├── api.py                        # Flask API for predictions
├── README.md                     # Project documentation
├── requirements.txt               # List of dependencies
├── house_price_prediction.pkl     # Saved trained model
├── house_prediction.html          # Front-end UI for API interaction
```

## How to Run

### 1. Install dependencies

pip install -r requirements.txt

### 2. Run the Flask API

python api.py


### 3. Test API with Postman or ThunderClient

Send a POST request to:

```
http://127.0.0.1:5000/predict
```

With JSON payload:

```json
{
  "MedInc": 5.0,
  "HouseAge": 20,
  "AveRooms": 5.5,
  "AveBedrms": 1.2,
  "Population": 3000,
  "AveOccup": 2.5,
  "Latitude": 37.5,
  "Longitude": -122.0
}
```

### 4. Run the Web UI

Open `house_prediction.html` in a browser and enter feature values to test the API.

## Model Performance

- **Mean Absolute Error (MAE):** *value*
- **Root Mean Squared Error (RMSE):** *value*
- **R² Score:** *value*

## Notes

- The dataset used is the **California Housing Dataset** from Scikit-learn.
- Flask is used for building the REST API.
- Random Forest is used as the regression model.
- A basic front-end UI is created to interact with the API.

## License

This project is for educational purposes only and is not intended for commercial use.
