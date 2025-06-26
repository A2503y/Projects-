import random

easy_word = ["apple","train","book","money","bottle"]
medium_word = ["computer","keyboard","guitar","science","football"]
hard_word = ["program","python","laptop","diamond","university"]

print("Welcome to the Guessing Game!")
print("Choose a difficulty level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

level = input("Enter the difficulty level (1/2/3): ").lower()
if level == "1":
    word = random.choice(easy_word)
elif level == "2":
    word = random.choice(medium_word)
elif level == "3":
    word = random.choice(hard_word)
else:
    print("Invalid choice. Defaulting to easy level.")
    word = random.choice(easy_word)

attempts = 0
print("\n Guess the word!")

while True:
    guess = input("Enter your guess:").lower()
    attempts += 1

    if guess == word:
        print(f"Congratulations! You've guessed the word '{word}' in {attempts} attempts.")
        break

    hint = ""

    for i in range(len(word)):
        if i < len(guess) and guess[i] == word[i]:
            hint += word[i]
        else:
            hint += "_"

    print(f"Hint: {hint}")
    
print("Game Over! Thanks for playing.")