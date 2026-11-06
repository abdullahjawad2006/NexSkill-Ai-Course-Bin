# Total Marks and Percentage
# Input marks of 5 subjects. Print:
#  Total marks
#  Percentage
#  Average
subject1=int(input("Enter marks in English:"))
subject2=int(input("Enter marks in Maths:"))
subject3=int(input("Enter marks in computer:"))
subject4=int(input("Enter marks in Islamiat:"))
subject5=int(input("Enter marks in Pakstudies:"))
total_marks= subject1 + subject2 + subject3 + subject4 + subject5
percentage=(total_marks/400) * 100
average=(subject1 + subject2 + subject3 + subject4 + subject5) / 5
print("Total marks:", total_marks)
print("Percentage:", percentage)
print("Average:",average)



