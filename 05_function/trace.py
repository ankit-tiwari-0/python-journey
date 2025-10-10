def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

orders = [100, 150, 200, 300]


for pric in orders:
    final_amount = add_vat(pric, 20) 
    print(f"original:{pric}, final with VAT: {final_amount}")











# Define a function named 'add_vat' that takes two arguments:
# 'price' (the original price of the product) and 'vat_rate' (percentage of VAT to add)
def add_vat(price, vat_rate):
    # This line calculates the final price including VAT.
    # It multiplies the price by (100 + vat_rate) / 100 to add the VAT.
    # Example: if price = 100 and vat_rate = 30 → 100 * (120/100) = 130
    return price * (100 + vat_rate) / 100

# A list of order prices without VAT
orders = [100, 150, 200, 300]

# Loop through each price in the orders list
for pric in orders:
    # Call the add_vat function with the price and a 30% VAT rate
    # Store the result in 'final_amount'
    final_amount = add_vat(pric, 30)

    # Print the original price and the final amount after adding VAT
    print(f"original: {pric}, final with VAT: {final_amount}")
