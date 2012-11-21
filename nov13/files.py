#! /usr/bin/python3

import sys

def fileaslines():
    path   = sys.argv[1]
    # file object as a list of lines 
    f = open(path,'r')
    for line in f:
        fields = line.split(",")
        print(line, end='')
    
    f.close()

def explicitlist():
    path   = sys.argv[1]
    f = open(path,'r')
    lines = f.readlines() # returns a list containing all the lines of data in the file.
    # print(lines)
    for line in lines:
        print(line,end='')
    f.close()

def singleline():
    f = open("grades.csv",'r')
    print(f.readline(),end='')
    f.close()

def filewrite():
    f = open ("temp.txt",'w')
    c = f.write("Hello\n")
    print (c)
    f.close()


# program entrance

# singleline()

explicitlist()

# fileaslines()

# filewrite()
