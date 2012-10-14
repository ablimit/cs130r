# sample solution for calc.py

num = int(input ("Please enter an integer:\n"))

# initilize aggregators for all, odd, even sum
allSum  = 0
oddSum  = 0
evenSum = 0

# index for loop control 
index =0


while num > 0:
    allSum += num
    # selectivly add odd/even numbers to the corresponding aggregator
    if num % 2 == 1:
    	oddSum += num
    else:
    	evenSum += num
    num -= 1

# output results

print("All sum is " + str(allSum))
print("Odd sum is " + str(oddSum))
print("Even sum is " + str(evenSum))
