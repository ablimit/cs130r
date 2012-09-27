
# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING CODE WRITTEN BY OTHERS. 

import random

count = int(input("Experiment repetition count:\n"))

heads  = 0
tails  = 0

i = count 

while i >0:
    face = random.randint(1,2)
    if face == 1:
        heads += 1
    else:
        tails += 1

    i = i - 1

print ("Prob[h] = " + str(heads/count))
print ("Prob[t] = " + str(tails/count))

