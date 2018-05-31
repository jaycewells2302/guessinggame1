import random

n = random.randint(1, 100)

name = str(input("what is your name?: "))

print("Try to guess a number 1 to 100. You have unlimited tries.")

while True:
    guess = int(input(" "))
    if guess < n:
        print("Your number is too low " + str(name))
    elif guess > n:
        print("Your number is too high " + str(name))
    elif guess == n:
        break

print("Congratulations " + str(name) + "!!! You got the number. ")
