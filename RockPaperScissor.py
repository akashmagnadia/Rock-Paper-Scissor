import random

user = "Rock"

while (user != "Out"):
    user = (input("Rock, Paper, Scissor: "))

    randint = random.randint(1,3)

    if (randint == 1):
        computer = "Rock"
    elif (randint == 2):
        computer = "Paper"
    else:
        computer = "Scissor"
    
    print("User: " + user)
    print("Computer: " + computer)


    if (((user == "Rock") & (computer == "Scissor")) | ((user == "Paper") & (computer == "Rock")) | ((user == "Scissor") & (computer == "Paper"))):
        print("User Wins!")
    elif (((computer == "Rock") & (user == "Scissor")) | ((computer == "Paper") & (user == "Rock")) | ((computer == "Scissor") & (user == "Paper"))):
        print("Computer Wins!")
    else:
        print("It's a draw")

    user = (input("To play another game press any key, To exit the game: Out"));

