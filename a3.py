import random
while True:
    user = input("Enter either rock paper or scissors: ")
    possAct = ["rock",'paper','scissors']
    comp = random.choice(possAct)
    print("You chose",user,'Computer chose',comp)

    if user == comp:
        print("Tie")
    elif user == "rock":
        if comp == 'scissors':
            print("You won")
        else:
            print("You lose")
    elif user == "paper":
        if comp == 'scissors':
            print("You lost")
        else:
            print("You win")
    elif user == "scissors":
        if comp == 'rock':
            print("You win")
        else:
            print("You lose")
    break
