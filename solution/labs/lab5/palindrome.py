
userInput= input("Please input a word or phrase of your choice:\n")

word = ""
# eliminate non alphabetic characters (space, !, ? , etc)
for letter in userInput:
	if letter.isalpha():
		word += letter.lower()

# print ("input",word)

length = len(word)
flag   = True

for i in range(0,length):
    if word[i] != word[length-1-i]:
        flag = False
        break

if flag:
	print (userInput, "is a palindrome.")
else:
	print (userInput, "is NOT a palindrome.")

