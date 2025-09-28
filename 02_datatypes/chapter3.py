chai_type = "ginger chai"
customer_name = "Noorin"

print(f"order for {customer_name} : {chai_type} please")


chai_description = "Aromatic and Bold more"
print(f"First word word: {chai_description[:7]}")
print(f"last word word: {chai_description[12:]}")
print(f"last word word: {chai_description[::-1]}")

label_text = "ankit is ugly"
ecoded_label = label_text.encode("utf-16")
print(f"Non Encoded label: {label_text}")
print(f"Non Encoded label: {ecoded_label}")

decoded_label = ecoded_label.decode("utf-16")
print(f"Non decoded label: {decoded_label}")


