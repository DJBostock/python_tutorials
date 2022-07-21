import random

names_string = input("Give me everybody's names, separated by a comma: ")

names = names_string.split(",")

number_of_names = len(names)

random_index = random.randint(0, number_of_names - 1)

chosen_name = names[random_index].strip()

print(f"The person who will pay is: {chosen_name}")