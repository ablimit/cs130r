
n = int(input("Please input a number:\n"))

a = 0  # first fibonacci nnumber
b = 1  # second fibonacci nnumber
c = 0  # temporary variable 

i =1   # counter 

fib_list = [a,b]
while i < n:
    c = a + b  # new fibonacci number 
    a = b      # advance a to next fibonacci number
    b = c      # advance b to the next fibonacci number
    fib_list.append(c)
    i = i+1    # update counter

# print("The fiabonacci number is " + str(b))
# print(fib_list)

# next we print them in reverse order
print("Fibonacci numbers in reverse order ")
for i in range(n,0,-1):
    print(fib_list[i])

