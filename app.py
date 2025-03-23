import pickle
import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title('Movie Recommender System')

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    if poster_path:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    else:
        return "https://via.placeholder.com/500x750?text=Poster+Not+Available"

try:
    movies_df = pickle.load(open('movies.pkl', 'rb'))
    movies = movies_df['title'].values
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    selected_movie_name = st.selectbox('Select a movie', movies)

    def recommend(movie):
        try:
            movie_index = movies_df[movies_df['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_movies = []
            for i in movies_list:
                movie_id = movies_df.iloc[i[0]].movie_id
                movie_title = movies_df.iloc[i[0]].title
                movie_poster = fetch_poster(movie_id)
                recommended_movies.append((movie_title, movie_poster))
            return recommended_movies
        except IndexError:
            st.error("Movie not found.")
            return []

    if st.button('Recommend'):
        recommendations = recommend(selected_movie_name)
        if recommendations:
            st.subheader("Recommended Movies:")
            cols = st.columns(5)
            for i, (movie_title, movie_poster) in enumerate(recommendations):
                with cols[i]:
                    st.text(movie_title)
                    st.image(movie_poster, use_container_width=True) 
        else:
            st.write("No recommendations found.")

except FileNotFoundError:
    st.error("Error: 'movies.pkl' or 'similarity.pkl' not found.")
except Exception as e:
    st.error(f"An error occurred: {e}")