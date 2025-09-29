list = [1,2,3,4,5]

# for x in list:
#     print(x, end=' ')
print(list)
list.append(6)
print(list)
list.remove(6)
print(list)
list.insert(0, 6)
print(list)

"""
    list.copy(): creates static copy
    list = list2: creates reference copy (changes made to original are reflected)
"""
n = len(list)
for i in range(0, 4, 2):
    print(i, end=' ')