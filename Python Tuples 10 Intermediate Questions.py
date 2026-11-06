#1.	Convert the list [1, 2, 3, 4] into a tuple and then unpack it into four variables.
#Tip: Use tuple() and simple unpacking.
list1=[1,2,3,4]
tup1=tuple(list1)
a,b,c,d=tup1
print(a)
print(b)
print(c)
print(d)
#2.	Given t = (('a', 1), ('b', 2), ('c', 3)), create a list of all second elements.
#Tip: Use a comprehension: x[1].
tup2=(('a',1),('b',2),('c',3))
list2=[]
for x in tup2:
    list2.append(x[1])
print(list2)
#3.	Write a function that returns multiple values (sum, min, max) using a tuple.
#Tip: Return (..., ..., ...) and unpack later.
def stats(numbers):
    return sum(numbers),max(numbers),min(numbers)
nums=(3,1,4,1,5)
sum_value,max_value,min_value=stats(nums)
print(sum_value)
print(max_value)
print(min_value)
#4.	Combine two tuples (1, 2, 3) and (4, 5) then convert the result to a list.
#Tip: Use + to join them.
tuple1=(1,2,3)
tuple2=(4,5)
newtuple=tuple1+tuple2
print(list(newtuple))
#5.	Given a tuple of numbers, find the element with the highest frequency.
#Tip: Loop through unique items using set(t).
tuple_of_numbers=(23,45,23,56,98,87,45,55,92,14)
highest_count=0
most_frequent="none"
for x in set(tuple_of_numbers):
    count=tuple_of_numbers.count(x)
    if count>highest_count:
        highest_count=count
        most_frequent=x
print(most_frequent)
#6.	Check if two tuples contain the same elements regardless of order.
#Tip: Compare sorted(tuple) values.
tuple3=(45,67,98)
tuple4=(78,34,98)
sorted(tuple3)
sorted(tuple4)
if sorted(tuple3)==sorted(tuple4):
    print("Same")
else:
    print("Not Same ")
#7.	Extract the last three items from a tuple using slicing.
#Tip: Use negative indexing: t[-3:].
tuple5=(24,"hamza",False,6.20,19.87,"lee")
print(tuple5[-3:])
#8.	Concatenate a tuple with itself three times (repeat operation).
#Tip: Use tuple * 3.
tuple5=(24,"hamza",False,6.20,19.87,"lee")
print(tuple5 * 3)
#9.	Convert a nested tuple ((1,2),(3,4)) into a flat tuple (1,2,3,4).
#Tip: Use a comprehension inside tuple().
tuple6=((1,2),(3,4))
flat_tuple=tuple(x for item in tuple6 for x in item)
print(flat_tuple)
#10.	Store coordinates in tuples and calculate the Manhattan distance.
#Tip: Use absolute difference formula: abs(x1-x2) + abs(y1-y2).
point1=(2,3)
point2=(5,7)
x1,y1=point1
x2,y2=point2
distance=abs(x1-x2) + abs(y1-y2)
print("Manhattan distance:",distance)







