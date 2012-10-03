# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING CODE WRITTEN BY OTHERS. 

gene = input("HAL: Captin Kirk, I'm ready to scan and clean the sequence:\n")

cleanGene = ""  # the new gene sequence after cleaning

for nucleic_acid in gene:
    
    if  nucleic_acid != "A" and nucleic_acid != "C" and nucleic_acid != "G" and nucleic_acid != "T":
        continue
    
    cleanGene += nucleic_acid
    
    print("Current nucleic acid is: " +nucleic_acid)

print ("HAL: Captin Kirk, gene sequence after cleansing is: " + cleanGene)


