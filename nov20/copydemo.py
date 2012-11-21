
grades = {"Jason" : 97, "Chris" : 87, "Emily": 91, "Michael": 88, "Joel": 77}

# copying the reference is dangerous 
print("Original Dictionary:\n",grades)

#grades_dup = grades 

#grades_dup["Jason"] = 59.0

#print("Grades:\n", grades)
#print("Grades_dup:\n", grades_dup)


# deep copy dictionary 

grades_dup = grades.copy()

grades_dup["Jason"] = 59.0

print("Grades:\n", grades)
print("Grades_dup:\n", grades_dup)


