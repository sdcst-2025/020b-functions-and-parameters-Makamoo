myList = []
"""
for i in range(20):
    x = input('enter something')
    #myList.append(x)
    myList.insert(0,x)

print(myList)

"""
x = int(input("hi"))
tiger = []
for i in range(x):
    i = i+1
    R = x/i
    T = int(R)
    S = float(T)
    if R == S:
        tiger.append(i)
print(tiger)