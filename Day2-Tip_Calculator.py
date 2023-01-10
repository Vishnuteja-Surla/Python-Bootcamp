print("Welcome to the Bill Generator")
bill = float(input("What is the total bill? "))
people = int(input("How many people are going to split the bill? "))
tip_percent = float(input("Percentage of tip : "))
tip = bill*tip_percent/100
pay = (bill + tip) / people
print(f"Each person should pay {round(pay,2)}")