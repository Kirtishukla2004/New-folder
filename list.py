"""
list is an  where we can store multiple types of elements
list is ordered (indexed ) sequence ordered elements it a mutabale type
list is not like an array 
it can have elements of diffrent datatypes in one variable like int ,string,float
for example 
list starts with brakets and seprated with commas(,)
list=['kirti',18,'delhi]
this is list 
for printing elements of list 
print(list)
///output:[kirti,18,delhi]
we have many inbuilt function sof list like 
"""
list=['kiriti',18,'delhi']
list1=[1,2,3,4,5,6]
list4=[6,5,4,8,2,1]
print(list)
print("lenght of list ",len(list))
list.insert(2,99)
print(list)
a=[7,6]
list.extend(a)
print(list)
list.append(20)
print(list)
 #concatination
print(list+list1)
list2=["hello"]
print(list2*5)
print(list)
list.pop()
print(list)
list.remove(18)
print(list)
print(list.count(1))#returns false as it is not present
print(list1.index(5))
list.reverse()
print(list)

list4.sort()
print(list4)
print(min(list1))
print(max(list4))
print(sum(list4))