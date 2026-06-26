mrp=float(input("enter mrp of book:"))
dis=0
net=0
if mrp>=500:
    dis=mrp*10/100
else:
    dis=mrp*5/100

net=mrp-dis
print(f"Mrp={mrp},Dis={dis},Net price{net}")