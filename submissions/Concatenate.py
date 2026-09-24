'''-----------------------------------------------------------------------

Problem Title: Concatenate
Problem Link: /challenges/np-concatenate
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n, m, p = map(int, input().split())

arr1 = np.array([input().split() for _ in range(n)], int)
arr2 = np.array([input().split() for _ in range(m)], int)

result = np.concatenate((arr1, arr2), axis=0)

print(result)
