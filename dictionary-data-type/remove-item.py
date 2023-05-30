'''
Remove items
'''

# 1. using pop()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("year")
print(thisdict)

# 2. using popitem()
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red"
}
car.popitem()
print(car)

# 3. using del()

thisdict01 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict01["brand"]
print(thisdict01)

# 4. using clear()
thisdict02 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict02.clear()
print(thisdict02)# {}