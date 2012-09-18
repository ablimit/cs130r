
#  BMI (body mass index) example for Sep 18
# Formula -->   BMI = (weight in punds * 703) / (height in inches)^2

# Below 18.5  Underweight
# 18.5 -24.9  Normal
# 25 - 29.9   Overweight
# 30 & Above  Obese

bmi = 22.0 

print("Your Body Mass Index is " + str(bmi))

if bmi < 18.5:
    print(" Eat more protin.")
elif bmi < 25.0:
    print("Awesome ! Just stick to your lifestyle.")
elif bmi < 30.0:
    print("Resist some pizza and snacks.")
else:
    print("It's time to start training for an Ironman Triathlon !")

