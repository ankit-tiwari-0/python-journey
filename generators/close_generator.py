def imported_chai():
    yield "Matcha"
    yield "Oolong"


def local_chai():
    yield "Masala chai"
    yield "Ginger chai"


def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)    


# Create the generator object
# menu = full_menu()

# # Manually get the next item each time
# print(next(menu))  # 1st item
# print(next(menu))  # 2nd item
# print(next(menu))  # 3rd item
# print(next(menu))  # 4th item

def chai_stall():
    try:
        while True:
            order = yield "waiting for chai order"
    except:
        print("stall closed, no more chai")


stall = chai_stall()
print(next(stall))
stall.close()