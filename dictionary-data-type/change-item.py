'''
Change items
'''

# 1. Change values
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car['year'] = 2023
print(car)

# 2. using update() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2018
}
thisdict.update({"year": 2020})
print(thisdict)
