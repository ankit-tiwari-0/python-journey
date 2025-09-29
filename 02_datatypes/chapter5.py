#list [] ---> array ,this  is mutable
ingre = ["water", "milk","black tea"]
ingre.append("sugar")
print(f"Ingrediants are : {ingre}")
ingre.remove("water")
print(f" New ingrediants are : {ingre}")

spice_option = ["ginger", "cardamom"]
chai_ing = ["water","milk"]
#we use exted to add both

chai_ing.extend(spice_option)
print(f"chai: {chai_ing}")

chai_ing.insert(2, "elachi")
print(f"chai: {chai_ing}")

last_added = chai_ing.pop()
print(f"chai4: {last_added}")
print(f"chai: {chai_ing}")
chai_ing.reverse()
print(f"chai: {chai_ing}")
chai_ing.sort()
print(f"chai: {chai_ing}")

sugar_level = [1,2,3,4,5,6]
print(f"maximum sugar level: {max(sugar_level)}")
print(f"maximum sugar level: {min(sugar_level)}")

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] *5
print(f"String brew:{strong_brew}")


raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CArd")
print(raw_spice_data)

