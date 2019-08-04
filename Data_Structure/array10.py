#coding:utf-8

#如何求数组连续的最大和
def maxSubArr(arr):
    n = len(arr)
    All = [None]*n
    End = [None]*n
    End[0] = arr[0]
    All[0] = arr[0]
    i = 1
    while i < n:
        End[i] = max(End[i-1]+arr[i], arr[i])
        print End[i-1],End[i] 
        print arr[i]
        All[i] = max(All[i-1], End[i])
        print All[i-1],All[i]
        i += 1
    return All[n-1]

if __name__=="__main__":
    #arr = [1,-2,4,8,-4,7,-1,-5]
    arr = [1,-2,4,8,-4,7]
    max_sum = maxSubArr(arr)
    print max_sum
