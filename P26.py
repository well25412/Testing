def spam():
    return f"Hello"

def greet(name):
    return f"hello {name}"

def add(a,b):
    return a+b

def demo(func):
    def delay(*args,**kwargs):
        result = func(*args,**kwargs)
        return result
    return delay

d= demo(add)
print(d(10,20))
d=demo(spam)
print(d())
d= demo(greet)
print(d('Luna'))

    

    
    
    
