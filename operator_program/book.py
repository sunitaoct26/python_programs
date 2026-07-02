mrp = float(input("Enter MRP of book: "))
discount_percent = float(input("Enter discount percentage: "))

discount_price = (mrp * discount_percent) / 100
net_price = mrp - discount_price

print("Discount Price =", discount_price)
print("Net Price =", net_price)