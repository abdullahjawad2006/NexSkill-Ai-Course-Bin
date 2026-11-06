# #Distribute Items Equally - You have n candies and k students.
# Write a program to find:
# how many candies each student gets
# how many are left
total_candies=int(input("Enter total number of candies:"))
total_students=int(input("Enter total number of students:"))
candy_each_student= total_candies//total_students
left_candies=total_candies % total_students
print("Candy each student gets:", candy_each_student)
print("Candies left:", left_candies)


