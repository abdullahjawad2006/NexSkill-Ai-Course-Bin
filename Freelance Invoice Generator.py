print("============================================")
print("       FREELANCE INVOICE GENERATOR           ")
print("============================================")
freelancer_name=input("Enter Freelancer Name:")
client_name=input("Enter Client Name:")
company_name=input("Enter Company Name:")
project_name=input("Enter Project Name:")
hours_worked=float(input("Enter number of hours worked:"))
hourly_rate=float(input("Enter hourly rate(Rs per hour):"))
add_charges=float(input("Enter additional expenses(internet):"))
project_cost=hours_worked*hourly_rate
total_invoice=project_cost + add_charges
print("=============================================")
print("                 INVOICE                   ")
print("=============================================")

print("Freelancer Name:",freelancer_name)
print("Client Name:",client_name)
print("Company Name:",company_name)
print("Project Name:",project_name)

print("---------------------------------------------")
print("Hours Worked:",hours_worked)
print("Hourly Rate:",hourly_rate)
print("Project Cost:",hourly_rate)

print("Additional Expenses:",add_charges)
print("-------------------------------------------")

print("TOTAL AMOUNT:",total_invoice)

print("==========================================")

print("Thank you for your business!")

print("==========================================")


