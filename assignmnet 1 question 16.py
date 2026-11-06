# Calculate Body Mass Index (BMI)
# Input weight (kg) and height (m), then calculate:
# BMI = weight / (height ** 2)
weight=int(input("Enter weight in kg:"))
height=float(input("Enter height in meter:"))
body_mass_index= weight / (height ** 2)
print("Your BMI:", float(body_mass_index))

