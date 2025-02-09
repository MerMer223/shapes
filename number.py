numbers = []
sum = 0
def read_file():
    file = open("number.txt","r")
    for number in file:
        numbers.append(number.lstrip("\ufeff"))

read_file()
print(numbers)
for number in numbers:
    number = number.strip()
    sum += int(number)
    
print(sum)