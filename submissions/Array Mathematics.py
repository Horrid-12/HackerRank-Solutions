'''-----------------------------------------------------------------------

Problem Title: Array Mathematics
Problem Link: /challenges/np-array-mathematics
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)
print (a + b)
print (a - b)
print (a * b)
print (a // b)
print (a % b)
print (a ** b)
