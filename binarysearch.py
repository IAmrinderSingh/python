def binarysearch(start,end,ele,arr):
    mid=start+(end-start)//2
    if arr[mid]==ele:
        return ele
    elif arr[mid]>ele:
        return binarysearch(start,mid-1,ele,arr)
    elif arr[mid]<ele:
        return binarysearch(mid+1,end,ele,arr)
    else:
        return -1
arr=[0,1,2,3,4,5,6,7,8,9,10]
ele=int(input("Enter an number to search in array 0-10: "))
print(binarysearch(0,len(arr)-1,ele,arr))