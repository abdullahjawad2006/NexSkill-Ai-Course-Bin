#Write a program to create a new string made of an input string’s first,middle, and last character.
string=input("Enter string:")
new_string= string[0] + string[len(string) // 2] + string[-1]
print(new_string)
#Write a program to count occurrences of all characters within a string
for i in string:
    print(i,":",string.count(i))
#Reverse a given string
print(string[::-1])
#Split a string on hyphens
string2= "apple - mango - banana"
print(string2.split("-"))
#remove special symbols/punctuation from a string
string3= "hello@*&world"
result="".join(i for i in string3 if i.isalnum())
print(result)





