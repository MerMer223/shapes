import random

marks = []
count = 20
while count >=0:
    x = random.randint(0,100)
    marks.append(x)
    count = count -1
print(marks)

low = []
mid = []
high = []

for mark in marks:
    if mark <=30:
        low.append(mark)
    elif mark >=31 and  mark <=69:
        mid.append(mark)
    elif mark >= 70:
        high.append(mark)

print(low)
print(mid)
print(high)
