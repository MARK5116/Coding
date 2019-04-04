#coding:utf-8

#如何查找元素中元素的最大值和最小值

#方法一：暴力法（首先任意定义一个MAX和MIN，然后遍历整个数组中每个元素，分别与MAX和MIN比较）
#时间复杂度：O(N)

#方法二：分治法 （将数组俩俩分组，把较小的放到左边，较大的放大右边，然后从左边找最小元素，从右边找最大元素）
class MaxMin:
    def __new__(self):
        self.max = None
        self.min = None 
    def getMax(self):
        return self.max
    def getMin(self):
        return self.min
    def GetMaxAndmin(self,arr):
        n = len(arr)
        if n == 0:
            return None
        self.max = arr[0]
        self.min = arr[0]
        i = 0
        #俩俩分组，把较小的放到左半部分，把较大的放到右半部分
        while i < n-1:
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
            i += 2
        #在左半部分找最小值
        self.min = arr[0]
        i = 2
        while i < n:
            if self.min > arr[i]:
                self.min = arr[i]
            i +=2
        #在右半部分找最大值
        self.max = arr[1]
        i = 3
        while i < n:
            if self.max < arr[i]:
                self.max = arr[i]
            i += 2
        if n%2 == 1:
            if self.max < arr[n-1]:
                self.max = arr[n-1]
            if self.min > arr[n-1]:
                self.min = arr[n-1]

if __name__=="__main__":
    arr = [7,3,19,40,4,7,1]
    m = MaxMin()
    m.GetMaxAndmin(arr)
    max = m.getMax()
    min = m.getMin()
    print("max:",max)
    print("min:",min)


