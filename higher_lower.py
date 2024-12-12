import celeb
import random
import os

score = 0
os.system("clear")
index1 = random.randint(0,len(celeb.data)-1)
index2 = random.randint(0,len(celeb.data)-1)
if index2 == index1:
    index2 = random.randint(0,len(celeb.data)-1)



while True:
    if score > 0:
        os.system("clear")
        print(f"Correct! Current score: {score}")

    print(f"Compare A: {celeb.data[index1]["name"]}, a {celeb.data[index1]["description"]}, from {celeb.data[index1]["country"]}\n")
    print(f"Compare B: {celeb.data[index2]["name"]}, a {celeb.data[index2]["description"]}, from {celeb.data[index2]["country"]}")

    while True:
        try:
            answer = str(input("Who do you think has more followers: Type 'A' or 'B': ")).upper()
            if answer == "A" or answer == "B":
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter A or B")

    follower1 = celeb.data[index1]["follower_count"]
    follower2 = celeb.data[index2]["follower_count"]

    if answer == "A":
        if follower1 > follower2:
            score += 1
            index2 = random.randint(0,len(celeb.data)-1)
        else:
            print("Incorrect. Play again later")
            break
    if answer == "B":
        if follower2 > follower1:
            score += 1
            index1 = index2
            index2 = random.randint(0,len(celeb.data)-1)
        else:
            print("Incorrect. Play again later")
            break

print(f"Your final score was {score}")


