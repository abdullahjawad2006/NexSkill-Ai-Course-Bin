print("------------ ELECTRICITY BILL ------------")
customer_name=input("Enter Customer Name:")
meter_number=input("Enter meter number:")
units_consumed=float(input("Enter number of units consumed:"))
unit_price=float(input("Enter price per unit:"))
total_bill=units_consumed*unit_price

print("----------- YOUR BILL ----------")
print("Customer Name:",customer_name)
print("Meter Number:",meter_number)
print("Units Consumed:",units_consumed)
print("Price per Unit:",unit_price)
print("Your Total Bill:",total_bill)

print("THANK YOU",customer_name,"for using our electricity service")
print("---------------------------------------------------")
      



                 