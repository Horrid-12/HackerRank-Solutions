'''-----------------------------------------------------------------------

Problem Title: Tuples 
Problem Link: /challenges/python-tuples
Author: 1272261921_s
Language: python

-----------------------------------------------------------------------'''


if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    t = tuple(integer_list)
    
    print(hash(t))
