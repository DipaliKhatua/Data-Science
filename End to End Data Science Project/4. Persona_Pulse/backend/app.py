# app.py
from flask import Flask, jsonify, request
from ai_engine import get_ai_reply

from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Endpoint to get AI-generated persona-based response
@app.route('/generate_reply', methods=['POST'])
def generate_reply():
    # Get user_id and message from the incoming JSON request
    data = request.get_json()

    user_id = data.get("user_id")
    message = data.get("message")

    if not user_id or not message:
        return jsonify({"error": "user_id and message are required"}), 400

    # Call the AI engine to get the response based on the user
    reply = get_ai_reply(user_id, message)
    
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
