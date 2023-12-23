"""Demonstrate boolean masking in np"""
import numpy as np

a = np.array([1, 4, 9, 16, 25, 36, 49])
b = [1,4,9,16,25,36,49]


print(a)
print(b)
print(a[a >= 25])
# won't work not np array
#print(b[b >= 25])

print(a >= 25)
