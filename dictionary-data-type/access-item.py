'''
Access Items
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

# 1. get() method
y = thisdict.get('model')
print(y)

# 2. get keys
getKey = thisdict.keys()
print(getKey) # before the change -> dict_keys(['brand', 'model', 'year'])

thisdict["color"] = "blue"
print(getKey) # after the change -> dict_keys(['brand', 'model', 'year', 'color'])

# 3. get values
values = thisdict.values()
print(values)  # before the change -> dict_values(['Ford', 'Mustang', 1964, 'blue'])

thisdict["year"] = 2000
print(values) # after the change -> dict_values(['Ford', 'Mustang', 2000, 'blue'])

# 4. get items
items = thisdict.items()
print(items) # before the change -> dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2000), ('color', 'blue')])
thisdict["color"] = "red"
print(items) # after the change -> dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2000), ('color', 'red')])

# 5. check if key exists

if "color" in thisdict:
    print("Yess!!!")
