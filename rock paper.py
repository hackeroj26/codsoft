import random
points=0

while True:
    user_choice = input("Enter a  choice(rock, paper, scissor):")
    choices = ["rock","paper","scissors"]
    comp_choice = random.choice(choices)
    print(f"Your choice:{user_choice} ,Computer choice:{comp_choice}")

    if user_choice == comp_choice:
        print(f"Both players selected {user_choice}. It's a tie")
    elif user_choice == "rock":
        if comp_choice == "scissors":
            points=points+1
            print("Rock smashes scissors! You win.")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == "paper":
        if comp_choice == "rock":
            points=points+1
            print("Paper covers rock! You win.")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "scissor":
        if comp_choice == "paper":
            points=points+1
            print("Scissors cuts paper! You win.")
        else:
            print("Rock smashes scissors! You lose.")
    play=input("Play Again? (y/n): ")
    if play.lower()!="y":
        print("Your Scored: ",points)
        print("Thank You for playing!")
        break
