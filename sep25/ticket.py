# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# CODE WRITTEN BY OTHERS. Ablimit Aji
# 

limit = input("Please input the speed limit:\n ")
speed = input("Please input the violation speed:\n ")
diff = int(speed) - int(limit)

fine  = int(diff)*5

if int(speed) >= 85:
	fine = fine + 200

print("You will be fined $" + str(fine))
