mylist=[25, 3.14, "python", True, 99, 6.14]
#Reverse a list in Python
#1st method
mylist.reverse()
print(mylist)
#2nd method
print(mylist[::-1])
#Turn every item of a list into its square
mylist1=[5,6,7,8,9,10]
mylist2=[]
for i in mylist1:
    mylist2.append(i ** 2)
print(mylist2)
#Remove empty strings from the list of strings
mylist3=["Ali","","Ahmad","","Sara",""]
newlist=[]
for i in mylist3:
    if i!="":
        newlist.append(i)
print(newlist)
#Add new item to list after a specified item
mylist4=["ali","ahmad","sara"]
mylist4.insert("ahmad"+1,"usman")
#Replace list’s item with new value if found
mylist5=["ali","ahmad","sara"]
if "ahmad" in mylist5:
    index=mylist5.index("ahmad")
    mylist5[index]="usman"
print(mylist5)

