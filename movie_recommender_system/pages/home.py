import io
import requests
import gdown
import streamlit as st
import pickle
import pandas as pd
from utils.api_utils import fetch_movie_details

# Load movie data
@st.cache_resource
def load_data():
    # File IDs from Google Drive
    movie_dict_id = "1X5ZZRFLdLSj38i2jDf1Oyu6AofyvCMd2"
    similarity_id = "1yMiXP6kFBhgGltWM7psmBJiDrWAYkZBE"

    # Construct download URLs
    movie_dict_url = f"https://drive.google.com/uc?export=download&id={movie_dict_id}"
    similarity_url = f"https://drive.google.com/uc?export=download&id={similarity_id}"

    # Download and load .pkl files
    movie_dict_path = "movie_dict.pkl"
    similarity_path = "similarity.pkl"

    gdown.download(movie_dict_url, movie_dict_path, quiet=False)
    gdown.download(similarity_url, similarity_path, quiet=False)

    # Load data from disk
    movies = pd.DataFrame(pickle.load(open(movie_dict_path, "rb")))
    similarity = pickle.load(open(similarity_path, "rb"))

    return movies, similarity

movies, similarity = load_data()

# Recommend function
def recommend(movie_title):
    index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [fetch_movie_details(movies.iloc[i[0]].movie_id) for i in movie_indices]

# Route to detail
def go_to_movie_page(movie_id):
    st.session_state.page = "movie"
    st.session_state.selected_movie_id = movie_id

# Home page
def home():
    # Styling
    st.markdown("""
        <style>
        [data-testid="stSidebar"] { display: none; }

        .block-container {
            padding-left: 2rem;
            padding-right: 2rem;
        }

        .title-container {
            text-align: center;
            margin-top: 2rem;
            margin-bottom: 2rem;
        }

        .stButton > button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 24px;
            font-size: 16px;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            margin-top: 10px;
        }

        .stButton > button:hover {
            background-color: #45a049;
        }

        .movie-title {
            text-align: center;
            font-weight: bold;
            font-size: 16px;
            color: white;
            margin-top: 8px;
        }

        .movie-card-center {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 30px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # App Title
    st.markdown('<div class="title-container"><h1>🎬 Movie Recommendation System Using Machine Learning</h1></div>', unsafe_allow_html=True)

    selected_movie = st.selectbox("Search and select a movie:", movies['title'].values)

    # Centered button
    col_space1, col_main, col_space2 = st.columns([1, 2, 1])
    with col_main:
        if st.button("Show Recommendation"):
            st.session_state.recommendations = recommend(selected_movie)
            st.session_state.selected_movie = selected_movie

    # Show selected movie in card format (centered)
    if "selected_movie" in st.session_state:
        selected = st.session_state.selected_movie
        movie_id = movies[movies['title'] == selected].iloc[0].movie_id
        movie = fetch_movie_details(movie_id)

        st.markdown("<div class='movie-card-center'>", unsafe_allow_html=True)
        html_block = f"""
        <div style='text-align: center; margin-top: 30px;'>
            <img src="{movie['poster']}" style="width:250px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);"/>
        </div>
        """
        st.markdown(html_block, unsafe_allow_html=True)

        # Center the actual Streamlit button (real logic)
        center_col1, center_col2, center_col3 = st.columns([2, 1, 2])
        with center_col2:
            if st.button("▶ Show Details", key="selected_detail_btn"):
                go_to_movie_page(movie["id"])
        st.markdown("</div>", unsafe_allow_html=True)

    # Show recommendations in grid
    if "recommendations" in st.session_state:
        recs = st.session_state.recommendations
        st.markdown("### 🎯 Top Recommendations")

        cols = st.columns(len(recs))
        for i, (col, movie) in enumerate(zip(cols, recs)):
            with col:
                st.image(movie["poster"], use_container_width=True)
                if st.button("▶ Show Details", key=f"detail_btn_{i}"):
                    go_to_movie_page(movie["id"])
