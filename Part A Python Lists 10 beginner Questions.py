#Create a list nums = [3, 1, 4, 1, 5] and print the first and last elements.
#Tip: Use nums[0] and nums[-1].
nums=[3,1,4,1,5]
print(nums[0])
print(nums[-1])
#Find the length of the list colors = ['red', 'blue', 'green'].
#Tip: Use len(colors).
colors=['red','blue','green']
print(len(colors))
#Append 'yellow' to the list colors = ['red', 'blue'].
#Tip: Use append()
colors1=['red','blue']
colors1.append('yellow')
print(colors1)
#Insert 'orange' at index 1 in fruits = ['apple', 'banana'].
#Tip: Use insert(index, value).
fruits=['apple','banana']
fruits.insert(1,'orange')
print(fruits)
#Remove 'banana' from fruits = ['apple', 'banana', 'grapes'].
#Tip: Use remove(value)
fruits1=['apple','banana','grapes']
fruits1.remove('banana')
print(fruits1)
#Pop the last element from items = [10, 20, 30] and print the popped value.
#Tip: Call items.pop().
items=[10,20,30]
value=items.pop(2)
print(value)
print(items)
#Check if 3 is in the list nums = [1, 2, 3, 4].
#Tip: Use the in operator.
nums=[1,2,3,4]
if 3 in nums:
    print(True)
else:
    print(False)
#Print the slice [2, 3] from the list [0, 1, 2, 3, 4].
#Tip: Use slicing: a[2:4].
list1=[0,1,2,3,4]
print(list1[2:4])
#Replace the element at index 1 in a = [5, 10, 15] with 12.
#Tip: Use assignment: a[1] = 12.
a=[5,10,15]
a[1] =12
print(a)
#Count how many times 2 appears in [1, 2, 2, 3, 2].
#Tip: Use list.count(value).
list2=[1,2,2,3,2]
print(list2.count(2))
