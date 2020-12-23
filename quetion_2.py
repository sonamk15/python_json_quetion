import json
a={
    "Name":"Ram", 
     "Class":"IV", 
     "Age":9 
     }
b=json.dumps(a)
print(b)
print(type(a))
print(type(b))
