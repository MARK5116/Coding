#coding:utf-8

#如何找出数组中出现奇数次的数
#数组中有N+2个数，其中N个数出现偶数次，2个数出现奇数次，请用O(1)的空间复杂度，找出这两个数。

#方法一：字典计数法
#空间复杂度和时间复杂度均为O(n)
def get2Num(arr):
    n = len(arr)
    if arr == None or n < 1:
        return None
    count_dict = {}
    for i in range(n):
        if arr[i] in count_dict:
            count_dict[arr[i]] += 1
        else:
            count_dict[arr[i]] = 1
    num = []
    for key in count_dict:
        if count_dict[key] % 2 == 1:
            num.append(key)
    return num

if __name__=="__main__":
    arr = [3,5,6,6,5,7,2,2]
    num = get2Num(arr)
    print(num)
