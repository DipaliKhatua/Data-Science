import streamlit as st
import requests
import json

# Streamlit app interface
st.title("PersonaPulse - AI-Powered Personas")

# Input fields for user_id and message
user_id = st.text_input("Enter your user ID", "")
message = st.text_area("Ask your question", "")

# Button to send request to Flask API
if st.button("Generate Reply"):
    if user_id and message:
        # Make the API call to Flask server
        response = requests.post("http://127.0.0.1:5000/generate_reply", 
                                 json={"user_id": user_id, "message": message})
        
        # Get the AI response from the Flask API
        if response.status_code == 200:
            data = response.json()
            st.write("AI Response: ", data["reply"])
        else:
            st.write("Error:", response.status_code, response.text)
    else:
        st.write("Please fill in both fields (User ID and Message).")
