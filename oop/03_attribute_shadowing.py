class Chai:
    temperature = "hot"
    strenght = "strong"


cutting = Chai()
print(cutting.temperature)


cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing", cutting.temperature)
print("cup size is", cutting.cup)
print("Direct look into the class", Chai.temperature)

del cutting.temperature
del cutting. cup 
print(cutting.temperature)
print(cutting.cup)
 
#  if some how the reference of this variable or the object attribute is no longer available
#  then it fall back to the value of the attribute which was defined in the CHAI itself


#17 the default fallback there and that exactly the shadowing there is nothing to fall back the shadow will fall onto the class itself, it it doean't exist in the class there is no fallback for it