l=[5,8,9,2,45,6,34,87]
l1=len(l)
i=0
j=0
for j in range(0,l1-1):
    for i in range(0,l1-1-i):
        if(l[i]>l[i+1]):
            l[i],l[i+1]=l[i+1],l[i]
print(l)