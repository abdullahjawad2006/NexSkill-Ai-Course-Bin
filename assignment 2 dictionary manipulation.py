#Check if a value exists in a dictionary
thisdict1={
    "Name":"Abdullah",
    "Age" : 20,
    "City":"Lahore"
}
if "Abdullah" in thisdict1.values():
    print("Value Found")
else:
    print("Value not found")
#Get the key of a minimum value from the following dictionary
marks={
    "Ali":85,
    "Ahmed":72,
    "Sara":91
}
print(min(marks,key=marks.get))
##Get the key of a minimum value from the following dictionary
marks={
    "Ali":85,
    "Ahmed":72,
    "Sara":91
}
print(min(marks,key=marks.get))
##Get the key of a minimum value from the following dictionary
marks={
    "Ali":85,
    "Ahmed":72,
    "Sara":91
}
print(min(marks,key=marks.get))
##Get the key of a minimum value from the following dictionary
marks={
    "Ali":85,
    "Ahmed":72,
    "Sara":91
}
print(min(marks,key=marks.get))
#Delete a list of keys from a dictionary
del marks["Ahmed"]


