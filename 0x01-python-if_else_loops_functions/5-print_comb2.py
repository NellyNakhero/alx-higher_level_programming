#!/usr/bin/python3
for i in range(0, 100):
    if len(repr(i)) != 2:
        print(f"{i:02}", end=', ')
    print(i, end=', ')
