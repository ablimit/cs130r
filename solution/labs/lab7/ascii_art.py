
# example code 

def repeat_char(char, i):
    """Repeat_char prints a character i number of times to the terminal.
    Input: a character and an integer, i
    Output: the character is printed to the terminal i number of times without a newline."""    
    print(char * i, end = '')

def indent_char(indent, char, i):
    """Indent_char prints an indent of a given size and then a character i number of times to the terminal.
    Input: indent: integer number of spaces to print, char: any character and i: number of times to repeat that character
    Output: an indentation followed by the repeated character and a newline"""    
    repeat_char(' ', indent)
    repeat_char(char, i)
    print()

def print_column(indent, width, height, char):
    """Print_column prints a column of characters.
    Input: indent = integer # of spaces to indent, width = integer width of column, height = integer height of column, char = character to repeat.
    Output: the column is printed to the terminal."""    
    for i in range(height):
        indent_char(indent, char, width)

def print_triangle(height, char):
    """Print_triangle prints a triangle of a given height.
    Input: height = height of the triangle, char = character to build the triangle
    Output: the triangle is printed to the terminal"""    
    for i in range(height):
        indent_char(height - 1 - i, char, i * 2 + 1)

def main():
    """The main function calls the print_column and print_triangle functions."""    
    print_triangle(6, 'A')
    print_column(3, 5, 4, 'X')

# main method 
main()
