Items = ["Basketball","Pizza","Shoes","Snacks"]

print(Items[0])
print(Items[-3])
print(Items[1:3])

Items.append("Net")

print(Items)

Items.pop(3)

print(Items)

Items.remove("Pizza")

print(Items)

Items [1] = "Giftcard"

print(Items)

if "Basketball" in Items:
    print("I would like to buy this")
else:
    print("What else do you have")


for item in Items:
    print(item)

length = len(Items)

for i in range(length):
    print(Items[i])


Names = ["bob","tom","jerry","amanda","MerMer"]

print("what is your username")
name = input()

if name in Names:
    print("Access granted")
else:
    print("Access denied")

