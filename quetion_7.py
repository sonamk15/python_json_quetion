import json 
filename = 'data.txt' 
fh=open(filename)
a=[] 
for line in fh:
    description = list( line.strip().split(None, 1)) 
    # print(description) 
    a.append(description) 
# print(a)
i=0
b=[]
c=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][0] not in b:
            if a[i][-1] not in c:   
                b.append(a[i][0])
                c.append(a[i][-1])
        j=j+1
    i=i+1   
print(b)
print(c)
dic={}
i=0
while i<len(b):
    dic[b[i]]=c[i]
    i=i+1
print(dic)
convert=json.dumps(dic)
print(convert)
print(type(dic))
print(type(convert))