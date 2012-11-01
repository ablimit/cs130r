
# doc string 
def mymax (a):
    """ This is function returns maximum member from a list of items
    Input: a list which contains comparable items
    Output: the maximum element by natural comparison
    """
    c = a[0]
    for i in a:
        if i > c:
            c = i
    return c 

newlist = [0,1,23,4,5,76,8]

# print(mymax(newlist))

print(mymax.__doc__)


