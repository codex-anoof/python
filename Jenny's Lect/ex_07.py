#BMI Result Finder
weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in m : "))
BMi = round(weight/ height ** 2)
print(f"Your BMI is {BMi} and")
res = "Result is : "
if BMi < 16:
    print(res,"UnderWeight --- (Severe Thinness)")
elif BMi > 16.0 and BMi < 16.9:
    print(res,"Underweight -- (Moderate Thinness)")
elif BMi > 17.0 and BMi < 18.4:
    print(res,"Underweight - (Mild Thinness)")
elif BMi > 18.5 and BMi < 24.9:
    print(res,"Noramal Range ")
elif BMi > 25.0 and BMi < 29.9:
    print(res,"OverWeight - (Pre-Obese)")
elif BMi > 30.0 and BMi < 34.9:
    print(res, "Obese - (Class I)")
elif BMi > 35.0 and BMi < 39.9:
    print(res,"Obese -- (Class II)")
elif BMi >= 40:
    print(res,"Obese --- Class III")