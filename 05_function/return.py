#return

def make_chai():
    return "here is your chai"

print(make_chai())


def make_chai():
    return "here is your chai 2"

return_value = make_chai()

print(return_value)


def make_chai1():
    # return "here is your chai"
    print("NOw u get none outpute")


print(make_chai1())

def idle_chaiwala():
    pass
print(idle_chaiwala()) #we get none


def sold_cup():
    return 1000

totaal = sold_cup()
print(totaal)

def chai_status(cups_left):
    if cups_left ==0:
        return "soorry, chai is over"
    return "chai is ready"
    print("chai")  #early from function
print(chai_status(0))
print(chai_status(5))

def chai_report():
    return 100, 20 #sold, reamaining

sold, reamaining = chai_report()
print("sollld: ", sold)
print("reamaining: ", reamaining)


# for 3 value
def chai_report():
    return 100, 20, 10 #sold, reamaining

sold, reamaining, _ = chai_report()
print("sollld: ", sold)
print("reamaining: ", reamaining)

# NOthin -> implicitly return None
# one Value
# multiple Value
# early from a function




















# cenario	What it Does
# No return	Function gives None by default
# One return value	Sends back a single value (string, number, etc.)
# Multiple return values	Returns a tuple (can be unpacked into variables)
# return ends function	Code after return does not run
# pass in function	Function does nothing, used as a placeholder
# Function not called	Nothing happens unless the function is called
# Returned value stored	You can store the returned value in a variable
# print() inside function	Prints something but does not return anything
# Function with conditions	Can return different things based on logic/conditions
# Underscore _ in unpacking	Used to ignore values you don’t need from return