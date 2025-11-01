def add(a,b):
    return a+b 

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b ==0:
        raise ValueError ("cannot divide by zero ")
    return a/b
def  test_div():
    assert div(4,2) == 2