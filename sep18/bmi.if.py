
#  BMI (body mass index) example for Sep 18
# Formula -->   BMI = (weight in punds * 703) / (height in inches)^2

# Below 18.5  Underweight
# 18.5 -24.9  Normal
# 25 - 29.9   Overweight
# 30 & Above  Obese


# example of multiple if statments to correctly hint BMI 
bmi = 22.0 

print("Your Body Mass Index is " + str(bmi))

if bmi < 18.5:
    print(" Eat more protin.")

if bmi >=18.5 and bmi < 25.0:
    print("Awesome ! Just keep your lifestyle.")

if bmi >=25 and bmi < 30.0:
    print("Resist pizza and snacks.")

if bmi >= 30:
    print("It's time to start training for an Ironman !")


