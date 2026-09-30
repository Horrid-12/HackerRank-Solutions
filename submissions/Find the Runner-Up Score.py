'''-----------------------------------------------------------------------

Problem Title: Find the Runner-Up Score!  
Problem Link: /challenges/find-second-maximum-number-in-a-list
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(set(arr))
arr.sort()

print(arr[-2])
