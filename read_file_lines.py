file = 'pinafore.txt'
with open(file) as fd:
  lines = fd.read().splitlines()
  for thisline in lines:
    print(thisline)

