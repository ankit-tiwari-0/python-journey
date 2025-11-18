# ✅ Use of This Decorator

# Your decorator is used to add extra behavior around a function without changing the function itself.

# In this case, it:

# Prints a message before the function runs.

# Runs the actual function (greet).

# Prints a message after the function runs.

# This is useful when you want to add something common to many functions, such as:

# Logging

# Printing start/end messages

# Timing how long a function takes

# Checking permissions

# Validating data

# Running setup and cleanup code

# And because you used @wraps, the function still keeps its original identity (its name, docs, etc.).

from functools import wraps

def My_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function run")
        func()
        print("After function run")
    return wrapper

@My_decorator
def greet():
    print("Hello from decorator class from chaicode")

greet()
print(greet.__name__)



# Real-Life Analogy for Decorators

# Imagine you are going to a restaurant.

# 🍽️ The main thing you want:

# Your food — this is your original function.

# 👨‍🍳 But before and after the food is served:

# The waiter does extra tasks you didn’t ask for:

# Before serving food:
# The waiter sets the table — plates, napkins, spoons.

# After you finish eating:
# The waiter clears the table.

# These are extra steps added around your main action (eating), without changing what the food actually is.

# 🧠 How this relates to decorators

# Your function → the food

# Decorator → the waiter

# Extra actions (before & after) → setting the table + cleaning up

# Food stays the same → your function’s core behavior doesn’t change

# Waiter adds behavior around it → decorator adds extra code around your function

# ✔️ In your code

# Your decorator prints:

# “Before function run” → waiter setting table

# runs your greet function → serving and eating food

# “After function run” → waiter cleaning tabl