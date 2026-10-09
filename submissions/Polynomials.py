'''-----------------------------------------------------------------------

Problem Title: Polynomials
Problem Link: /challenges/np-polynomials
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT\

import numpy as np

P = list(map(float, input().split()))
x = float(input())

print(np.polyval(P, x))
