# Importing Dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# ML algorithms 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import pickle  # to save the model for further deployment

# Step 1: Load the dataset
heart_data = pd.read_csv('heart.csv')
# print(heart_data)