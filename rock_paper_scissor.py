import random

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']


while True:
    user_input = input("Enter a choice (rock, paper, scissors): or q to quit: ").lower()
    if user_input == 'q':
       break 
    
    if user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue

    random_number = random.randint(1,3) 
    computer_pick = options[random_number - 1]
    print("Computer picked",computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("Rock smashes scissors! You win!")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("Paper covers rock! You win!")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("Scissors cuts paper! You win!")
        user_wins += 1
        continue
    elif user_input == computer_pick:  
        print("It's a tie")
        continue
    else:
        print("You lose this round!")
        
print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print("Good Bye!")
