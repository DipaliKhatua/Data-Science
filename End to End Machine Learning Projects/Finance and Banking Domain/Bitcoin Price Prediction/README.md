B# itcoin Price Prediction Using Machine Learning

Author: Dipali Khatua

📌 Project Overview

This end-to-end Data Science project aims to predict Bitcoin prices based on historical market data. It covers the entire ML lifecycle, from data preprocessing to deployment via a Flask API with a basic UI. This project is ideal for understanding both financial data analysis and applying core ML concepts practically.

📂 Project Structure

Bitcoin_Price_Prediction/
│
├── data/
│   └── bitcoin.csv                    # Dataset (over 40K rows)
│
├── notebooks/
│   └── bitcoin_price_prediction.ipynb  # EDA, Feature Engineering, ML Model Building
│
├── models/
│   └── best_model.pkl                # Saved best-performing model
│
├── api/
│   └── app.py                        # Flask API for prediction
│
├── ui/
│   └── index.html                    # Basic UI to interact with API
│
└── README.md                         # Project Overview (this file)

📊 Dataset Overview

Source: Bitcoin historical prices (more than 40,000 rows)

Columns:

Date: Date of record

Open: Opening price

High: Highest price of the day

Low: Lowest price of the day

Close: Closing price

Adj Close: Adjusted close price

Volume: Volume of trades

💡 Goal:

Predict the next day's closing price or determine price movement trends (up/down), which helps in making informed investment or trading decisions.

🧠 Core Machine Learning Lifecycle

Exploratory Data Analysis (EDA): Trends, seasonality, correlation

Feature Engineering: Time-based features, lag values, rolling averages

Data Preprocessing: Handling missing values, scaling, encoding

Model Selection: Linear Regression, Random Forest, XGBoost, etc.

Evaluation: RMSE, MAE, R2 Score

Hyperparameter Tuning: GridSearchCV

Model Saving: Save best model as best_model.pkl

Deployment: Flask API with UI for real-time prediction

⚙️ Tools & Libraries Used

Python: Core language

Pandas, NumPy: Data manipulation

Matplotlib, Seaborn: Visualization

Scikit-learn: ML models & preprocessing

XGBoost/LightGBM: Advanced ML models

Flask: API Deployment

HTML/CSS: Basic UI

🎯 Learning Outcomes

Understand financial data behavior (volatility, trends)

Practice model selection for time-series/financial data

Develop a realistic, deployable ML solution

Gain exposure to Flask API & UI integration

Prepare for interview questions related to ML projects, evaluation, and deployment


