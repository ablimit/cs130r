# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING CODE WRITTEN BY OTHERS. 

# empty tuple creation 
myGarage = ("MACBOOK")
print (len(myGarage)) # length should be zero
print(myGarage)       # prints contents of the tuple



# a tuple with similar (same types) of items
neighborGarage = ("Veyron", "cat", "shoe")
print ("There are " +str(len(neighborGarage)) + " items in your neighbor's garage.")


# basically all sequence operations can be applied to tuples 

# c in seq    (existance)
item ="Veyron"
if item in neighborGarage:
    print("You have your car in the grage.")
else:
    print("Call 911.")


# c not in seq (absence)
item ='Macbook'

if item not in myGarage:
    print("Your macbook is on your desk.")
else:
    print("Are you starting a business ?")

# myGarage is a tuple which contains different kinds of items 
# specifally it contais a floating point number, an integer and a boolean value

myGarage = (3.14, 9, True)

#a + b      (concatenation)
print( myGarage + neighborGarage ) # generates a new tuples with the items added together

#s * n  (n copy of s)
n = 2
print(neighborGarage*n)


# s[i]   (ith item of s )
print(neighborGarage[0])
print(neighborGarage[-1])
# print(neighborGarage[-6])


#s[i:j]   (slice of s from ith item to jth item)  Note: jth item is exclusive  
print(neighborGarage[0:2])


