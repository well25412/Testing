d ={}
d=dict()
print(d)
d=dict({'a':1,'b':2,'c':3})
print(d)
print(d['a'])
#print(d['d'])-- key error
print(d.get('d',0))

print(id(d))
d['B'] ='ugly'
print(d)

for item in d.items():
    print(item)

r={}
m = ['apple','google','microsoft']
for item in m:
    if item in r:
        r[item]+=1
    else:
        r[item]=1
print(r)

dum =list()
sentence ="hello hello world world welcome to python world"
words = sentence.split()
dum = words.copy()
print(dum)

t = (1,)
print(t)
t =('eat','sleeping','watching')
print(t)
print(t[-1])
print(t[::2])
print(t[1:3])
#t[3]= 'listening'
print(t) 
a =list()
print(a)
a = list(['men','women','kid'])
print(a)

print('steves',2019)
print('welcome to python"s world')






