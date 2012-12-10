import sys

grades = {}

def readfile():
    f = open(sys.argv[1], 'r')
    for line in f:
        sp= line.strip().split(',')
        name = sp [0]
        grade = int (sp[1])
        grades[name] = grade
    f.close()

def query(name):
    query = print(name, "'s grade is ", grades[name], sep = '')

def prompt():
    name = input('Please input the student name to query or type "exit" to exit the program: ')
    return name

def main():

    readfile()
    number_students = len(grades)
    print('I have read in', number_students, "student's information.")
    
    name = prompt()
    while name != 'exit':
        if name in grades:
            query(name)
        else:
            print(name, 'not in grades file.')
        name = prompt()


if len(sys.argv) <2:
    print ("Error: Missing param.")
    print("Usage: python3 query.py [grade.csv]")
    sys.exit()

# main function
main()
