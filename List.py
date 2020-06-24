#78 Write a Python program to split a given list into two parts where the length of the first part of the list is given.

x=[1, 1, 2, 3, 4, 4, 5, 1]

result=x[:3]

result2=x[3:]

print(result)
print(result2)


# 74. Write a Python program to pack consecutive duplicates of a given list elements into sublists. Go to the editor

from itertools import groupby
l1=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
l2=[]

for k,j in groupby(l1):
    l2.append(list(j))
print(l2)


# 73. Write a Python program to remove consecutive duplicates of a given list. Go to the editor

from itertools import groupby
l1=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
l2=[]
for k,j in groupby(l1):
    l2.append(k)
    
print(l2)

# 72. Write a Python program to flatten a given nested list structure

new_list=[]
def flat_list(x):
    for item in x:
        if type(item)==list:
            flat_list(item)
        else:
            new_list.append(item)
    return new_list
                
    
flat_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])




