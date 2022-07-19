print("Welcome to Forest Adventure.")
print("Your goal is to find the treasure.")

print("You stand at a crossroads.")
choice1 = input("Type 'Left' or 'Right' to choose a path.").lower()
if choice1 == 'left':
    print("You come to a lake. There is an island in the middle.")
    choice2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()
    if choice2 == 'wait':
        print("You arrive at the island unharmed. There is a house with three doors.")
        choice3 = input("Type 'Blue', 'Red', or 'Yellow' to choose the door of that color.").lower()
        if choice3 == 'blue':
            print("You enter a room of beasts. Game over.")
        elif choice3 == 'red':
            print("You enter a room full of fire. Game over.")
        elif choice3 == 'yellow':
            print("You found the treasure! You win!")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You are attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game over.")