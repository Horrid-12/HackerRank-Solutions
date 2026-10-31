'''-----------------------------------------------------------------------

Problem Title: Validating and Parsing Email Addresses
Problem Link: /challenges/validating-named-email-addresses
Author: Horrid-12
Language: python3

-----------------------------------------------------------------------'''


import re
import email.utils

n = int(input())

pattern = r'[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}'

for _ in range(n):
    line = input()
    name, address = email.utils.parseaddr(line)

    if re.fullmatch(pattern, address):
        print(email.utils.formataddr((name, address)))
