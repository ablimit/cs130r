basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed


# fast membership testing

if 'Orange' in basket:
    print("We got orange in our basket.")

if 'pomegranate' in basket:
    print ("We don't have my favorite item in the basket.")


# set operations on unique letters from two words
# can construct a set by passing a sequence 
a = set('abracadabra')
b = set('alacazam')
# print(a)

# unique letters in a
print("set a:", a)                                  

print("set b:", b)

# letters in a but not in b
print("a -b", a - b)                      

# letters in either a or b
print("a|b", a | b )                             

# letters in both a and b
print("a&b",a & b) 

# letters in a or b but not both
print("a^b",a ^ b)

# what is this ? 
print ("?", a&b | a^b)
