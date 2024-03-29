names = ["Jack", "George", "ali", "Anie"]
print(names, len(names))
names.insert(0, "Victor")
print(names)
names[3:] = ["freddy", "Marie"]
print(names, len(names))

#['Jack', 'George']
print(names[1:-2])
print(names[1:3])
print(names[-4:-2])
print(names[-4:3])

print(names)

names.append("Joan")
names.extend(["Doris", "Mimi", "Anie"])
print(names)
print(names.pop())
print(names.pop(2))
print(names.remove("Joan"))
print(names)

