'''
Copy a Dictionary
'''

# 1. using copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
myDict = thisdict.copy()
print(myDict)

# 2. using dict() constructor

dictCopy = dict(thisdict)
print(dictCopy)