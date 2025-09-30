#dictionary

chai_order = dict(type="Masala chai", size="Large", sugar=3)
print(f"chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"recipe base: {chai_recipe['base']}")
print(f"recipe:{ chai_recipe}")
del chai_recipe["liquid"]
print(f"recipe : {chai_recipe}")


print(f"Is sugar in the order {'type' in chai_order}")

chai_order = {"typer": "Ginger chai", "size": "Mediam", "sugar": 1}

print(f"order detail (key): {chai_order.keys()}")
print(f"order detail (key): {chai_order.values()}")

last_item = chai_order.popitem()
print(f"Remove last item: {last_item}")

extra_spices = {"cardamom": "crushed","ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"extra_spice {chai_recipe}")

customer_note = chai_order.get("NOte", "NO NOTE")
print("customer_note is", customer_note)