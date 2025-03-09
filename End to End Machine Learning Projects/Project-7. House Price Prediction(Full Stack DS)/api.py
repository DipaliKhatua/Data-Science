from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Load the trained model
model = joblib.load("house_price_prediction.pkl")


REQUIRED_FEATURES = ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        missing_features = [feature for feature in REQUIRED_FEATURES if feature not in data]
        if missing_features:
            return jsonify({"error": f"Missing features: {', '.join(missing_features)}"}), 400

        
        features = np.array([[data[feature] for feature in REQUIRED_FEATURES]])


        prediction = model.predict(features)[0]

        return jsonify({"predicted_price": float(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
