# PersonaPulse - AI-Powered Personas

## Project Overview
**PersonaPulse** is an AI-powered platform where users can interact with dynamic AI personas. By providing a **user_id** and a **message**, users can get personalized replies from an AI persona that mimics their unique profile. This project leverages Flask for the backend and Streamlit for the user interface.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: Streamlit (Python)
- **AI Model**: Open-source pre-trained model for generating AI responses
- **CORS**: Flask-CORS for enabling cross-origin requests between frontend and backend
- **HTTP Requests**: Python `requests` library for communication between frontend and backend

## Features
- Input fields for **user_id** and **message**.
- Sends a POST request to the Flask API with the user’s **user_id** and **message**.
- AI model processes the request and returns a dynamic response based on the user’s profile.
- Displays the AI-generated reply on the frontend.

## Setup and Run Instructions


# Install required libraries
pip install -r requirements.txt
1. Start the Flask Backend
In the project directory, run the Flask backend API.

This will start the Flask server at http://127.0.0.1:5000.

2. Run the Streamlit Frontend
In a separate terminal window, navigate to the project directory and start the Streamlit app.
streamlit run frontend.py
This will open the Streamlit interface in your default web browser.

3. Interact with the AI
Input a user_id in the provided field.

Enter your message (question) in the text area.

Click the Generate Reply button.

View the AI-generated response based on your persona.

# Example Interaction
User ID: "1"
Message: "Tell me something about my persona."

AI Response: "You're a Data Scientist and enjoy exploring AI-based projects..."

# Challenges Faced
AI Integration: Handling persona-based responses dynamically based on user input. (Though I am working on it..)
CORS Issue: Enabling communication between the Streamlit frontend and Flask backend with Flask-CORS.
Frontend Design: Ensuring an intuitive, easy-to-use interface in Streamlit for seamless user interaction.

# Author
@Dipali Khatua
Data Scientist | AI Enthusiast 
# GitHub Profile  - https://github.com/DipaliKhatua
# LinkedIn Profile - https://www.linkedin.com/in/dipalikhatua/

Connect
If you have any questions, suggestions, or feedback, feel free to connect with me:
https://www.linkedin.com/in/dipalikhatua/

# License
This project is licensed under the MIT License.




