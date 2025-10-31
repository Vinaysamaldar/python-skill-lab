def div(n1,n2):
    return n1 // n2
try:
    res = div(10,0)
    print(f"result is {res}")
    
except ZeroDivisionError as e :
    print("You cannot divisible by zero..")

