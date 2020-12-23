import json
a={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
# b=json.dumps(a)
# print(b)
m=input("enter the item :")
g=int(input("how many item you want :"))
r=a["shopping_list"][m]
remo=int(r)-g
# print(remo)
a["shopping_list"][m]=remo
print(a)
b=json.dumps(a)
print(b)


