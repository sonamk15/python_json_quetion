import json
j='{"a":1,"a":2,"a":4,"b":1,"b":2}'
s=json.loads(j)
print(s)
print(type(j))
print(type(s))