'''-----------------------------------------------------------------------

Problem Title: Set .discard(), .remove() & .pop()
Problem Link: /challenges/py-set-discard-remove-pop
Author: Horrid-12
Language: python3

-----------------------------------------------------------------------'''


n = int(input())
s = set(map(int, input().split()))
commands = int(input())

for _ in range(commands):
    command = input().split()

    if command[0] == "pop":
        s.pop()

    elif command[0] == "remove":
        s.remove(int(command[1]))

    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))
