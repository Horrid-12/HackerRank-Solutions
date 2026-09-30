'''-----------------------------------------------------------------------

Problem Title: Tuples 
Problem Link: /challenges/python-tuples
Author: Horrid-12
Language: python

-----------------------------------------------------------------------'''


if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    t = tuple(integer_list)
    
    print(hash(t))
