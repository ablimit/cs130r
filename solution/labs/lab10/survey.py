#! /usr/bin/python3

def readset(path):
    """ Opens a text file, reads the contents of each line as a string into a set.
    Input: path, type string: a file system path to the target file
    Output: f_set, type set: file content as a set"""

    f = open(path, 'r')
    f_set = set()
    for line in f:
        f_set.add(line.strip())
    return f_set

def main():
    football   = readset('/home/cs130r00/share/labs/lab10/football.txt')
    baseball   = readset('/home/cs130r00/share/labs/lab10/baseball.txt')
    basketball = readset('/home/cs130r00/share/labs/lab10/basketball.txt')
    respondents = football | baseball | basketball
    all_three = football & baseball & basketball
    football_notbasketball = football - basketball
    football_basketball = (football | basketball) - baseball
    bonus = (football & basketball) - baseball
    
    print('Number of people who responded to the survey:', len(respondents))
    print('Number of people who watch all three sports:', len(all_three))
    print('Number of people who watch football but not basketball:', len(football_notbasketball))
    print('Number of people who watch football or basketball but not baseball:', len(football_basketball))
    print('Number of people who watch football and basketball but not baseball:', len(bonus))


main()

