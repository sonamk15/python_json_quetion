import json
n={
    "4": 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    }
a=[]
b=[]
for x in n:
    a.append(x)
    b.append(n[x])
i=0
n={}
while i<len(b):
    j=0
    while j<len(b):
        if b[i]<b[j]:
            b[i],b[j]=b[j],b[i]
            a[i],a[j]=a[j],a[i]  
        j=j+1
    i=i+1
i=0
n={}
while i<len(b):
    n[a[i]]=b[i]
    i=i+1
h=json.dumps(n)
print(h)
print(type(h))
print(type(n))