print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give?"))
people = int(input("How many people to split the bill? "))
individual_bill_inc_tip = round(bill/people) + (bill * tip / 100)
print(f"individual bill amount =${individual_bill_inc_tip}")


