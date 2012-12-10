#! /usr/bin/python3

import sys


if len(sys.argv) <2:
    print ("Error: Missing param.")
    print("Usage: python3 lookup.py [grade.csv]")
    sys.exit()


f = open(sys.argv[1], 'r')
grades = {}

for line in f:
    sp = line.strip().split(',')
    name = sp[0]
    grade = int(sp[1])
    grades[name] = grade

f.close()


def students(x):
    """Returns a list of student names who got a grade of x
    Input: x , type int 
    Output: student_list, list """

    student_list = []
    for key in grades:
        if grades[key] == x:
            student_list.append(key)
    return student_list

print(students(90))
print(students(89))
print(students(93))
print(students(99))
