countries = {
    "Egypt":"Cairo",
    "Canada":"Ottawa",
    "China":"Beijing",
    "United Arab Emirates":"Abu Dhabi"
}

print(countries.keys())
print(countries.values())
print(countries["Egypt"])
print(countries["United Arab Emirates"])
#adding a new key value pair
countries ["United Stated of America"]= "Washington DC"

del(countries["Canada"])
print(countries)
if "China" in countries:
    print("yes")
else:
    print("no")
for key in countries.keys():
    print(key,countries[key])
