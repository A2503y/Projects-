import random

# Sample movie database
movies = {
    "action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
    "comedy": ["The Grand Budapest Hotel", "Superbad", "Step Brothers", "The Hangover"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "Fight Club", "The Godfather"],
    "sci-fi": ["Inception", "Interstellar", "The Matrix", "Blade Runner 2049"],
    "romance": ["Pride & Prejudice", "La La Land", "The Notebook", "Before Sunrise"],
    "horror": ["Get Out", "The Conjuring", "Hereditary", "A Quiet Place"]
}

def recommend_movies(genre):
    genre = genre.lower()
    if genre in movies:
        recommendation = random.choice(movies[genre])
        print(f"\n🎥 You might enjoy: **{recommendation}** ({genre.title()})")
    else:
        print("Sorry, I don't have recommendations for that genre yet.")

def main():
    print("🎬 Welcome to the Movie Recommendation Bot!")
    print("Available genres: Action, Comedy, Drama, Sci-Fi, Romance, Horror")
    
    while True:
        user_input = input("\nWhat genre are you in the mood for? (type 'exit' to quit): ").strip()
        if user_input.lower() == "exit":
            print("Goodbye! Enjoy your movie 🎉")
            break
        recommend_movies(user_input)

if __name__ == "__main__":
    main()
