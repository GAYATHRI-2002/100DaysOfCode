list1 =[2,1,4,3,5,7,6,8]
list2 = []
for i in list1:
    if i % 2 == 0:
        list1.remove(i)
        list2.append(i) 

print("The updated list:",list1)
print("The removed:",list2) 