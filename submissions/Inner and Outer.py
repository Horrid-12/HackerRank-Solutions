'''-----------------------------------------------------------------------

Problem Title: Inner and Outer
Problem Link: /challenges/np-inner-and-outer
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

A = np.array(input().split(), int)
B = np.array(input().split(), int)

print(np.inner(A, B))
print(np.outer(A, B))
