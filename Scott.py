#Weight Value.
weightValue=float(input("Enter Weight Value:"))
#Height Value.
heightValue=float(input("Enter Height Value:"))
#Outputs weight in pounds.
print("Weight Value: Pounds:" + str(weightValue))
#Outputs height in inches.
print("Height Value: Inches:" + str(heightValue))
#Calculations for finding BMI.
bmiValue=(weightValue*703)/(heightValue)**2
#Formats output to two decimal places
formatted_float="{:.2f}".format(bmiValue)
#Outputs BMI value in percentage form.
print("BMI Value: %" + str(formatted_float))




                  
