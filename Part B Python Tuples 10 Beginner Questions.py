#Create a tuple t = (10, 20, 30) and print the second element.
#Tip: Tuples use indexing: t[1].
t=(10,20,30)
print(t[1])
#Find the length of tuple ('a', 'b', 'c')
t1=('a','b','c')
print(len(t1))
#Unpack the tuple (4, 5) into variables x and y.
#Tip: x, y = (4, 5).
t2=(4,5)
x,y=(t2)
print(x)
print(y)
#Check if 'b' is in the tuple ('a', 'b', 'c').
t3=('a','b','c')
if 'b' in t3:
    print(True)
else:
    print(False)
#Create an empty tuple and print its type.
t4=()
print(type(t4))
#Concatenate (1, 2) and (3, 4) into a new tuple.
t5,t6=(1,2),(3,4)
print(t5 + t6)
#Repeat (7,) three times.
t7=(7,)
print(t7 * 3)
#Find the index of 2 in (1, 2, 3, 2).
#Tip: Use index() method.
t8=(1,2,3,2)
print(t8.index(2))
#Count how many times 2 appears in (1, 2, 3, 2).
t9=(1,2,3,2)
print(t9.count(2))
#Create a single‑ element tuple containing the value 5.
#Tip: Remember to use a comma: (5,).
t10=(5,)

