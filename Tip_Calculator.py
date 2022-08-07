# Tip Calculator.
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15 or 20 ? "))
people = int(input("How many people to split the bill into? "))
tip_as_percent = tip / 100
total_tip_amount = tip_as_percent * bill
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each Person Should pay ${final_amount}")