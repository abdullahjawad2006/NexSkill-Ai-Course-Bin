#Write a program that reads a string and prints its length.
string1="hello world"
print(len(string1))
#Convert the input string to uppercase and lowercase.
string2="Python3"
print(string2.upper())
print(string2.lower())
#Count how many times a given character appears in a string (case-sensitive).
string3="banana"
print(string3.count("a"))
#Print the first and last character of a string; handle empty input
string4="drawer"
if not string4:
    print("the string is empty")
else:
    print("First:",string4[0])
    print("Last:",string4[-1])
#Check if a substring exists in a string.
string5="data science"
if "science" in string5:
    print("True")
else:
    print("False")
#Print a substring from index start to end (exclusive).
string6="programming"
print(string6[3:8])
#Reverse a String
string7="python"
print(string7[::-1])
#Replace Substring
string8= "I love apples. Apples are great!"
old="apples"
new="oranges"
print(string8.replace(old,new))
#Split and Join
string9="split this sentence"
words=string9.split()
print("-".join(words))
#Strip Whitespace
string10=" padded text "
print(string10.strip())



