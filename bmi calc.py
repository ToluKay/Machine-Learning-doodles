#Build a function that calculates BMI... height in m, weight in kg
def bmi_cal():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in m: "))
    bmi = weight/(height**2)
    
    if bmi < 18.5:
        return("Your BMI is ", bmi, ". This is considered underweight.")
    elif bmi >= 18.5 and bmi < 25.0:
        return("Your BMI is ", bmi, ". This is considered healthy weight.")
    elif bmi >= 25.0 and bmi < 30.0:
        return("Your BMI is ", bmi, ". This is considered overweight.")
    elif bmi >= 30.0 and bmi < 35.0:
        return("Your BMI is ", bmi, ". This is considered Class 1 obesity.")
    elif bmi >= 35.0 and bmi < 40.0:
        return("Your BMI is ", bmi, ". This is considered Class 2 obesity.")
    elif bmi <= 40.0:
        return("Your BMI is ", bmi, ". This is considered Class 3 obesity.")

bmi_cal()