import requests

API_KEY = "62a7695d7c12db066f9f837da180bd19"

def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    res = requests.get(url)
    if res.status_code != 200:
        return {}
    data = res.json()
    return {
        "id": movie_id,
        "title": data.get("title", "N/A"),
        "poster": "https://image.tmdb.org/t/p/original" + data.get("poster_path", ""),
        "overview": data.get("overview", "N/A"),
        "release_date": data.get("release_date", "N/A"),
        "rating": data.get("vote_average", "N/A"),
        "genres": [g["name"] for g in data.get("genres", [])],
        "homepage": data.get("homepage", ""),
    }

def fetch_youtube_trailer(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}"
    res = requests.get(url)
    if res.status_code != 200:
        return None

    data = res.json().get("results", [])
    for video in data:
        if video["site"] == "YouTube" and video["type"] == "Trailer":
            return f"https://www.youtube.com/embed/{video['key']}"
    return None

