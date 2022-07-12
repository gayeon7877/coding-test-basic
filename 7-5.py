n=int(input())
arr=list(map(int,input().split()))
m=int(input())
arr1=list(map(int,input().split()))

arr.sort();

def binary_search(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2

    if array[mid]==target:
        return mid

    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)

    else:
        return binary_search(array,target,mid+1,end)

for i in arr1:
    result=binary_search(arr,i,0,n-1)
    if result!=None:
        print('yes',end=' ')
    else:
        print('no',end=' ')

