from flask import Flask, request, jsonify
import pickle
from sentence_transformers import SentenceTransformer, util


model_path = '../models/similarity_model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

# API endpoint
@app.route('/predict', methods=['POST'])
def predict_similarity():
    data = request.get_json()
    text1 = data.get('text1')
    text2 = data.get('text2')
    
    if not text1 or not text2:
        return jsonify({"error": "Both text1 and text2 are required"}), 400
    
    embedding1 = model.encode(text1, convert_to_tensor=True)
    embedding2 = model.encode(text2, convert_to_tensor=True)
    similarity_score = util.pytorch_cos_sim(embedding1, embedding2).item()
    
    return jsonify({"similarity_score": round(similarity_score, 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
