#!/usr/bin/python3
print("{}".format("\n".join([
    "{} = 0x{:x}".format(i, i) for i in range(0, 99)
])))
