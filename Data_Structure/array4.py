#coding:utf-8

#如何找出数组中丢失的数
#方法一：累加求和法
def getNum(arr):
    n = len(arr)
    if n==0:
        return -1
    result_sum = 0
    for i in range(n):
        result_sum += arr[i]
    all_sum = 0
    for i in range(n+2):
        all_sum += i
    return all_sum - result_sum

if __name__=="__main__":
    arr = [1,4,3,2,7,5]
    num = getNum(arr)
    print(num)
