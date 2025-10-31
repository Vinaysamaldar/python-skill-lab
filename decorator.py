def log_sum(func):
    print("Inside of log_sum decorator..")
    def wrapper(n1,n2):
        result = func(n1,n2)




        
@log_sum


def log(func):
    print("Inside of log decorator..")
    def test(name):
        print("Before calling hello func..")
        func(name)
        print("After calling hello func")
    return test

@log
def hello(name):
    print(f"hello,{name}")

hello("ganesh")            