#! /usr/bin/python3

import sys

def stats(grades):
    i = 0 # max grade index 
    j = 0 # min grade index 
    for idx in range(len(grades)):
        if grades[idx] > grades[i]:
            i = idx
        if grades[idx] < grades[j]:
            j = idx
    return (i,j)

def output(grades, index):
    avg = sum(grades)/len(grades)
    index = stats(grades)
    print("Number of students:", len(grades))
    print("Average grade:", avg)
    print("Maximum grade:", grades[index[0]])
    print("Minimum grade:", grades[index[1]])

def extracredit(names, grades, index):
    avg = sum(grades)/len(grades)
    index = stats(grades)
    f = open("res.txt",'w')
    f.write ("Number of students: "+str(len(grades))+"\n")
    f.write("Average grade: "+str(avg)+"\n")
    f.write("Maximum grade student name: "+str(names[index[0]])+"\n")
    f.write("Maximum grade is "+str(grades[index[0]])+"\n")
    f.write("Minimum grade student name: "+str(names[index[1]])+"\n")
    f.write("Minimum grade is "+str(grades[index[1]])+"\n")
    f.close()

def main():
    path   = sys.argv[1]
    names = []
    grades = []

    f = open(path,'r')
    for line in f:
        fields = line.split(",")
        names.append(fields[0])
        grades.append(float(fields[1]))
    
    f.close()
    
    index = stats(grades)
    output(grades,index)
    extracredit(names,grades,index)

# main function 
main()

