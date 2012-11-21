
grades = {"Jason" : 97, "Chris" : 87, "Emily": 91, "Michael": 88, "Joel": 77}


print("Original Dictionary:\n",grades, "\n")

# iterate keys in a dictionay 
def keylist():
    key_list = grades.keys()
    print ("The students in our class:")
    for student in key_list:
        print(student)


# iterate values in a dictionary
def vallist():
    val_list = grades.values()
    grade_sum = 0.0
    for grade in val_list:
        grade_sum +=grade
    print ("\naverage grade is:", grade_sum/len(grades))


# iterate key value pairs 
# curve the grades 
# simple approach 
def simpleitercurve():
    key_list = grades.keys()
    for student in key_list:
        grades[student] = grades[student] + 5.0


def ontheflycurve():
    for student,grade in grades.items():
        grades[student] = grade + 5.0
    print("Curved Grades:\n",grades, "\n")


#ontheflycurve()

# add 5.0 points to Morgan if he didn't drop the class
# grade["Morgan"] would result in an error 

def membertest():
    if grades.has_key("Morgan"):
        print ("Morgan is enrolled in the class, so we will add 5.0 points.")
        grades["Morgan"] = grades["Morgan"] + 5.0
    else:
        print ("Morgan dropped the class, so we don't care.")


ontheflycurve()

