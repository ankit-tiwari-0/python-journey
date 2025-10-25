#list comprehensive

menu = [
    "Masala chai",
    "Iced Lenon Tea",
    "Green Tea",
    "Iced Peach Tea",
    " Iced Ginger chai"
]


iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea ]
            # exprestion for item in iterable if condition

print(iced_tea)



# expression → what you want to include in the new list (here it’s my_tea)

# item in iterable → loop through each item in the list (menu)

# if condition → include only the items that meet a condition (here, those containing "Iced")

# if "Iced" in my_tea → This checks whether the word "Iced" appears in each tea name.

# Result: Only items containing "Iced" are added to the new list.