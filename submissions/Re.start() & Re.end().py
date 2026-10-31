'''-----------------------------------------------------------------------

Problem Title: Re.start() & Re.end()
Problem Link: /challenges/re-start-re-end
Author: Horrid-12
Language: python3

-----------------------------------------------------------------------'''


import re

s = input()
k = input()

matches = list(re.finditer(r'(?=(' + re.escape(k) + r'))', s))

if matches:
    for m in matches:
        print((m.start(1), m.end(1) - 1))
else:
    print((-1, -1))
