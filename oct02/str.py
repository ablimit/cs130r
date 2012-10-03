# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING CODE WRITTEN BY OTHERS. 

gene = "ACGTTGCAGTCAAGTCCTGTGTACACGTC"

# c in seq    (existance)
c ='A'
if c in gene:
    print("Gene has "    + c)
else:
    print("Gene has no " + c)


# c not in seq (absence)
c ='R'
if c not in gene:
    print("Gene has no " + c)
else:
    print("Gene has "    + c)


#a + b      (concatenation)
a ='Emory '
b ='University'
print(a+b)

# s * n  (n copy of s)
s ='Emory'
n = 2
print(s*n)
print(n*s)
n = -1
print(n*s)

# access individual characters 
# s[i]   (ith item of s )
s ='Emory'
print(s[0])
print(s[4])
#print(s[5])

print(s[-1])
print(s[-5])
#print(s[-6])


# s[i:j]   (slice of s from ith item to jth item)  Note: jth item is exclusive  
s = "Emory"
print(s[-2:-1])
print(s[-1:-3] + 'tional')


#len(s)                  (lenth of s )
s = "Emory"
print(len(s))
print(s[-len(s)])           # first item

# utility functions specific to strings

s = "Emory"

print (s.lower()) # change s to all lower case 
print (s.upper()) # change s to all upper case 
print (s.startswith('E'))  #  if s starts with the given string
print (s.endswith('E'))    # if s ends with the given string


