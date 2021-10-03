def binarysearch(start,end,ele,arr):
    if end>=start:
        mid=start+(end-start)//2
        if arr[mid]==ele:
            return ele
        elif arr[mid]>ele:
            return binarysearch(start,mid-1,ele,arr)
        else:
            return binarysearch(mid+1,end,ele,arr)
    else:
        return -1
lenarr=int(input("Enter length of array: "))
arr=[]
for i in range(lenarr):
    arr.append(int(input(f"Enter [{i}] element: ")))
ele=int(input("Enter an number to search in array : "))
result=binarysearch(0,len(arr)-1,ele,arr)
if (result==-1):
    print("Number not exist")
else:
    print("Element is :",result)