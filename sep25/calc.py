
# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING CODE WRITTEN BY OTHERS. 
# Ablimit Aji
# aaji@mathcs.emory.edu

count = int(input("Please input the upper bound of summation:\n "))

allSum = 0
evenSum = 0
oddSum = 0

while count >0:
    allSum = allSum + count
    if count % 2 == 0:
        evenSum = evenSum + count
    else:
        oddSum = oddSum + count
    count = count - 1

print ("All Sum  = " + str(allSum))
print ("Odd Sum  = " + str(evenSum))
print ("Even Sum = " + str(evenSum))

# calculate factorial as a practice
