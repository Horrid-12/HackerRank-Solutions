'''-----------------------------------------------------------------------

Problem Title: Zeros and Ones
Problem Link: /challenges/np-zeros-and-ones
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

shape = tuple(map(int, input().split()))

print(np.zeros(shape, dtype=int))
print(np.ones(shape, dtype=int))
