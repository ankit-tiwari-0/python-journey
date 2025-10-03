amount = int(input("what is your order amout"))

if amount >300 :
    print("your order amoount is more than 300, delivery is free")
    total = amount
else: 
    print("delivary charge is 30")
total = amount + 30

print("total amount to be :", total)



order_amount = int(input("Enter the order amount:"))


delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fess is : {delivery_fees}")