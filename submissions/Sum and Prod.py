'''-----------------------------------------------------------------------

Problem Title: Sum and Prod
Problem Link: /challenges/np-sum-and-prod
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
add = np.sum(a, axis = 0)
prod = np.prod(add)
print (prod)
