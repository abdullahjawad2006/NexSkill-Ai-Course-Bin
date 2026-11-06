#1.	Given two sets, find elements that are in the first set but not the second.
#Tip: Use the - operator
set1={20,45,98}
set2={10,52,79}
result=set1-set2
print(result)
#2.	Find common items between three sets using intersection.
#Tip: Use set1 & set2 & set3.
set3={25,45,95,56}
set4={25,67,87,51}
set5={20,67,87,59}
result=set3 & set4 & set5
print(result)                                            #Output: set()
#3.	Given a sentence, return all unique words in lowercase.
#Tip: Split the string → lowercase → convert to set.
sentence="My name is Abdullah Full Stack AI Development Pandas Numpy Seaborn TensorFlow SckitLearn"
parts=sentence.split()
lower_words=[]
for word in parts:
    lower_words.append(word.lower())
print(set(lower_words))
#4.	Convert a list with duplicates into a set, then back to a sorted list.
#Tip: Use sorted(set(list)).
list1=[99,11,34,44,99,44,14,10,14,11]
result1=sorted(set(list1))
print(result1)
#5.	Check if one set is a strict subset of another.
#Tip: Use < operator.
set6={1,4,8,10}
set7={1,4}
if set7<set6:
    print("It is a strict subset")
else:
    print("It is not a subset")
#6.	Use a set comprehension to collect all squares of numbers from 1–15 that are divisible by 3.
#Tip: Write {x*x for x in ... if x % 3 == 0}.
set8={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
squares={x*x for x in set8 if x%3==0}
print(squares)
#7.	Count how many duplicate values exist in a list using sets.
#Tip: Compare lengths: len(list) - len(set(list)).
list2=[2,4,6,87,98,89,4,98,32,55,90,11,32,55,90]
print(len(list2)-len(set(list2)))
#8.	Write a program to remove all vowels from a string using a set.
#Tip: Use a vowel set and filter characters
string1="Ali and Omar are at home."
set10={'a','e','i','o','u'}
new_string=""
for char in string1:
    if char.lower() not in set10:
        new_string+=char
print(new_string)
#9.	Find the symmetric difference between two sets.
#Tip: Use the ^ operator
set11={1,2,3,4}
set12={3,4,5,6}
result2=set11 ^ set12
print(result2)
#10.	Check if two strings are anagrams using set comparison (unique characters only).
#Tip: Compare set(str1) with set(str2).
string2="silent"
string3="listen"
if set(string2) == set(string3):
    print("Anagram")
else:
    print("Not Anagram")
