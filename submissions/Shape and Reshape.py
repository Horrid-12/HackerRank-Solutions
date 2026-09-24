'''-----------------------------------------------------------------------

Problem Title: Shape and Reshape
Problem Link: /challenges/np-shape-reshape
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np 
arr = np.array(input().split(), int)
arr = arr.reshape(3, 3)
print(arr)
