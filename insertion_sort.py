l=[5,8,9,2,45,6,34,87]
l1=len(l)
for j in range(1,l1):
    for i in range(j-1,-1,-1):
        if(l[i]>l[i+1]):
            l[i],l[i+1]=l[i+1],l[i]
        else:
            break
print(l)