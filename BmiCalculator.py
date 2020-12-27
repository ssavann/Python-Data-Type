#Body Mass Index calculation
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmiCalculation = float(weight) / float(height)**2       #need to convert "height" and "weight" into a float
bmi = str(bmiCalculation)

print("Your BMI is: " + bmi)

#if I want an Integer number instead of decimal number
bmiToInteger = int(bmiCalculation)
bmiToString = str(bmiToInteger)
print("Your BMI is: " + bmiToString)

#or
print("Your BMI is: " + str(bmiToInteger) + " second option")

