"""Demonstrate read lines in directory"""
import re
import os

dirlist = os.listdir()
for thisfilename in dirlist:
  filename_base = re.search(r"(.*?)\.txt",thisfilename)
  if filename_base:
    print(filename_base.group(1))
