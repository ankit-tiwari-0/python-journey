# Scopes and Name Resolution in Python
# LEGB Rule:
# L - Local: Names assigned inside a function (local to that function)
# E - Enclosing: Names in the local scope of any and all enclosing functions (used in nested functions)
# G - Global: Names assigned at the top-level of a script/module
# B - Built-in: Names that are preassigned in the built-in names module (like print, len, etc.)

def serve_chai():
    chai_type = "Masala " # local scope
    print(f"INside fun {chai_type}")


chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}")


def chai_counter():
    chai_order = "lemon" #enclosing

    def print_order():
        chai_order = "Ginger"
        print("Inner:", chai_order)
    print_order()    
    print("Outer:", chai_order)    

chai_order = "tulsi" # globa;
chai_counter()
print("global:", chai_order)    



######################################################################

# ************explasion ********************

# Function demonstrating Local Scope
def serve_chai():
    chai_type = "Masala"  # 'chai_type' here is local to this function
    print(f"Inside function: {chai_type}")  # This will print "Masala"

# Global variable
chai_type = "Lemon"  # This is in the global scope

# Calling the function
serve_chai()  # This uses the local 'chai_type' from inside the function

# Outside the function, global variable is used
print(f"Outside function: {chai_type}")  # This will print "Lemon"


# Function demonstrating Enclosing Scope in nested functions
def chai_counter():
    chai_order = "lemon"  # Enclosing scope variable

    def print_order():
        chai_order = "Ginger"  # Local to this inner function
        print("Inner:", chai_order)  # Prints "Ginger"

    print_order()  # Calls inner function
    print("Outer:", chai_order)  # Prints the enclosing variable, "lemon"

# Global variable with same name
chai_order = "tulsi"  # Global scope

# Calling the outer function
chai_counter()  # Demonstrates how enclosing and local scopes work

# Printing global variable value
print("global:", chai_order)  # Prints "tulsi"
