#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1

    if num_args == 0:
        print(f"{num_args} arguments.")
    elif num_args == 1:
        print(f"{num_args} argument:")
    else:
        print(f"{num_args} arguments:")

    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"{i}: {arg}")
