import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset of movies
data = {
    "Title": [
        "The Matrix",
        "The Matrix Reloaded",
        "The Godfather",
        "The Dark Knight",
        "Pulp Fiction",
        "Inception",
        "Interstellar",
        "The Prestige",
        "Memento",
        "The Social Network",
    ],
    "Genre": [
        "Sci-Fi, Action",
        "Sci-Fi, Action",
        "Crime, Drama",
        "Action, Crime, Drama",
        "Crime, Drama",
        "Action, Sci-Fi",
        "Adventure, Drama, Sci-Fi",
        "Drama, Mystery, Sci-Fi",
        "Mystery, Thriller",
        "Biography, Drama",
    ],
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Print the dataset
print("Movie Dataset:")
print(df)

# Step 1: Create a TF-IDF Vectorizer to process the "Genre" column
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["Genre"])

# Step 2: Calculate cosine similarity based on the TF-IDF matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend movies based on title
def recommend_movies(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = df[df["Title"] == title].index[0]

    # Get the pairwise similarity scores of all movies with the input movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 5 most similar movies (excluding the input movie itself)
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 5 most similar movies
    return df["Title"].iloc[movie_indices]

# Main program
print("\nWelcome to the Movie Recommendation System!")
print("Here are the available movies:")
print(df["Title"].to_string(index=False))

# Input from user
user_movie = input("\nEnter a movie title to get recommendations: ")

# Check if the movie exists in the dataset
if user_movie in df["Title"].values:
    recommendations = recommend_movies(user_movie)
    print("\nBecause you liked '{}', we recommend:".format(user_movie))
    for movie in recommendations:
        print(f"- {movie}")
else:
    print("Sorry, the movie is not in our dataset.")
