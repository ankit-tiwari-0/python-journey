# Tuple ----> ()

masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1},{spice2},{spice3}")

ginger_ratio, cadramom_ratio = 2,1

print(f"Ratio is G : {ginger_ratio} and c : {cadramom_ratio}")
ginger_ratio,cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"Ratio is G : {ginger_ratio} and c : {cadramom_ratio}")

#membership

print(f"is ginger in masala spice ? {'ginger' in masala_spices}")
print(f"is ginger in masala spice ? {'cardamom' in masala_spices}")

