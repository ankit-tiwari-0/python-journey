# chai = "Ginger chai"


# def prepare_chai(order):
#     print("preparing", order)

# prepare_chai(chai)
# print(chai)

chai = [1, 2 , 3]


def edit_chai(cup):  #here cup is peremeter
    cup[1] = 694

edit_chai(chai)    #here chai is our arrument
print(chai)



def make_chai(tea, milk, suger):
    print(tea, milk, suger)

make_chai("Darjeeling", "yes", "low") #position
make_chai(tea="Green", suger="Mediam", milk="nnn") #keyword


#kwargg

def special_chai(*args, **kwargs):
    print("Ingridient", args)
    print("Extras", kwargs)

special_chai("cinnamom", "cardmom", sweetener = "Honey", foam = "no")    

# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)


# def chai_order(order=None):
#     order.append("Masala")
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []
    order.append("Masala")
    print(order)

chai_order()
chai_order()


















# # This is a list representing a chai cup with some initial values
# chai = [1, 2, 3]

# # Define a function 'edit_chai' which takes a parameter 'cup' (a list)
# def edit_chai(cup):  # 'cup' is a parameter that expects a list
#     # Change the second element (index 1) of the list to 694
#     cup[1] = 694

# # Call the function 'edit_chai' and pass the 'chai' list as an argument
# edit_chai(chai)  # 'chai' is passed as the argument here
# print(chai)      # Prints the updated list after modification by the function


# # Define a function 'make_chai' that takes three parameters: tea, milk, and sugar
# def make_chai(tea, milk, sugar):
#     # Print the values of tea, milk, and sugar
#     print(tea, milk, sugar)

# # Call 'make_chai' using positional arguments (order matters)
# make_chai("Darjeeling", "yes", "low")

# # Call 'make_chai' using keyword arguments (order does not matter)
# make_chai(tea="Green", sugar="Medium", milk="no")


# # Define a function 'special_chai' that accepts any number of positional and keyword arguments
# def special_chai(*args, **kwargs):
#     # args is a tuple of all positional arguments
#     print("Ingredients:", args)
#     # kwargs is a dictionary of all keyword arguments
#     print("Extras:", kwargs)

# # Call 'special_chai' with multiple ingredients and extra options
# special_chai("cinnamon", "cardamom", sweetener="Honey", foam="no")


# # Define a function 'chai_order' that uses a default mutable argument safely
# def chai_order(order=None):
#     # If no list is passed, create a new empty list
#     if order is None:
#         order = []
#     # Append the string "Masala" to the list
#     order.append("Masala")
#     # Print the current state of the order list
#     print(order)

# # Call 'chai_order' twice to see that it doesn't remember previous calls
# chai_order()  # Output: ['Masala']
# chai_order()  # Output: ['Masala'] again, new list each time
