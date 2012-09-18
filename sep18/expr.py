#  Expressions 
# precedence comp < +,- < *,/,//,% < +x,-x < ** < (exp)

weight = 135.5
height = 70.0

# this is wrong 
bmi = weight *703 / height * height 

# this is right 
bmi = weight *703 / (height * height) 

expr = 5*2**3
print(expr)

expr = (5*2)**3
print(expr)


