#!/usr/bin/python3
def uppercase(str):
        print("{}".format("".join([
        chr(ord(char) - 32) if ord('a') <= ord(char) <= ord('z') else char
        for char in str
    ])))
