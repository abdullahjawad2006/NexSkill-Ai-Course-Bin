#1.	Count word frequencies in a sentence and store the results in a dictionary.
#Tip: Use d[word] = d.get(word, 0) + 1.
sentence = "apple banana apple orange banana apple"
word_count={}
sentence.split()
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
#2.	Invert a dictionary where all values are unique.
#Tip: Swap key and value in a loop.
dict1={
    'Name':'Abdullah',
    'Age': 20,
    'Height':5.7
}
new_dict={}
for key in dict1:
    value=dict1[key]
    new_dict[value]=key
    print(new_dict)
#3.	Merge two dictionaries where second dictionary overrides first.
#Tip: Use {**dict1, **dict2} or dict1 | dict2 (Python 3.9+).
dict1={
    'Name':'Abdullah',
    'Age': 20,
    'Height':5.7
}
dict2={
    'Age':21,
    'Country':"Pakistan"
}
new_dict2={**dict1,**dict2}
print(new_dict2)
#4.	Group words by their first letter into a dictionary of lists.
#Tip: Use setdefault
words = ["apple", "ant", "banana", "ball", "cat"]
grouped={}
for word in words:
    first_letter=word[0]
    grouped.setdefault(first_letter,[]).append(word)
print(grouped)
#5.	Filter a dictionary to keep only entries with values greater than 50.
#Tip: Use a dictionary comprehension.
marks = {
    "Ali": 45,
    "Ahmed": 80,
    "Sara": 60,
    "Usman": 30
}
new_marks={name:score for name, score in marks.items() if score > 50}
print(new_marks)
#6.	Given a nested dictionary, safely access a deeply nested key.
#Tip: Chain .get() calls with default {}.
student={
    "name":"abdullah",
    "marks": {
        "math": {
            "mid":80,
            "final":90
        }
    }
}
result=student.get("marks",{}).get("math",{}).get("final")
print(result)
#7.	Write a dictionary comprehension that maps numbers 1–10 to their cubes.
#Tip: {x: x**3 for x in range(1,11)}.
cube_dict={x:x**3 for x in range(1,11)}
print(cube_dict)
#8.	Find the key with the highest value in a dictionary.
#Tip: Use max(d, key=d.get).
marks = {
    "Ali": 45,
    "Ahmed": 80,
    "Sara": 60,
    "Usman": 30
}
highest=max(marks,key=marks.get)
print(highest)
#9.	Combine two lists into a dictionary (keys from first list, values from second).
#Tip: Use zip().
keys=["Name","Age","City"]
values=["Abdullah",20,"Lahore"]
new_dict3=dict(zip(key,values))
print(new_dict3)
#10.	Remove all keys from a dictionary whose values are None.
#Tip: Check value before adding to new dict.
data={
    "Name":"ABdullah",
    "Age":None,
    "City":"Lahore",
    "Phone":None
}
new_dict4={}
for key,value in data.items():
    if value is not None:
        new_dict4[key]=value
print(new_dict4)






