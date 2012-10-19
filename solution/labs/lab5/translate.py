
date = input("Please input a date in numbers:\n")

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
days = ("First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelveth", "Thirteenth")
teens = ("One", "Two", "Three", "Four", "Fif", "Six", "Seven", "Eigh", "Nine")

month = int(date[0:2])
day   = int(date[3:])
# print (month,day)

monthName = months[month-1]
dayName = ""

if   day<=13:
    dayName = days[day-1]
elif day <20:
    dayName = teens[day-10-1] + "teenth"
elif day == 20:
    dayName = "Twentieth"
elif day < 30:
    dayName = "Twenty "+ days[day-20-1]
elif day == 30:
    dayName = "Thirtieth"
elif day == 31:
    dayName = "Thirty First"
else:
    print ("invalid input")

print (monthName,dayName)
