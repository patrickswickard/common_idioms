"""Demo to read in json file"""
import json

with open('sample.json','r',encoding='utf-8') as myjsonfile:
  json_hash = json.load(myjsonfile)

print(json_hash)
