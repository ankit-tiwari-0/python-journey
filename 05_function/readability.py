# Define a function named 'caalculation_bill' that takes two parameters: chai (quantity) and price (per item)
def caalculation_bill(chai, price):
    # The 'return' statement sends back the result of chai * price to where the function was called
    return chai * price

# Call the function with 5 items and price 20. The returned value is stored in 'dd'
dd = caalculation_bill(5, 20)

# Print the result of the first bill
print(dd)

# Call the function again directly in the print statement (5 items at price 10)
print("second order", caalculation_bill(5, 10))
