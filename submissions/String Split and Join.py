'''-----------------------------------------------------------------------

Problem Title: String Split and Join
Problem Link: /challenges/python-string-split-and-join
Author: Horrid-12
Language: pypy3

-----------------------------------------------------------------------'''




def split_and_join(line):
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
