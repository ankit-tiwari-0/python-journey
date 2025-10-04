#ZIP

names = ["ankir", "pookie", "noorin", "ali"]
bill = [45,455,777,555]

for name, ammount, in zip(names,bill):
    print(f"{name} paid ${ammount} ")