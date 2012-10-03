# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING CODE WRITTEN BY OTHERS. 

gene = input("HAL: Captin Kirk, I'm ready to scan the gene sequence:\n")

prefix = ""
index = 1

for nucleic_acid in gene:
    prefix = prefix + nucleic_acid
    index  = index  + 1
    if  index >= 4:
        break

print ("HAL: Captin Kirk, this gene starts with " + prefix )


