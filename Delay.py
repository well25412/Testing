def g1():
    print(f'you are calling {g1.__name__} ')

    
g1()
print(g1.__name__)
          

def spam():
    return 'hello world'
result = spam()
print(result)

print(spam)
s= spam
print(s)

def greet(name):
    return f"hello {name} "

def add(a,b):
    return a+b


word = 'Hello'
print(id(spam))
from time import sleep
def delay(func,time_delay,*args,**kwargs):
    sleep(time_delay)
    print(f"You are calling {func.__name__}")
    result = func(*args,**kwargs)
    return result
print(delay(spam,2))
print(delay(greet,2,'Luna'))
print(delay(add,2,10,30))

print(delay(spam,2))
print(delay(greet,2,name ='Beast'))
print(delay(add,2,10,b=50))










