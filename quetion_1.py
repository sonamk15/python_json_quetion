import json
a=open("quetion_1.json")
print(a)
b=json.load(a)
print(b)
print(type(a))
print(type(b))
a.close()