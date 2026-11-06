#Create a dictionary {'name': 'Ali', 'age': 25} and print the name.
#Tip: Use d['name'].
dict1={
    'name':'Ali',
    'age': 25
}
print(dict1['name'])
#Add key 'city': 'Lahore' to a dictionary.
#Tip: Use assignment: d['city'] = 'Lahore'.
dict1['city']='Lahore'
print(dict1)
#Change 'age' in {'name': 'Ali', 'age': 25} to 30.
#Tip: Assign a new value: d['age'] = 30.
dict1['age']=30
print(dict1)
#Delete key 'age' from a dictionary.
#Tip: Use del d['age'].
del(dict1['age'])
print(dict1)
#Check if key 'salary' exists in a dictionary.
#Tip: Use in operator.
if 'salary' in dict1:
    print("It exists")
else:
    print("It dosnt exist")
#. Print all keys from {'a': 1, 'b': 2}.
#Tip: Use d.keys().
dict2={'a':1,'b':2}
print(dict2.keys())
#Iterate and print key‑ value pairs from {'x': 10, 'y': 20}.
#Tip: Use for k, v in d.items().
dict3={'x':10,'y':20}
for k,v in dict3.items():
    print(k,v)
#Use get() to safely read key 'score' from an empty dictionary.
#Tip: Use d.get('score', default_value).
dict4={}
print(dict4.get('score',20))
#Create a dictionary from two lists: keys = ['a','b'], values = [1,2].
#Tip: Use dict(zip(keys, values))
keys=['a','b']
values=[1,2]
print(dict(zip(keys,values)))
