import json

json_file = open('sample.json', 'r')
json_hash = json.load(json_file)
json_file.close()

print(json_hash)

