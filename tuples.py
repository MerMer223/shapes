address = (36,"mansion","boulevard","Canada","F5W3H7")


print(address[1])
door_no, house_name, street_name, country, zip_code = address

print(street_name)

# tuple does not support item assignment address[2] = 6

num = 1,2

print(num[1])

print(len(num))

print(num * 2)

num1 = 3,4

print(num1 + num)

print(address [1:3])
print(address [3:5])


if "mansion" in address:
    print("true")
else:
    print("false")


for information in address:
    print(information)




num2 = 0,[1,2],3

num2 [1][0] = 5





