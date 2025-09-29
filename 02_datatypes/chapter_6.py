#set by default is known  for uniqueness only

# Set Intersection: &
# The intersection of two sets (A ∩ B) includes only the elements that are present in both sets.
# For example, if Set A = {1, 2, 3} and Set B = {2, 3, 4}, then the intersection A ∩ B = {2, 3}.

# Set Union: |
# The union of two sets (A ∪ B) includes all unique elements from both sets.
# Using the earlier example, the union A ∪ B = {1, 2, 3, 4}

essential_spices = {"cardamom", "ginger", "cinamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices

print(f"unioun : {all_spices}")

common_spices = essential_spices & optional_spices
print(f"intersection : {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"only in essential spices : {only_in_essential}")

print(f"Is 'cloves' in opt spices? : {'cloves' in optional_spices}")