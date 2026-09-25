'''-----------------------------------------------------------------------

Problem Title: Floor, Ceil and Rint
Problem Link: /challenges/floor-ceil-and-rint
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
np.set_printoptions(legacy = '1.13')
a = np.array(input().split(), float)
floor = np.floor(a)
ceil = np.ceil(a)
rint = np.rint(a)
print (floor)
print (ceil)
print (rint)
