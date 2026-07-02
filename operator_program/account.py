premium = float(input("Enter monthly premium: "))

maturity_amount = (premium / 5) * 345.40

print("Maturity Amount =", maturity_amount)

#cild,young and old fare
childs = int(input("Enter number of childs: "))
youngs = int(input("Enter number of youngs: "))
olds = int(input("Enter number of olds: "))

child_fare = childs * 450
young_fare = youngs * 650
old_fare = olds * 500

total_fare = child_fare + young_fare + old_fare

print("Fare of Childs =", child_fare)
print("Fare of Youngs =", young_fare)
print("Fare of Olds =", old_fare)
print("Total Fare =", total_fare)