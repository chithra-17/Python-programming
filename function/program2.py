#use result in another function

def add(a,b):
    return a+b

def square(n):
    return n*n

value = square(add(2,4)) 

print(value)