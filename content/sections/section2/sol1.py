#Makes a list of all the even numbers from 0 to 20 with a For Loop
l = []
for i in range(20):
    if i%2==0:
        l.append(i)
print(l)
