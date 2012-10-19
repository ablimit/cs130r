import random

log = "" # to record the outcome of each coin toss 
headCount = 0  # count of heads in a row

# total coin toss
toss = 0

while headCount < 3:
    coin = random.randint(0,1) # 0 represents tail & 1 represents head
    toss += 1
    if coin == 1:
        log += 'H'
        headCount += 1
	# if we get 3 heads in a row, we exit the loop
        if headCount == 3: 
            break
    else:
        log += 'T'
        headCount = 0  # reset the counter


print (log)
print ("It took", toss, "flips to get 3 heads in a row.")

