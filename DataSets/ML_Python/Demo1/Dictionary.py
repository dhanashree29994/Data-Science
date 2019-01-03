#Dictionary: k:v
info = {101 : "Raj", 102: "Sam","Red":"Apple"}
print(type(info))


print(info.get(101))

### get keys

print(info.keys())
print(info.items())
print(info.values())


print("Apple" in info.values())

for k,v in info.items():
    print(k, v)
