#!/usr/bin/python3
import sys

if (__name__) == ("__main__"):
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 argument.")
    else:
        if num_args == 1:
            print(f"1 argument: ")
        else:
            print("{} argument:".format(num_args))

        for i in range(1, num_args + 1):
            print("{}: {}".format(i, sys.argv[i]))
