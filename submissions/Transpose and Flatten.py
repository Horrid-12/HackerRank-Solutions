'''-----------------------------------------------------------------------

Problem Title: Transpose and Flatten
Problem Link: /challenges/np-transpose-and-flatten
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np 
n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], int)
t = np.transpose(arr)
print (t)
z = arr.flatten()
print(z)
