import enum


arr = [0,2,4,6,8,10]

for x in arr:
    print(x)

print("------------")

arrLen = len(arr)
for i in range(arrLen):
    print(i)

print("------------")

for i, x in enumerate(arr):
    print(i, x)