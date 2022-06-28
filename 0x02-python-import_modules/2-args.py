#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    num = int(len(sys.argv)) - 1
    if num == 1:
        print(f"{num} argument:")
    else:
        print(f"{num} arguments:")

    if num > 0:
        for i in range(num + 1):
            if i == 0:
                continue
            print(f"{i}: {sys.argv[i]}")
