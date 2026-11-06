#Calculate Compound Interest Use the formula: CI = P * (1 + R/100)**T - P
#Where P = principal, R = rate, T = time
P=int(input("Enter principal amount:"))
R=float(input("Enter profit rate:"))
T=int(input("Enter time in years:"))
compound_interest= P * (1+R/100)**T - P
print("Compound interest:", int(compound_interest))

