# Math Score Prediction using Machine Learning

This project demonstrates an end-to-end data science pipeline to predict students' math scores based on various features such as gender, ethnicity, parental education, lunch type, test preparation, and more. The dataset used for this project was sourced from [Kaggle: Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams).

---

## Overview

The goal of this project is to leverage machine learning techniques to predict students' math scores. The pipeline includes data ingestion, preprocessing, model training, evaluation, and deployment-ready artifacts.

---

## Key Features

1. **Data Ingestion**:
   - Data is ingested from a MySQL database.
   - Utilized Python's `pymysql` and `pandas` libraries to fetch the dataset.

2. **Dataset**:
   - Dataset URL: [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams).
   - Features include:
     - Gender
     - Race/Ethnicity
     - Parental Level of Education
     - Lunch Type
     - Test Preparation Course
     - Reading Score
     - Writing Score
     - Math Score (Target Variable).

3. **Data Preprocessing**:
   - Handled missing data with `SimpleImputer`.
   - Applied feature scaling using `StandardScaler`.
   - Encoded categorical variables with `OneHotEncoder`.

4. **Model Training**:
   - Tried multiple machine learning models:
     - Random Forest Regressor
     - Gradient Boosting Regressor
     - XGBoost Regressor
     - CatBoost Regressor
     - Linear Regression
     - AdaBoost Regressor
   - Selected the best-performing model using GridSearchCV for hyperparameter tuning.

5. **Model Evaluation**:
   - Evaluation metrics:
     - R² Score
     - Mean Absolute Error (MAE)
     - Root Mean Squared Error (RMSE).

6. **Artifacts**:
   - Preprocessor and trained model are saved as `.pkl` files for reuse.

---

## Project Structure
End-to-End Data Science Project/
├── src/
│   ├── DSProject/
│       ├── components/
│       │   ├── data_ingestion.py
│       │   ├── data_transformation.py
│       │   ├── model_trainer.py
│       ├── exception.py
│       ├── logger.py
│       ├── utils.py
├── artifacts/
│   ├── preprocessor.pkl
│   ├── model.pkl
├── app.py
├── README.md
├── requirements.txt
├── .env

## Installation and Usage
### Prerequisites
- Python 3.8 or above
- MySQL database server
- Required libraries (listed in `requirements.txt`)

## @ Author:
Dipali Khatua
Connect with me on # LinkedIn (https://www.linkedin.com/in/dipalikhatua/)