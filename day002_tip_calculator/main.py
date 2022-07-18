print("Welcome to the Tip Calculator.")

total_bill = float(input("What was the total bill?: "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15?: "))
number_people = int(input("How many people to split the bill?: "))

final_bill = total_bill * ((tip_percentage + 100) / 100) / number_people

print(f"Each person should pay ${final_bill: .2f}.")