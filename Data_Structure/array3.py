#coding:utf-8

#如何找出旋转数组的最小元素
#二分查找法
def getMin(arr):
    n = len(arr)
    if n < 2:
        return arr
    left = 0
    right = n-1
    while right > left + 1:
       mid = (left + right)/2
       if arr[left] > arr[mid]:
           right = mid
       if arr[left] <= arr[mid]:
           left = mid
    return arr[right]

if __name__=="__main__":
    arr = [5,6,1,2,3,4]
    min_num = getMin(arr)
    print(min_num)
