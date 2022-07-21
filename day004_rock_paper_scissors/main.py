import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper, or '2' for Scissors."))
computer_choice = random.randint(0, 2)

if user_choice == 0:
    print(rock)
    if computer_choice == 0:
        print(rock)
        print("draw.")
    elif computer_choice == 1:
        print(paper)
        print("computer win.")
    else:
        print(scissors)
        print("you win.")
elif user_choice == 1:
    print(paper)
    if computer_choice == 1:
        print(paper)
        print("draw.")
    elif computer_choice == 2:
        print(scissors)
        print("computer win.")
    else:
        print(rock)
        print("you win.")
elif user_choice == 2:
    print(scissors)
    if computer_choice == 2:
        print(scissors)
        print("draw.")
    elif computer_choice == 0:
        print(rock)
        print("computer win.")
    else:
        print(paper)
        print("you win.")
else:
    print("invalid player choice.")
