import random

again = True

while again:
    print(random.randint(1,6))
    another_roll = input("Want to roll the dice again? (Y/N): ")
    if another_roll.lower()== "y":
        continue
    else:
        print("Thanks for plying see you soon ")
        break