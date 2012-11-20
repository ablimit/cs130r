n = int(input("Please input a number:\n"))

print("Here is the multiplication table:")

for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j, end=" ")
    print()

