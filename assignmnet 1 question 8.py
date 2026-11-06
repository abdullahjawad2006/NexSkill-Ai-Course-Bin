# #Input cost price and selling price. Display either:
# Profit and amount, or
# Loss and amount, or
# No Profit No Loss
cost_price=float(input("Enter cost price:"))
selling_price=float(input("Enter selling price:"))
if selling_price > cost_price:
    print("Profit:",selling_price - cost_price)
elif cost_price > selling_price:
    print("Loss:", cost_price - selling_price)
else:
    print("No Profit No Loss")


    
