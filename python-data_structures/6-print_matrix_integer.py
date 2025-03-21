#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for number in range(len(row)):
            if number != 0:
                print(" ", end="")
            print("{:d}".format(row[number]), end="")
        print()
