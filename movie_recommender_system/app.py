# app.py (Main entry point)
import streamlit as st
from pages.home import home
from pages.movie_detail import movie_detail

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"
if "selected_movie_id" not in st.session_state:
    st.session_state.selected_movie_id = None

# Page router
if st.session_state.page == "home":
    home()
elif st.session_state.page == "movie":
    movie_detail()
