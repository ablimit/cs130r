import random

sentence = input("Please input a sentence:\n")
words = sentence.split()
size = len(words)

# reset output sentence
sentence = ""
# empty space to seperate words in a sentence
space = " "

while size!= 0:
    size -= 1 
    index = random.randint(0,size)
    word = words[index]
    sentence = sentence + word  + space
    # remove the word from the list
    del words[index]

print(sentence)
