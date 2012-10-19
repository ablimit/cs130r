import random

n = int(input("Please input the number of runs: "))

# count of heads in a row
headCount = 0

# variable i counts  the number of times we repeat the experiment
i = 0

# total coin toss
toss = 0

# records total number of coin toss
totalCount = 0

while i < n:
    while headCount < 3:
        # 0 represents tail & 1 represents head
        coin = random.randint(0,1)
        
        if coin == 1:
            headCount += 1
            # if we get 3 heads in a row, we exit the loop
            if headCount == 3: 
                break
        else:
            headCount = 0  # reset the counter
        toss += 1

    totalCount += toss

    # reset counters 
    toss = 0 
    headCount = 0 

    # increment the counter in the outer loop 
    i += 1

print ("It expected number of coin toss to get 3 heads in a row is", float(totalCount)/float(n))

