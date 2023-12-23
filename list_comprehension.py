"""Reminder of list comprehensions"""
# clunky version:

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

newlist = []

for x in fruits:
  if 'a' in x:
    newlist.append(x)

print(newlist)

# smooth version
newlist2 = [x for x in fruits if 'a' in x]

print(newlist2)

# non-picky version
newlist3 = [x + x for x in fruits]
print(newlist3)
