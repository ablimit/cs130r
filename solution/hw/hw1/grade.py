
points = float(input("Please specify the numeric grade: "))
fullgrade = 175.0

if points/fullgrade >= 0.9:
    print ("A")
elif points/fullgrade >= 0.8:
    print ("B")
elif points/fullgrade >= 0.7:
    print ("C")
elif points/fullgrade >= 0.6:
    print ("D")
else:
    print ("F")

