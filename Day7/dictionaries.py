thisdict = {
    "name" : "Peter",
    "age" : 22,
    "place" : "Delhi",
    "citizenship" : True
}
print(thisdict)
x = thisdict["age"]
y = thisdict.get("name")
print(y)
print(x)
thisdict["language"] = "Hindi"
keys_in = thisdict.keys()
print(keys_in)
v = thisdict.values()
print(v)
print(thisdict)