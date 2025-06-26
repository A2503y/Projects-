name = input("Hey type your name: ")
print(f"Hello {name} Welcome to my game!")

should_we_play = input("Do you want to play? (yes/no)or(y/n): ")
score = 0
if should_we_play.lower() == "yes" or should_we_play.lower() == "y":
    print("Let's play")
    direction = input("Do you want to go left or right? ")
    if direction.lower() == "left":
        print("Okay you went left and fell into a lava pit and you died")
    elif direction.lower() == "right":
        print("Okay you went right")
        choice = input("Okay you now see the bridge,do u wanna swim under or u wanna cross the river ? ")
        if choice.lower() == "swim under":
            print("Okay you swam under and got eaten by a shark and died")
        elif choice.lower() == "cross the river":
            print("Okay you crossed the river and you cleared the level")
            print("Congrats you cleared the level!")
            score +=1
        else:
            print("Invalid choice, you died")
        print("Welcome to new level!")
        print("You are in a forest and you see a bear")
        choice2 = input("Do you wanna run or fight the bear? ")
        if choice2.lower() == "run":
            print("Okay you ran and you failed the level!")
        elif choice2.lower() == "fight":
             print("Okay you fought and you cleared the level and got a reward!")
             score +=1
        else:
             print("Invalid choice, you died")
        
    else:
        print("Invalid input,you die")
else:
    print("Okay, maybe next time")