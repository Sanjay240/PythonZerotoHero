# key value pairs

d1 ={}
# print(type(d1))

d2 ={"Harry":"Burger", "Sanjay": "Veg", "Sachin":{"B": "eggs", "L": "proteins", "D":"chicken"}}

print(d2["Sanjay"])

d2["Golu"] = "Meat"
print(d2)

del d2["Harry"]
 
print(d2)

# don't use the direct assognment operator insetead use the copy function, update()
# d3 = d2 instead use d3 = d2.copy()

