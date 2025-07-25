import pickle
import streamlit as st

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

# Streamlit app header
st.header('Movie Recommender System Using Machine Learning')

# Load pre-trained data
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# Movie selection dropdown
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Button to show recommendations
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    for name in recommended_movie_names:
        st.text(name)