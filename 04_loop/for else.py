staff = [("Amit", 16), ("Zara",17),("raj", 15)]


for name, age in staff:
    if age <= 18:
        print(f"{name}is eligible to manage the staff")
        break

else:
    print(f"No one is eligible")    



 #  else block only run if the loop did't break 
 # use it when for something it not found fallback logic