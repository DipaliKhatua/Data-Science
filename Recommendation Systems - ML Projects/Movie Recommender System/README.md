# Movie Recommender System

This project is a **Movie Recommender System** built using **Streamlit** and **Machine Learning**. It provides movie recommendations based on content similarity, using a pre-trained similarity model. We can run it locally on our machine with minimal setup.

---

## Features
- **Content-Based Recommendations**: Suggests movies similar to a selected movie.
- **User-Friendly Interface**: Built with Streamlit for ease of interaction.
- **Local Execution**: Runs on your local machine without any deployment requirements.

---

## Prerequisites
Make sure your system meets the following requirements:
- Python 3.7 or higher installed.
- Libraries: `streamlit`, `pandas`, `pickle-mixin`, `sckit-learn`, `nltk`.

---
# Run the application"
Usage
- Run the Streamlit application:python -m streamlit run app.py

- Open the application in your web browser. The application typically run
http://localhost:8501

File Structure
├── app.py               # Main Streamlit application script
├── model/           # Folder for pre-trained model artifacts
│   ├── movie_list.pkl   # Pickled file containing the movie dataset
│   ├── similarity.pkl   # Pickled file containing the similarity matrix
├── README.md            # Project documentation

# Example Walkthrough
- Launch the application using the command:python -m streamlit run app.py

- On the web interface:- Select a movie from the dropdown (e.g., Inception).
- The system will recommend 5 similar movies based on the pre-trained similarity model.

- Example output for the movie Inception:Recommended Movies:
- Interstellar
- The Dark Knight
- Memento
- The Prestige
- Shutter Island



Connect me : https://www.linkedin.com/in/dipalikhatua/
