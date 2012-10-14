# sample solution for ticket.py

# assuming all user inputs are valid, we omit input validation

limit = int(input("Please input the speed limit:\n"))
speed = int(input("Please input the violation speed:\n"))

diff  = speed - limit
fine  = diff * 5.0

# check for superspeeder fine
if speed >= 85:
    fine  += 200.0

print("You will be fined $" + str(fine))

