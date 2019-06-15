l=[5,8,9,2,45,6,34,87]
l1=len(l)
for j in range(0,l1-1):
    min=j
    for i in range(j+1,l1):
        if(l[min]>l[i]):
            min=i
    if(min!=j):
        l[j],l[min]=l[min],l[j]
print(l)        