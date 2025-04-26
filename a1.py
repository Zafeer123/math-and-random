import random
num = random.randint(0,10)
print("I have picked a number 1-10,try to guess it: ")
while True:
    guess = int(input("Guess the number: "))
    if guess == num:
        print("You won")
        break
    else:
        print("Try again")