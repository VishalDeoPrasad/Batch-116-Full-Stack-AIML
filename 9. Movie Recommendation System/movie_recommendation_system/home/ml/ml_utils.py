import joblib 
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
simi_path = os.path.join(BASE_DIR, 'similarity.joblib')
simi_df = joblib.load(simi_path)

def recommend(movie_name):
    score = simi_df[movie_name]
    result = score.sort_values(ascending=False).head(10)
    return list(result.index)

def get_all_movies():
    return list(simi_df.index)