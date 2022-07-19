print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
combined_name = name1 + name2

first_digit = 0
first_digit += combined_name.count("t")
first_digit += combined_name.count("r")
first_digit += combined_name.count("u")
first_digit += combined_name.count("e")

second_digit = 0
second_digit += combined_name.count("l")
second_digit += combined_name.count("o")
second_digit += combined_name.count("v")
second_digit += combined_name.count("e")

love_score = int(str(first_digit) + str(second_digit))

if love_score < 10 or love_score > 90:
    print(f"Your love score is: {love_score}. You go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your love score is: {love_score}. You are alright together.")
else:
    print(f"Your love score is: {love_score}.")
