import re

file = 'pinafore.txt'
with open(file) as fd:
  lines = fd.read().splitlines()

# find and report
for thisline in lines:
  branch = re.search(r"Queen's\s+(\w+)",thisline)
  if branch:
    print(branch.group(1))


# find and report
for thisline in lines:
  newline = re.sub(r"\W","",thisline)
  print(newline)
