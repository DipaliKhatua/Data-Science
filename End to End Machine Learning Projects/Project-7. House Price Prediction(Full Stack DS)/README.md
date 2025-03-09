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

## Project Structure

```
├── house_price_prediction.py  # Main Python script with ML model and API
├── README.md                   # Project documentation
├── requirements.txt            # List of dependencies
├── house_price_prediction.pkl       # Saved trained model
```

## How to Run

### 1. Install dependencies


pip install -r requirements.txt


### 2. Run the Flask API


python house_price_prediction.py


### 3. Test API with Postman or ThunderClient


 "http://127.0.0.1:5000/predict" -H "Content-Type: application/json" -d '{"MedInc": 5.0, "HouseAge": 20, "AveRooms": 5, "Population": 3000, "Latitude": 37.0, "Longitude": -122.0}'


## Model Performance

- **Mean Absolute Error (MAE):** *value*
- **Root Mean Squared Error (RMSE):** *value*
- **R² Score:** *value*

## Notes

- The dataset used is the **California Housing Dataset** from Scikit-learn.
- Flask is used for building the REST API.
- Random Forest is used as the regression model.

## Future Improvements

- Implement Hyperparameter tuning using GridSearchCV.
- Improve model accuracy with feature engineering.
- Deploy the API using cloud services.

## License

This project is for educational purposes only and is not intended for commercial use.

