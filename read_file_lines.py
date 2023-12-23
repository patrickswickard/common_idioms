"""Demo read lines from file"""
file = 'pinafore.txt'
with open(file,'r',encoding='utf-8') as myinfile:
  lines = myinfile.read().splitlines()
  for thisline in lines:
    print(thisline)
