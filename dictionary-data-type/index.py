'''
Dictionary 
'''
thisDict = {
    "brand": "Ha",
    "model": "No",
    "year": 1999
}
print(thisDict)

# 1. Dictionary items
print(thisDict["year"])#1999

# 2. Duplicates not allowed
thisdict01 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict01)

# 3. Dictionary length
print(len(thisDict)) # 3

# 4. type
thisdict02 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict02))# <class 'dict'>

# 5. dict() constructor
constructorDict = dict(name = "John", age = 36, country = "Norway")
print(constructorDict)