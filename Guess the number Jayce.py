import random

n = random.randint(1, 100)

print("Try to guess a number 1 to 100. You have unlimited tries.")

while True:
    guess = int(input(" "))
    if guess < n:
        print("Your number is too low.")
    elif guess > n:
        print("Your number is too high.")
    elif guess == n:
        break

print("Congratulations!!! You got the number.")