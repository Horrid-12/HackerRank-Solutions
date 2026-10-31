'''-----------------------------------------------------------------------

Problem Title: Validating phone numbers
Problem Link: /challenges/validating-the-phone-number
Author: Horrid-12
Language: python3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for _ in range(n):
    number = input()
    if re.fullmatch(r'[789]\d{9}', number):
        print("YES")
    else:
        print("NO")
