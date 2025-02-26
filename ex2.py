import pandas as pd

url_ratings = "https://files.grouplens.org/datasets/movielens/ml-100k/u.data"
column_names = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_csv(url_ratings, sep="\t", names=column_names, usecols=["user_id", "movie_id", "rating"])

url_movies = "https://files.grouplens.org/datasets/movielens/ml-100k/u.item"
movies = pd.read_csv(url_movies, sep="|", encoding="latin-1", names=["movie_id", "title"], usecols=[0, 1])

user_ratings_count = ratings.groupby('user_id').size()
active_users = user_ratings_count[user_ratings_count >= 10].index
ratings_filtered = ratings[ratings['user_id'].isin(active_users)]

movie_avg_rating = ratings_filtered.groupby('movie_id')['rating'].mean()
movie_ratings_count = ratings_filtered.groupby('movie_id').size()

movie_popularity = pd.DataFrame({
    'avg_rating': movie_avg_rating,
    'num_ratings': movie_ratings_count
})

movie_popularity = movie_popularity.sort_values(by='num_ratings', ascending=False)

movie_popularity = movie_popularity.merge(movies, on='movie_id')

top_5_movies = movie_popularity[['title', 'avg_rating', 'num_ratings']].head(5)

print(top_5_movies)
