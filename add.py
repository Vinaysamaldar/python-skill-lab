# def sum(*args):
#     print("args is;",args)
#     print("Type of args is:",type(args))
#     count = 0
#     for num in range:
#         count += num
#     return count

# res = sum(1,2,3,4,5,6,7,8,9,10)
# print("Sum is:",res)

def test(**kwargs):
    print("kwargs is:", kwargs)
    print("Type of kwargs is:", type(kwargs))
    print(f"name is: {kwargs['name']}")
