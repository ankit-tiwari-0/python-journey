# Global variable defined at the top level
chai_type = "plain"  # This is in the global scope

def front_desk():
    # Nested function inside front_desk
    def kitchen():
        global chai_type  # Refers to the global variable 'chai_type'
        chai_type = "irnai"  # Modifies the global variable, not a local one

    kitchen()  # Call the inner function to change the global variable

# Call the outer function, which calls the inner function
front_desk()

# After function execution, the global 'chai_type' is updated
print("final global chai:", chai_type)  # Output will be: final global chai: irnai
























# 🧠 Key Concepts:
# Keyword	What it Affects	Scope Affected
# local	Variables declared inside a function	That function only
# nonlocal	Variables from the enclosing function	Immediate outer function
# global	Variables declared in the global scope	Top-level of the script

# global chai_type means: "Don't create a local chai_type; instead, use the one defined outside, at the module (global) level."