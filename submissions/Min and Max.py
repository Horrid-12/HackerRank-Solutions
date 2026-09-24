'''-----------------------------------------------------------------------

Problem Title: Min and Max
Problem Link: /challenges/np-min-and-max
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n, m = map(int, input().split())
A = np.array([input().split() for _ in range(n)], int)
minimum = np.min(A, axis = 1)
maximum = np.max(minimum)
print (maximum)
