import json 
filename = 'quetion_8.txt'
dict1 = {}   
fields =['name', 'designation', 'age', 'salary'] 
with open(filename) as fh:  
    l = 1
    list1 = []  
    for line in fh:  
        description = list( line.strip().split(None, 4)) 
        # print(description)
        list1.append(description) 
    # print(list1)
    d={}
    i=0
    p=1
    s="emp"
    while i<len(list1):
        c={}
        j=0
        while j<len(list1[i]):
            c[fields[j]]=list1[i][j]
            j=j+1
        d[s+str(p)]=c
        p=p+1
        # print(c)
        i=i+1
        
# print(d)    python dictionary
u=json.dumps(d)
print(u) 
# print(u)   json string convert
# print(type(d))
# print(type(u))   
        
        
        


        
