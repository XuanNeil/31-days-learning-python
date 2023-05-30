'''
Add items
'''

# 1. Adding items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# 2. using update() method
thisdict.update({"id": 1})
print(thisdict)