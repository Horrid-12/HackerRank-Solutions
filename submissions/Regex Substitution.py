'''-----------------------------------------------------------------------

Problem Title: Regex Substitution
Problem Link: /challenges/re-sub-regex-substitution
Author: Horrid-12
Language: python3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for _ in range (n) : 
  line = input()
  line = re.sub(r'(?<= )&&(?= )', 'and', line)
  line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
  print(line)
