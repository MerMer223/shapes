num = [1,2,3,4,5,6]
set1 = set(num)
set12 = {7,8,9,10,11,12}

print(num)
print(set1)

set1.add(0)

print(set1)

#set1.remove(7)
set1.discard(7)
print(set1)

if 4 in set1:
    print("True")

for i in set1:
    print(i)

#Set Operations
# 1) Union |
# 2) Intersection &
# 3) Difference -
# 4) Symmetric Difference ^

seta = {1,2,3,7,11,12}
setb = {3,4,6,8,10,14}

print(seta|setb)

print(seta&setb)

print(seta-setb)

print(setb-seta)

print(seta^setb)









