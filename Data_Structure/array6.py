#coding:utf-8

#如何找出数组中第K小的数

def findSmallK(arr, low, high, k):
    i = low
    j = high
    while i < j:
        while i < j and arr[i] <= arr[j]:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
        while i < j and arr[i] <= arr[j]:
            i +=1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
            j -=1
#        findSmallK(arr,low,i-1,k)
#        findSmallK(arr,i+1,high,k)
#    return arr
    if i+1 < k:
        return findSmallK(arr,i+1,high,k)
    elif i+1 > k:
        return findSmallK(arr,low,i-1,k)
    else:
        return arr[i]
        

if __name__=="__main__":
    arr = [4,0,1,0,2,3] 
    print(arr)
    min_k = findSmallK(arr, 0, 5, 3)
    print(min_k)
