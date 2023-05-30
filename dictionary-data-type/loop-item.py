'''
Loop dictionary
'''

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red"
}
for item in car:
    print(item) # return key

for item in car:
    print(car[item])# return value

for item in car.values():
    print(item)# return value

for item in car.keys():
    print(item) # return key

for x, y in car.items():
    print(x, y)# return x(key) y(value)

