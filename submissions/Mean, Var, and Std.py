'''-----------------------------------------------------------------------

Problem Title: Mean, Var, and Std
Problem Link: /challenges/np-mean-var-and-std
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''


import numpy as np 
n, m = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)])
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(round(np.std(arr), 11))
