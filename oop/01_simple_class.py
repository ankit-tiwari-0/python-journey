class Cartoon:
    pass

# print(type(Cartoon))

# it saying type class but it alwaays object, internally it is an object

class cartoontype:
    pass

print(type(Cartoon))

motu = Cartoon()
print(type(motu))
print(type(motu) is Cartoon) 
print(type(motu) is cartoontype)