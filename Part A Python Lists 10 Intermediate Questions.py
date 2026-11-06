#1.	Create a list comprehension that returns the squares of only the even numbers from 0–20.
#Tip: Use an if condition inside the comprehension.
list1=[]
for x in range(21):
    if x%2 == 0:
     print(list1.append(x**2))
print(list1)
#2.	Given nums = [3, 1, 4, 1, 5, 9], sort the list without modifying the original.
#Tip: Use sorted() instead of .sort().
given_nums=[3,1,4,1,5,9]
new_list=sorted(given_nums)
print(new_list)
print(given_nums)
#3.	Remove duplicates from a list while preserving the original order.
#Tip: Track seen values in a new list.
nums=[3,1,4,1,5,3,9]
new_list1=[]
for x in nums:
   if x not in new_list1:
     new_list1.append(x)
print(new_list1)
#4.	Flatten the nested list [[1, 2], [3, 4], [5]] into a single list using a list comprehension.
#Tip: Use a nested loop inside the comprehension.
nestedlist=[[1,2],[3,4],[5]]
new_list2=[]
for x in nestedlist:
   for y in x:
      new_list2.append(y)
print(new_list2)
#5.	Given names = ['alice', 'Bob', 'charlie', 'DAVID'], sort them alphabetically but ignore case.
#Tip: Use key=str.lower.
given_names=['alice','Bob','charlie','DAVID']
new_names=sorted(given_names,key=str.lower)
print(new_names)
#6.	Replace items from index 2–4 in a list with [100, 200] using slice assignment.
#Tip: Use a[2:5] = [...].
list3=[400,500,600,700,800,900,1000]
list3[2:5]=[100,200]
print(list3)
#7.	Write a program to find all indices of a value in a list (e.g., all indices of 7).
#Tip: Use enumerate.
list4=[5,7,2,7,9,7]
for i,x in enumerate(list4):
   if x==7:
      print(i)
#8.	Create a new list containing only elements that appear exactly once in the original list.
#Tip: Use list.count() inside a comprehension.
original_list = [1, 2, 3, 2, 4, 5, 1, 6]
new_list3=[]
for x in original_list:
   if original_list.count(x)==1:
      new_list3.append(x)
print(new_list3)
#9.	Rotate a list right by one position (e.g., [1,2,3,4] → [4,1,2,3]).
#Tip: Use slicing: lst[-1:] + lst[:-1].
list5=[1,2,3,4]
print(list5[-1:] + list5[:-1])
#10.	Split a list into two lists: one with even numbers, one with odd numbers.
#Tip: Create two comprehensions.
list6=[1,2,3,4,5,6,7,8,9,10]
even_list=[]
odd_list=[]
for x in list6:
   if x % 2 ==0:
      even_list.append(x)
   else:
    odd_list.append(x)
print(even_list)
print(odd_list)

  

















