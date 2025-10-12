# Function demonstrating the use of 'nonlocal' to modify a variable from an enclosing function

def update_order():
    chai_type = "Elaichi"  # Variable in the enclosing (outer) function

    def kitchen():
        nonlocal chai_type  # Refers to the variable in the outer function (update_order)
        chai_type = "Kesar"  # Updates the value of chai_type in the enclosing scope

    kitchen()  # Call inner function to update the value
    print("After kitchen update:", chai_type)  # This will print: After kitchen update: Kesar

# Call the function
update_order()
