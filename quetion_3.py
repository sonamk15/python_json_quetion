import json 
w={    "name": "David",
     "class":"I",
     "age": 6  
 }

a=open("quetion_3.json","w")
b=json.dump(w,a)

a.close()