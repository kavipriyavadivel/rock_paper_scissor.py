import random
def choice(user_c,com_c):
    print(f"user's choice is {user_c}!!!")
    if com_c == 0:
        print(f"computer's choice is Rock!!!")
    elif com_c == 1:
        print(f"computer's choice is Paper!!!")
    else:
        print(f"computer's choice is Scissor!!!")
end = False
score = 0
user = input("Enter username: ")
while not end:
    user_input = input("Enter Rock, paper or scissor: ").lower()
    if user_input == "rock":
        user_choice = 0
    elif user_input == "paper":
        user_choice = 1
    elif user_input == "scissor":
        user_choice = 2
    else:
        print("Invalid Input!")
    computer_choice = random.randint(0, 2)
    if computer_choice == 2 and user_choice == 0:
        choice(user_input, computer_choice)
        print(f"{user} wins!!!")
        score = score + 1
    elif computer_choice == 0 and user_choice == 2:
        choice(user_input, computer_choice)
        print(f"Computer wins!!!")
    elif computer_choice > user_choice:
        choice(user_input, computer_choice)
        print(f"Computer wins!!!")
    elif user_choice > computer_choice:
        choice(user_input, computer_choice)
        print(f"{user} wins!!!")
        score = score + 1
    elif computer_choice == user_choice:
        choice(user_input, computer_choice)
        print(f"It's a tie!!!")
    end_game = input("Do you want to end the game(y or n): ").lower()
    if end_game == 'y':
        end = True
        print(f"Your total Score is {score}!!!")