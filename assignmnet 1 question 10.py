# #Salary Calculator
# Input basic salary. Calculate:
#  HRA = 20% of basic
#  DA = 15% of basic
#  Total Salary = Basic + HRA + DA
basic_salary=int(input('Enter basic salary:'))
house_rent_allowance=basic_salary * 20/100
dearness_allowance=basic_salary * 15/100
total_salary= basic_salary + house_rent_allowance + dearness_allowance
print("HRA:", house_rent_allowance)
print("DA:", dearness_allowance)
print("Total Salary:", total_salary)
