def find_index(arr,k,n):
    for i in range(n):
        if arr[i]==k:
            return print("fun")
        elif arr[i]>k:
            return i
    return n

arr=[1,25,48,458,790]
k = 4588
find_index(arr,k,len(arr))
            