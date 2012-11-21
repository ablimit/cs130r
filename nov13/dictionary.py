
grades = {"Jason" : "97", "Chris" : "87", "Emily": "91"}

print(grades)

# some functions applies to sequence types 
print("Length of the dictionary is:", len(grades))

# access

print("Jason's grade:" , grades["Jason"])

print("Emily's grade:" , grades["emily"])


# update
# add new entry 
grades["Kevin"] = '67'

print("Kevin's grade:" , grades["Kevin"])

print(grades)

# update old values

grades["Chris"] = '78'



# delete 

# individual entry 
del grades["Kevin"]


# clear entries  
grades.clear()

