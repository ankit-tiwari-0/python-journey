#walrus


#normal way
# value = 13
# reminder = value % 5

# if reminder:
#     print(f"Not divisible, reminder is {reminder}")


value = 13
if(reminder := value %5):
    print(f"not divisible, reminder is {reminder} ")



available_size = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup size:")) in available_size:
    print(f"Serving {requested_size} chai")

else:
    print(f"Size is unavaible - {requested_size}")    