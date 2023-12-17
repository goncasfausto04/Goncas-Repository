import random

options = ["rock", "paper", "scissors"]

while True:
    play = input("Rock, Paper or Scissors?:").lower()
    if play.lower() in options:
        break
    else:
        print("Try again:")

pcplay = random.choice(options)

print(f"The computer chooses: {pcplay}")

if pcplay.lower() == play.lower():
    print("Tie")
if pcplay == "scissors" and play == "paper":
    print("You Loose")
elif pcplay == "scissors" and play == "rock":
    print("You Win")
elif pcplay == "rock" and play == "paper":
    print("You Win")
elif pcplay == "rock" and play == "scissors":
    print("You Loose")
elif pcplay == "paper" and play == "rock":
    print("You Loose")
elif pcplay == "paper" and play == "scissors":
    print("You Win")