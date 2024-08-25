import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
game_image = [rock,paper,scissors]
user_choice = int(input("enter your choice: type 0 for rock , 1 for paper, 2 for scissors: "))
print(game_image[user_choice])
if user_choice >= 3 or user_choice < 0:
    print("you entered invalid number, you lose.")
else:
    computer_choice = random.randint(0,2)
    print("Computer choice:")
    print(game_image[computer_choice])
    if computer_choice == user_choice:
        print("Its a draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("you lose")
    elif computer_choice == 0 and computer_choice == 2:
        print("You Win")
    elif computer_choice > user_choice:
        print("you lose")
    elif user_choice > computer_choice:
        print("you Win")
