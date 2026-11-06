#Create a set from [1, 2, 2, 3] and print it.
#Tip: Use set(list).
list1=[1,2,2,3]
print(set(list1))
#Add element 4 to the set {1, 2, 3}.
#add()
set1={1,2,3}
set1.add(4)
print(set1)
#Remove element 2 from the set {1, 2, 3}
#use remove()
set2={1,2,3}
set2.remove(2)
print(set2)
#Check if 5 is in the set {1, 3, 5}.
set3={1,3,5}
if 5 in set3:
    print("Found")
else:
    print("Not Found")
#Clear all elements from the set {1, 2, 3}.
set4={1,2,3}
set4.clear()
print(set4)
#Create a set {'a', 'b'} and add 'c' only if it’s missing.
#Tip: Check membership first: if 'c' not in s:.
set5={'a','b'}
if 'c' not in set5:
    set5.add('c')
    print(set5)
#Convert list ['a', 'a', 'b'] into a set to remove duplicates.
#Tip: Casting removes duplicates automatically.
list2=['a','a','b']
print(set(list2))
#Create two sets and print their union.
#Tip: Use set1 | set2.
set6,set7={1,2,3},{4,5,6}
print(set6 | set7)
#Create two sets and print their intersection.
#Tip: Use set1 & set2.
set8,set9={7,8,9},{10,11,12}
print(set8.intersection(set9))
#you can also use print(set8 & set9)
