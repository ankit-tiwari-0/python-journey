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