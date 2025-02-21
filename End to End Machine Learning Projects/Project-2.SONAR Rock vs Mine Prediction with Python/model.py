# Importing Dependencies
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Data Collection and Data Processing 

# Loading dataset to pandas dataframe
sonar_data = pd.read_csv('Copy of sonar data.csv', header=None)

print(sonar_data)