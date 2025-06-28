mylist = [
  'Elmer Fudd',
  'Wile E Coyote',
  'Daffy Duck',
  'Yosemite Sam',
  'Pol Pot',
  'Marvin the Martian',
]

with open('out.txt', 'w') as f:
  print(mylist, file=f)
