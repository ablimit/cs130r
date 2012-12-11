import random

def roll():
	a = random.randint(1,6)
	b = random.randint(1,6)
	return a + b

def play():
	res = roll()
	if res == 2 or res == 3 or res == 12: 
		return False
	elif res == 7 or res == 11: 
		return True
	else:
		res2 = roll()
		while res2 != 7 and res2 != res:
			res2 = roll()
		if res2 == 7:
			return False
		else:
			return True


n = 100000
win = 0
for i in range(n): 
	if play(): win += 1
print("the chance of winning:", win/n)