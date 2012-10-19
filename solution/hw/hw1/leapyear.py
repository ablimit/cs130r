year = int(input("Please input the year: "))

flag = False
if   year % 400 == 0:
    flag = True
elif year % 100 == 0:
    flag = False
elif year % 4   == 0:
    flag = True
else:
    flag =False

if flag:
    print ("Year", year, "is a leap year.")
else:
    print ("Year", year, "is NOT a leap year.")

