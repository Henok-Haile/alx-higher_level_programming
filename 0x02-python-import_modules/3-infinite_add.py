#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_arg = len(sys.argv) - 1
    total = 0

    for i in range(num_arg):
        if num_arg == 0:
            print("{}".format(int(num_arg)))
        total = total + int(sys.argv[i + 1])
    print("{}".format(total))
