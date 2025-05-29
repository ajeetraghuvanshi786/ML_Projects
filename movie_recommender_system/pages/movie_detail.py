import streamlit as st
from utils.api_utils import fetch_movie_details, fetch_youtube_trailer

def movie_detail():
    movie_id = st.session_state.selected_movie_id
    movie = fetch_movie_details(movie_id)
    trailer_url = fetch_youtube_trailer(movie_id)

    st.markdown("""
        <style>
        /* Hide sidebar */
        [data-testid="stSidebar"] {
            display: none;
        }

        /* Center layout spacing */
        .block-container {
            padding-left: 3rem;
            padding-right: 3rem;
        }

        /* Poster styling */
        .movie-detail-poster {
            width: 100%;
            max-width: 300px;
            border-radius: 16px;
            box-shadow: 0 0 20px rgba(0,0,0,0.3);
            transition: transform 0.3s ease;
        }

        .movie-detail-poster:hover {
            transform: scale(1.05);
        }

        /* Title styling */
        .movie-title {
            text-align: center;
            font-size: 2.2rem;
            margin-bottom: 10px;
        }

        /* Back button */
        .back-button {
            display: inline-block;
            background-color: #262730;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            margin-top: 20px;
            font-weight: 500;
            transition: background-color 0.3s ease;
            border: none;
        }

        .back-button:hover {
            background-color: #444;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

    # Movie Title
    st.markdown(f"<div class='movie-title'>{movie['title']}</div>", unsafe_allow_html=True)

    # Poster Centered
    st.markdown(
        f"<div style='text-align: center;'><img class='movie-detail-poster' src='{movie['poster']}'></div>",
        unsafe_allow_html=True
    )

    # Movie Metadata
    st.markdown("### 🎬 Movie Details")
    st.markdown(f"**Genres:** {', '.join(movie['genres'])}")
    st.markdown(f"**Release Date:** {movie['release_date']}")
    st.markdown(f"**Rating:** {movie['rating']} ⭐")
    st.markdown(f"**Overview:** {movie['overview']}")

    if movie["homepage"]:
        st.markdown(f"[🌐 Visit Official Site]({movie['homepage']})")

    # YouTube Trailer
    if trailer_url:
        st.markdown("### 🎞️ Official Trailer")
        st.video(trailer_url)
    else:
        st.info("🎥 Trailer not available.")

    # Back button (visible)
    st.button("🔙 Back to Recommendations", on_click=lambda: st.session_state.update({"page": "home"}))
