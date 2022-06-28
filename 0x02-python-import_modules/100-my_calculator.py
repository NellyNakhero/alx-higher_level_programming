#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    nargs = len(sys.argv) - 1
    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        num1 = int(sys.argv[1])
        symbl = sys.argv[2]
        num2 = int(sys.argv[3])

        if "+".__eq__(symbl):
            print(f"{num1} {symbl} {num2} = {add(num1, num2)}")
        elif "-".__eq__(symbl):
            print(f"{num1} {symbl} {num2} = {sub(num1, num2)}")
        elif "*".__eq__(symbl):
            print(f"{num1} {symbl} {num2} = {mul(num1, num2)}")
        elif "/".__eq__(symbl):
            print(f"{num1} {symbl} {num2} = {div(num1, num2)}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
