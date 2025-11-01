#set
#{expression for item in iterable if condition}



fav_chai =[
    "Masala chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi chai"
]

Unique_chai = {chai for chai in fav_chai }
print(Unique_chai)

recipes = {
   "Masala chai ":  ["ginger", "cardamom", "clove"],
   "elaichi chai ":  [ "carda", "cl"],
   "Maaa chai ":  ["ginger", "black cardamom", "clove"],
}

uniq_chai = {spice for ingredient in recipes.values() for spice in ingredient }

print(uniq_chai)



# 🏁 Summary Table
# Concept	                                          Description                              	                              Example
# Set	                                          Collection of unique, unordered items                  	                 {1, 2, 3}
# Set Comprehension  	                          Creates a set using a loop and optional condition	                         {x for x in data if x > 5}
# Duplicate removal	                            Automatically handled                                    	                 'Green Tea' appears once
# Nested comprehension 	                        Loops inside loops	                                                          {spice for lst in recipes.values() for spice in lst}