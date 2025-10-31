numbers = [1,2,3,4,5]
res = []

for n in numbers:
    square = n ** 2
    res.append(square)
print(res)    

#using list comprehesion
square = [n ** 2 for n in numbers]
print(square)