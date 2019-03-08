#Function to takes in a dataset and normalizes it
#Define Lists of Elements
list_a = ['a','b','c','d','e']
list_b = [1,2,3,4,5]

#Regular For Loop
l = {}
for i in range(len(list_a)):
    l[list_a[i]] = list_b[i]
print(l)

#Dictionary Comprehension
l = {list_a[i]:list_b[i] for i in range(len(list_a))}
print(l)

#Using Zip
l = dict(zip(list_a, list_b))
print(l)
