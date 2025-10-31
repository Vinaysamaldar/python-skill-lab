def first():
    print("first...")
    
def second():
    print("second...")
    first()
    print("After first function call..")

def third():
    print("third...")
    second()
    print("After second function call..")


def fourth():
    print("fourth...")
    third()
    print("After third function call..")


fourth()    
print("After fourth function call..")

