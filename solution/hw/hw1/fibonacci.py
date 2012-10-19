
n = int(input("Please input the sequence number: "))
f1 = 0
f2 = 1

while n>1:
    f3 = f1+f2
    f1 = f2
    f2 = f3
    n -= 1 

print ("The",n,"th Fibonacci number is",f2)
