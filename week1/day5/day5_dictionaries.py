# Dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates


capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow",
            "Algeria": "Alger"}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA"))
print(capitals.get("Japan"))

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()
# capitals.clear()

keys = capitals.keys()

for key in capitals.keys():
    print(key)

values = capitals.values()

for value in capitals.values():
    print(value)

items = capitals.items()

for key, value in capitals.items():
    print(f"{key}: {value}")