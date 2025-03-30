import pandas as pd
import numpy as np
import torch
from sentence_transformers import SentenceTransformer, util
import pickle


df = pd.read_csv('data/DataNeuron_Text_Similarity.csv')


df = df.drop_duplicates().reset_index(drop=True)


model = SentenceTransformer('paraphrase-MiniLM-L6-v2')


def compute_similarity(text1, text2):
    embedding1 = model.encode(text1, convert_to_tensor=True)
    embedding2 = model.encode(text2, convert_to_tensor=True)
    return util.pytorch_cos_sim(embedding1, embedding2).item()


df['similarity_score'] = df.apply(lambda row: compute_similarity(row['text1'], row['text2']), axis=1)

model_path = 'models/similarity_model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f'Model saved successfully at {model_path}')
