info={
     "key": "value",
     "name": "aqsa",
     "learning": "python",
     "age": 21,
     "height": 5.2,
     "tup": (1,2,3),
     "lst": [1,2,3]
     }
print(info)
print(type(info))
print(info["name"])

info["name"]="ayesha"
info["surname"]="zafar"
print(info)

dict={}
dict["goat"]="cristiano ronaldo"
print(dict)


student={
    "name":"aqsa",
    "subjects":{
        "phy":90,
        "chem":80,
        "maths":70
    }
}
print(student["subjects"]["phy"])

print(info.keys())
print(len(list(info.values())))
print(len(info))

print(list(info.items()))
pairs=(list(info.items()))
print(pairs[0])

print(info.get("name"))

info.update({"city" : "kamir"})
print(info)

sets={1,2,3,4,5,6,7,8,9,10,11,12}
print(sets)
print(type(sets))
print(len(sets))

collection=set()
print(type(collection))

collection.add(10)
collection.add(20)

collection.pop()
collection.clear()
print(collection)
set2={1,13,14,5,7}
print(sets.union(set2))


print(sets.intersection(set2))