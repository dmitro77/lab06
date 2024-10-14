import math

def func(x):
    if (x <= 0):
        print("X має бути додатнім")
        return 0
    y = math.log(3, math.fabs(x + math.exp(x)))
    return y
        
a = input("A: ")
b = input("B: ")
h = input("H: ")

valList1 = list()
    
for i in range(int(a), int(b), int(h)):
    valList1.append(func(i))
    
valList2 = list()
    
i = int(a)
while i < int(b):
    valList2.append(func(i))
    i += int(h)

print("\n")

print("Значення функції за способом 1:")
for y in valList1:
    print(y)

print("\n")

print("Значення функції за способом 2:")
for y in valList2:
    print(y)
    
print("\n")
    
largestIndex = 0
largest = valList1[0]
for i in range(1, len(valList1)):
    if (valList1[i] > largest):
        largestIndex = i
        largest = valList1[i]

smallestIndex = 0
smallest = valList1[0]
for i in range(1, len(valList1)):
    if (valList1[i] < smallest):
        smallestIndex = i
        smallest = valList1[i]


print("Найбільше: ", largestIndex)
print("Найменше: ", smallestIndex)
