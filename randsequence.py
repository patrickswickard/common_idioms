import random

a = list(range(1,251))
b = list(range(1,251))
c = list(range(1,251))

random.shuffle(a)
print(a)
random.shuffle(b)
print(b)
random.shuffle(c)
print(c)

def dosetstuff():
  a = list(range(1,251))
  b = list(range(1,251))
  c = list(range(1,251))

  random.shuffle(a)
#  print(a)
  random.shuffle(b)
#  print(b)
  random.shuffle(c)
#  print(c)
  bigset_a = set()
  bigset_b = set()
  bigset_c = set()
  for i in range(0,249):
#    print(a[i],a[i+1])
    bigset_a.add((a[i],a[i+1]))
  for i in range(0,249):
#    print(b[i],b[i+1])
    bigset_b.add((b[i],b[i+1]))
  for i in range(0,249):
#    print(c[i],c[i+1])
    bigset_c.add((c[i],c[i+1]))
#  print(bigset_a)
#  print(bigset_b)
#  print(bigset_c)
  return[bigset_a,bigset_b,bigset_c]

stop = False
count = 0
while not stop:
  count = count + 1
  print('Try number ' + str(count))
  setlist = dosetstuff()
  bigset_a = setlist[0]
  bigset_b = setlist[1]
  bigset_c = setlist[2]
  if not bigset_a.intersection(bigset_b) and not bigset_b.intersection(bigset_c) and not bigset_a.intersection(bigset_c):
#  if not bigset_a.intersection(bigset_b) and bigset_b.intersection(bigset_c) and bigset_a.intersection(bigset_c):
    print("first_okay")
    print(bigset_b.intersection(bigset_c))
    print(bigset_a.intersection(bigset_c))
    stop = True
  else:
    print(bigset_a.intersection(bigset_b))
    print("try again...")
    print('my friend')
    stop = False


for i in range(1,251):
  source = i
  for setmember in bigset_a:
    if setmember[0] == i:
      destination_1 = setmember[1]
  for setmember in bigset_b:
    if setmember[0] == i:
      destination_2 = setmember[1]
  for setmember in bigset_c:
    if setmember[0] == i:
      destination_3 = setmember[1]
  mylist = [source,destination_1,destination_2,destination_3]
  print(mylist)
