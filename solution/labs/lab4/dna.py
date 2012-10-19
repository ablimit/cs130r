
geneSequence = input("HAL: Captin Kirk, I'm ready to scan the sequence.\n")
a = 0 # count of adenine 
t = 0 # count of thymine 
c = 0 # count of cytosin
g = 0 # count of guanine

prefix = ""

#loop which counts individual acids in the sequence.

for letter in geneSequence:
    if letter   == 'A' or letter == 'a' :
        a += 1
    elif letter == 'T' or letter == 't' :
        t += 1
    elif letter == 'C' or letter == 'c' :
        c += 1
    elif letter == 'G' or letter == 'g' :
        g += 1
    else:
        print("invalid string")

# to extract prefix we use a loop
i = 0 
for letter in geneSequence:
    if i< 4:
        prefix += letter.lower()
    i += 1 

# print ("prefix", prefix)

if a==t and t==c and c==g and prefix == "tcga":
    print ("HAL: This is a silicon based life form.")
else:
    print ("HAL: This is a carbon based life form.")

