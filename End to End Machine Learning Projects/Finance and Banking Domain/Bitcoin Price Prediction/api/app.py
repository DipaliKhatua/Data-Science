from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model = joblib.load('../models/best_bitcoin_rf_model.pkl')

# -------------------------
# Route for Web UI
# -------------------------
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # Serves UI form

# -------------------------
# API Route: For ThunderClient or Frontend
# -------------------------
@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        data = request.get_json()
        input_data = [
            data['Open'], data['High'], data['Low'], data['Volume'],
            data['Price_Change'], data['Daily_Return'], data['MA_5'], data['MA_10']
        ]
        prediction = model.predict([input_data])[0]
        return jsonify({'predicted_close_price': round(prediction, 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# -------------------------
# Web UI Form Submission Route
# -------------------------
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Fetch form data
        input_data = [
            float(request.form['Open']),
            float(request.form['High']),
            float(request.form['Low']),
            float(request.form['Volume']),
            float(request.form['Price_Change']),
            float(request.form['Daily_Return']),
            float(request.form['MA_5']),
            float(request.form['MA_10'])
        ]
        prediction = model.predict([input_data])[0]
        return render_template('index.html', prediction_text=f'Predicted Close Price: ${round(prediction, 2)}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

# -------------------------
# Run the Flask App
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)
