# MOVIE RECOMMENDATION SYSTEM

# Importing libraries
import streamlit as st
import pandas as pd
import pickle
import requests

# Fetch Poster Path Function
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url).json()
    full_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return full_path

# Movie Recommendation Function
def recommend(selected_movie):
    index = movies[movies['title'] == selected_movie].index[0]
    movies_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in movies_list:
        # Fetch Movie Poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_posters , recommended_movie_names

# Loading Data Frames
similarity = pickle.load(open('similarity.pkl','rb'))
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

# Webpage
st.title('Movie Recommender System') # Title
selected_movie = st.selectbox("Type/Select a movie from the dropdown" , movies['title'].values) # Dropdown-Menu

if st.button('Show Recommendation'): # Button
    recommended_movie_posters , recommended_movie_names = recommend(selected_movie)
    col1 , col2 , col3 , col4 , col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.text(recommended_movie_names[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.text(recommended_movie_names[1])
    with col3:
        st.image(recommended_movie_posters[2])
        st.text(recommended_movie_names[2])
    with col4:
        st.image(recommended_movie_posters[3])
        st.text(recommended_movie_names[3])
    with col5:
        st.image(recommended_movie_posters[4])
        st.text(recommended_movie_names[4])

st.text('© Copyright 2024 Akash Negi. All rights reserved.') # Footer

# END