import random
import os

rand_num = random.randint(0, 100)
lives = 0
print("Thinking of a number 1 - 100")

print(f"Hint it is {rand_num}")
diffcult = str(input("Choose a diffculty: type 'easy' or 'hard'")).lower()

if diffcult == "easy":
    lives = 10
if diffcult == "hard":
    lives = 5
while lives > 0:
    guess = int(input("Make a guess: "))

    if guess == rand_num:
        print("Got it correct")
        break
    if guess < rand_num:
        print("Too low.\nGuess again")
        lives -= 1
        print(f"You have {lives} left")
    if guess > rand_num:
        print("Too high\nGuess again")
        lives -= 1
        print(f"You have {lives} left")