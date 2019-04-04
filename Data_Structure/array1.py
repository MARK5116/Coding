#coding:utf-8


#如何找出数组中唯一重复的元素
#方法一：Hash法:缺点是增加了辅助空间   (构造链表)
#时间复杂度：O(N)  空间复杂度：O(N)
def findDup(arr):
    n = len(arr)
    if len(arr) <= 1:
        return -1
    hashTable = {}
    i = 0
    for i in range(n):
        if arr[i] in hashTable:
            hashTable[arr[i]] += 1
            return arr[i]
        else:
            hashTable[arr[i]] = 0

#方法二：累加求和法

#方法三：异或法
#时间复杂度：O(N) 没有构造辅助空间
def findDup3(arr):
    n = len(arr)
    if n <= 1:
        return -1
    result = 0
    for i in range(n):
        result ^= arr[i]
    for i in range(1,n):
        result ^= i
    return result

if __name__=="__main__":
    arr = [1,3,4,2,5,2]
    num = findDup3(arr)
    print(num)


