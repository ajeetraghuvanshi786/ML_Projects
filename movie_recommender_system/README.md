
# 🎬 Movie Recommendation System

This is a **Movie Recommendation System** built using **Python**, **Streamlit**, and **The Movie Database (TMDb) API**. It recommends movies based on user selection using cosine similarity on movie vectors. It also fetches movie details, posters, and trailers dynamically using the TMDb API.

---

## 📦 Project Features

- 🔍 Search and select movies
- 🎯 Recommend 5 similar movies based on cosine similarity
- 📽️ View poster, genre, rating, and overview of movies
- 🎞️ Watch the official trailer via embedded YouTube player
- ☁️ Loads large `.pkl` files (movie data and similarity matrix) dynamically from **Google Drive**
- 🧠 Simple, intuitive, and responsive UI with **Streamlit**

---

## 📁 Project Structure

```bash
movie_recommender_system/
│
├── app.py                     # Entry point of the Streamlit app
├── pages/
│   ├── home.py                # Home page UI and recommendation logic
│   └── movie_detail.py        # Movie detail and trailer display
│
├── utils/
│   └── api_utils.py           # TMDb API fetch logic
│
├── data/                      # (Optional local .pkl storage if needed)
└── README.md
```

---

## ⚙️ Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ajeetraghuvanshi786/ML_Projects/movie_recommender_system.git
cd movie_recommender_system
```

### 2. Create and Activate Virtual Environment (Recommended)

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/Mac
.venv\Scripts\activate         # Windows
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install manually:

```bash
pip install streamlit pandas numpy requests gdown
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🌐 Dynamic Data Loading from Google Drive

To handle large `.pkl` files (which cannot be pushed to GitHub), this app dynamically downloads them using [gdown](https://pypi.org/project/gdown/).

### Required Google Drive Setup:

1. Upload the following `.pkl` files to your Google Drive:
   - `movie_dict.pkl`
   - `similarity.pkl`

2. Make them shareable to "Anyone with the link".

3. Extract the **file ID** from the shareable link. For example:

```
https://drive.google.com/file/d/1X5ZZRFLdLSj38i2jDf1Oyu6AofyvCMd2/view?usp=sharing
                         ↑↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
                         This is your file ID
```

4. In `home.py`, the data is fetched dynamically as:

```python
import gdown

movie_dict_id = "1X5ZZRFLdLSj38i2jDf1Oyu6AofyvCMd2"
similarity_id = "1yMiXP6kFBhgGltWM7psmBJiDrWAYkZBE"

movie_dict_url = f"https://drive.google.com/uc?export=download&id={movie_dict_id}"
similarity_url = f"https://drive.google.com/uc?export=download&id={similarity_id}"

gdown.download(movie_dict_url, "movie_dict.pkl", quiet=False)
gdown.download(similarity_url, "similarity.pkl", quiet=False)
```

---

## 🔧 Making Changes

If you want to use your own data:

1. Train your recommender and export:
   - A dictionary of movies: `movie_dict.pkl`
   - A cosine similarity matrix: `similarity.pkl`

2. Upload both to Google Drive.

3. Update the file IDs in `home.py`.

---

## 📡 TMDb API

The app uses TMDb API to fetch metadata and trailers.

- You need to create an account at [https://www.themoviedb.org/](https://www.themoviedb.org/) and generate an API key.
- Replace the `API_KEY` in `api_utils.py`:

```python
API_KEY = "your_tmdb_api_key_here"
```

---



