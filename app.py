import streamlit as st
import pickle as pk
import requests
from dotenv import load_dotenv
import os
load_dotenv("api_key.env")
API_KEY=os.getenv("TMDB_API_KEY")

try:
    movies = pk.load(open("movies_list.pkl", "rb"))
    similarity = pk.load(open("similarity.pkl", "rb"))
    movies_list = movies['title'].values
except FileNotFoundError:
    st.error("Required  files not found.")

st.header("Movies Recommendation")
value_select = st.selectbox("Select movie from drop down", movies_list)

def recommendation_of(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommended_movies = []
    recommend_poster = []
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommend_poster

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "poster_path" in data:
            incomplete_path = data["poster_path"]
            full_path = f"https://image.tmdb.org/t/p/w500/{incomplete_path}"
            return full_path


if st.button("Show Recommend"):
    movie_name, movie_poster = recommendation_of(value_select)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])

    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])

    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])

    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])

    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
