
def quick_sort(l,low,high):
    if(low < high):
        pi=partition(l,low,high)
        quick_sort(l,low,pi-1)
        quick_sort(l,pi+1,high)
def partition(l,low,high):
    i=low-1
    pivot=l[high-low//2]
    for j in range(low,high):
        if(l[j]<=pivot):
            i=i+1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[high]=l[high],l[i+1]
    return(i+1)        

l=[5,8,9,2,45,6,34,87]
l1=len(l)
quick_sort(l,0,l1-1)
print("The Sorted list is\n")
print(l)