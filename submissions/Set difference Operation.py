'''-----------------------------------------------------------------------

Problem Title: Set .difference() Operation
Problem Link: /challenges/py-set-difference-operation
Author: Horrid-12
Language: python3

-----------------------------------------------------------------------'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(map(int, input().split()))

m = int(input())
B = set(map(int, input().split()))

common = A.difference(B)

print(len(common))
