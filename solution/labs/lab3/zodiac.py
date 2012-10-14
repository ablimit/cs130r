print("Hey, let's figure out your Zodiac sign!")
month = int( input ("First, enter is your birth month: ") )
day   = int( input ("Next, enter your birth day: ") )

if month == 1:
	if day < 20:
		print ("You are a Capricorn.")
	elif day <=31:
		print ("You are a Aquarius.")
	else:
		print ("invalid input.")

elif month == 2:
	if day < 18:
		print ("You are a Aquarius.")
	elif day <= 29:
		print ("You are a Pisces.")
	else:
		print ("invalid input.")

elif month == 3:
	if day < 20:
		print ("You are a Pisces.")
	elif day <= 31:
		print ("You are a Aries.")
	else:
		print ("invalid input.")

elif month == 4:
	if day < 20:
		print ("You are a Aries.")
	elif day <= 30:
		print ("You are a Taurus.")
	else:
		print ("invalid input.")

elif month == 5:
	if day < 21:
		print ("You are a Taurus.")
	elif day <= 31:
		print ("You are a Gemini.")
	else:
		print ("invalid input.")

elif month == 6:
	if day < 21:
		print ("You are a Gemini.")
	elif day <= 30:
		print ("You are a Cancer.")
	else:
		print ("invalid input.")

elif month == 7:
	if day < 23:
		print ("You are a Cancer.")
	elif day <= 31:
		print ("You are a Leo.")
	else:
		print ("invalid input.")

elif month == 8:
	if day < 23:
		print ("You are a Leo")
	elif day <= 31:
		print ("You are a Virgo.")
	else:
		print ("invalid input.")

elif month == 9:
	if day < 23:
		print ("You are a Virgo.")
	elif day <= 30:
		print ("You are a Libra.")
	else:
		print ("invalid input.")

elif month == 10:
	if day < 23:
		print ("You are a Libra.")
	elif day <= 31:
		print ("You are a Scorpio.")
	else:
		print ("invalid input.")

elif month == 11:
	if day < 22:
		print ("You are a Scorpio.")
	elif day <= 30:
		print ("You are a Sagittarius.")
	else:
		print ("invalid input.")

elif month == 12:
	if day < 22:
		print ("You are a Sagittarius.")
	elif day <= 31:
		print ("You are a Capricorn.")
	else:
		print ("invalid input.")
