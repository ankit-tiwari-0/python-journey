def chai_flavor(flavor="masala"):
    """ return the flavor of chai """
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)



def generate_bill(chai=0, samosa=0):
    """
    write documentation
    """
    total = chai*10 + samosa*15
    return total

print(generate_bill(2,2))