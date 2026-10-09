'''-----------------------------------------------------------------------

Problem Title: Dot and Cross
Problem Link: /challenges/np-dot-and-cross
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT


import numpy as np

n = int(input())

A = np.array([input().split() for i in range(n)], int)
B = np.array([input().split() for i in range(n)], int)

print(np.dot(A, B))
