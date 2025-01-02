"""
from random import randint

user_choice = int(input("Choose number:"))
pc_choice = randint(1, 50)

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower! Computer choice ", pc_choice)
elif user_choice < pc_choice:
    print("Higher! Computer choice ", pc_choice)
"""

# while 구문
distance = 0

while distance < 20:
    print(f"I'm running: {distance}km" )
    distance += 1