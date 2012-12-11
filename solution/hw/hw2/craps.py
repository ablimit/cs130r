import random

def roll():
	a = random.randint(1,6)
	b = random.randint(1,6)
	print("You rolled", a, "+", b, "=", a + b)
	return a + b

def play():
	res = roll()
	if res == 2 or res == 3 or res == 12: 
		print("You lose") 
		return False
	elif res == 7 or res == 11: 
		print("You win") 
		return True
	else:
		print("point is", res)
		res2 = roll()
		while res2 != 7 and res2 != res:
			res2 = roll()
		if res2 == 7:
			print("you lose")
			return False
		else:
			print("you win")
			return True

play()