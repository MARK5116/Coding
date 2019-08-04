#coding:utf-8

#如何求数组中绝对值最小的数

def binaryFind(arr):
    n = len(arr)
    left = 0
    right = n-1
    while left < right:
        mid = (left+right+1) / 2
        if arr[mid] == 0:
            return arr[mid]
        elif arr[mid] > 0:
            if arr[mid-1]==0:
                return arr[mid-1]
            elif arr[mid-1] < 0:
                if abs(arr[mid-1]) > arr[mid]:
                    return arr[mid]
                else:
                    return arr[mid-1]
            else:
                right = mid
        else:
            if arr[mid+1]==0:
                return arr[mid+1]
            elif arr[mid+1] > 0:
                if abs(arr[mid+1]) > arr[mid]:
                    return arr[mid]
                else:
                    return arr[mid+1]
            else:
                left = mid


def findMin(arr):
    n = len(arr)
    if arr[0] >= 0:
        return arr[0]
    elif arr[-1] <= 0:
        return arr[-1]
    else:
        mins = binaryFind(arr)
        return mins
    

if __name__=="__main__":
    arr = [-10,-5,-2,-1,7,15,50]
    mins = findMin(arr)
    print mins
