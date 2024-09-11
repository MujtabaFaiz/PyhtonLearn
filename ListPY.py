#========================================List
mylist =["AA","BB","CC","CC"]
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
#print(mylist)
#print(len( mylist))
#print(type( list3))

#===============================list() Constructor
listcon = ("apple", "banana", "cherry")
#print(listcon)
#==================================Python Collections (Arrays)
#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.


#====================================Access List Items
thislist = ["apple", "banana", "cherry"]
#print(thislist[1])
print(thislist[-1])
#---------------------------Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# print(thislist[5:])
# print(thislist[:5])
# print(thislist[-4:-1]) #Range of Negative Indexes
#if "apple" in  thislist:
    #print("Exist")

#=======================================Change List Items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
#thislist[1]="blackcurrant"
#print(thislist)
#thislist[1:3] = ["blackcurrant", "watermelon"]
#print(thislist)

#-------------------Insert Items
#thislist.insert(2,"Mujtaba")
#print(thislist)

#==================================Add List Items
thislist = ["apple", "banana", "cherry"]
#thislist.append("orange")
#print(thislist)
#--------------------Extend List
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
#print(thislist)      

#================================== Remove List Items
#thislist.remove("apple")
#thislist.pop(2)
#thislist.pop()
#del thislist[0]
#del thislist
#thislist.clear()
#print(thislist)
#================================== Loop List Items
#for x in thislist:
    # print()
#Loop Through the Index Numbers
# for x in range(len(thislist)):
#     print(thislist[x])

#============================Using a While Loop
# i = 0
# while i<len(thislist):
#     print(thislist[i])
#     i = i+1

#============================Looping Using List Comprehension
#[print(x) for x in thislist]
newlist =[]
# for x in thislist:
#     if "a" in x:
#         newlist.append(x)


# newlist1 = [x for x in thislist if "a" in x] 
# #print(newlist1)
# newlist1 = [x for x in thislist if x != "apple"] 
# print(newlist1)             
# newlist = [x for x in thislist]
# print(newlist)
# newlist = [x for x in range(3)]
# print(newlist)
# newlist = [x.upper() for x in thislist]
# print(newlist)
# newlist = ['hello' for x in thislist]
# print(newlist)
# newlist = [x if x != "banana" else "orange" for x in thislist]
# print(newlist)

#================================== Sort List
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
#print(thislist)
#------------------------Sort Descending
thislist.sort(reverse=True)
#print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 300]
thislist.sort(key = myfunc)
#print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
#print(thislist)

#================================ Copy Lists
mylst = thislist.copy();
#print(mylst)
mylst = list(thislist)
#print(mylst)
mylst = thislist[:]
#print(mylst)

#========================================== Join Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
lst3 = list1 +list2
#print(lst3)

for x in list1:
  list2.append(x)

#print(list2)

list1.extend(list2)
#print(list1)

#==================================Tuples
mytuple = ("apple", "banana", "cherry") #A tuple is a collection which is ordered and unchangeable.
# Ordered not change
# Unchangeable
# Allow Duplicates
thistuple = ("apple",)
#print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
#print(type(thistuple))

#==================================Set
myset = {"apple", "banana", "cherry"}
#A set is a collection which is unordered, unchangeable*, and unindexed.
#Duplicates Not Allowed
myset.add("orange")

myset.update(mylist) # add set
myset.discard("banana") 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
set3 = set1 | set2
print(set3)

myset = set1.union(set2, set3)
print(myset)
set1.update(set2)
print(set1)