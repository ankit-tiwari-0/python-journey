amount = int(input("what is your order"))

if amount >300 :
    print("your order amoount is more than 300, delivery is free")
    total = amount
else: 
    print("delivary charge is 30")
total = amount + 30

print("total amount to be :", total)