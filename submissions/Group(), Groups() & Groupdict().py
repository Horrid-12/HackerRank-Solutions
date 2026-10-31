'''-----------------------------------------------------------------------

Problem Title: Group(), Groups() & Groupdict()
Problem Link: /challenges/re-group-groups
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()
m = re.search(r"([a-zA-Z0-9])\1", s)

if m : 
  print(m.group(1))
else :
  print(-1)
