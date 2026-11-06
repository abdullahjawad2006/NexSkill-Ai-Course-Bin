#Count Vowels & Consonants
string1="Hello, World! 123"
vowels=0
consonnats=0
for ch in string1:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels+=1
        else:
            consonnats+=1
print("Vowels:",vowels)
print("Consonants:",consonnats)
#Palindrome Check (Ignore Case & Non-alphanumerics)
string2="A man, a plan, a canal: Panama!"
new_string=""
for ch in string2:
    if ch.isalnum():
     new_string += ch.lower()
if new_string == new_string[::-1]:
    print("True")
else:
    print("False")
#Convert a sentence to title case without using .title()
string3= "hELLO wORLD from PYTHON"
words = string3.split()
new_string = ""
for word in words:
    new_string += word[0].upper() + word[1:].lower() + " "
print(new_string.strip())
#find all indices of a substring (allow overlaps)
string4 = "aaaa"
sub = "aa"
indices = []
for i in range(len(string4) - len(sub) + 1):
    if string4[i:i + len(sub)] == sub:
        indices.append(i)
print(indices)
#Build a frequency dictionary for characters (case-insensitive, skip spaces).
string = "Baa Baa Black Sheep"
frequency = {}
for ch in string.lower():
    if ch != " ":
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1
print(frequency)
#Anagram Checker
string1 = "Listen"
string2 = "Silent"
new_string1 = ""
new_string2 = ""
for ch in string1:
    if ch.isalpha():
        new_string1 += ch.lower()
for ch in string2:
    if ch.isalpha():
        new_string2 += ch.lower()
if sorted(new_string1) == sorted(new_string2):
    print(True)
else:
    print(False)
#Compress Repeated Characters (RLE-lite)
string6 = "aaabbcaaaa"
string7 = ""
count = 1
for i in range(1, len(string6)):
    if string6[i] == string6[i - 1]:
        count += 1
    else:
        string7 += string6[i - 1] + str(count)
        count = 1
string7 += string6[-1] + str(count)
print(string7)
#Longest Word in a Sentence
string10 = "Find the longest_word here!"
words = string10.split()
longest = ""
for word in words:
    clean_word = ""
for ch in word:
    if ch.isalpha():
     clean_word += ch
if len(clean_word) > len(longest):
    longest = clean_word
print(longest)
#Remove Duplicate Characters but Keep Order
string11="banana"
result=""
seen=set()
for ch in string11:
    if ch not in seen:
        result+=ch
        seen.add(ch)
#Mask Email Username
string12 = "john.doe@example.com"
parts = string12.split("@")
username = parts[0]
domain = parts[1]
stars = "*" * (len(username) - 2)
print(username[0] + stars + username[-1] + "@" + domain)




