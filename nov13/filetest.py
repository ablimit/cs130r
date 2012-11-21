#! /usr/bin/python3

import sys
import os


path = "/home/cs130r00/cs130r"
val = os.path.isfile(path)
print(val)

val = os.path.isdir(path)
print(val)
