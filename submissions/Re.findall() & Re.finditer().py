'''-----------------------------------------------------------------------

Problem Title: Re.findall() & Re.finditer()
Problem Link: /challenges/re-findall-re-finditer
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
s = input()
m = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])[aeiou]{2,}(?=[qwrtypsdfghjklzxcvbnm])', s, re.I)

if m : 
  print(*m, sep = "\n")
else: 
  print(-1)
