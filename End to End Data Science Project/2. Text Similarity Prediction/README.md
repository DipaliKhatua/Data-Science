Text Similarity Prediction API

Project Overview

This project aims to build and deploy a Semantic Textual Similarity (STS) Model that predicts the similarity score (0-1) between two given text paragraphs. The similarity score quantifies the degree of semantic similarity.

Problem Statement:
# Note: The Dataset I have used for the project provided by DataNeuron.ai 
We have a dataset containing pairs of text paragraphs. Our objective is to:

Train a model that predicts similarity scores based on semantic meaning.

Deploy the model as a REST API using Flask, allowing users to send text pairs and receive a similarity score.

Project Structure

Text-Similarity-Project(DataNeuron -Task)/
│── data/
│   ├── DataNeuron_Text_Similarity.csv  
│── models/
│   ├── similarity_model.pkl           
│── app/
│   ├── app.py                          
│── requirements.txt                     
│── README.md                           
│── model.py                         

Steps Included:

Part A: Model Development

Preprocess the dataset (cleaning, tokenization, embeddings).

Train a similarity model using Sentence-BERT.

Save the trained model as similarity_model.pkl.

Part B: Flask API Deployment

Create an API (/predict) to accept JSON input {text1, text2}.

Load the trained model and return similarity scores.

Test the API using Postman
Note: I have used Thunder-Client for testing. 

Deploy it on a local server using Flask.

API Usage:

Request Format

{
  "text1": "nuclear body seeks new tech ....",
  "text2": "terror suspects face arrest ......"
}

Response Format

{
  "similarity_score": 0.2
}

Installation & Running the API

# Create a virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
python app/app.py


Author: Dipali Khatua

For queries, contact: [khatuadipsha@gmail.com]


