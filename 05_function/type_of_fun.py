#Type of function
 #    pure vs impure
 #    recusive function
 #     lambda(anonymous fuc)

def pure_chai(cups):
    return cups * 10
print(pure_chai(3))


tota_chai = 0

# not recommended

def impure_chai(cup):
    global tota_chai
    tota_chai += cup
    return tota_chai

print(impure_chai(45))    

# recusive

def pour_chai(n):
    print(n)
    if n== 0:
        return "ALL cups poured"
    return pour_chai(n-1)

print(pour_chai(5))

#lamda

chai_type = ["kkk", "xxx", "xxx", "lll"]

strong = list(filter(lambda chai: chai == "xxx", chai_type))
              #map

print(strong)








# | **Type**                  | **Explanation**                                                                                             | **Example**                  |
# | ------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------- |
# | ✅ **Pure Function**       | - Gives same output for same input<br>- No side effects (doesn’t modify outside things)                     | `pure_chai(cups)`            |
# | ❌ **Impure Function**     | - Changes or depends on global/external state<br>- Can produce different output with same input             | `impure_chai(cup)`           |
# | 🔁 **Recursive Function** | - Calls itself inside the function<br>- Useful for repetitive tasks or breaking problems into smaller parts | `pour_chai(n)`               |
# | ⚡ **Lambda Function**     | - Short, anonymous one-line function<br>- Often used with `map()`, `filter()`, `sort()`                     | `lambda chai: chai == "xxx"` |
