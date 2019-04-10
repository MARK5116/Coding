#coding:utf-8

#如何求两个元素的最小距离
def minDistance(arr,num1,num2):
    n = len(arr)
    if n == 0:
        return None
    lastPos1 = -1 #上次遍历到num1的位置
    lastPos2 = -1 #上次遍历到num2的位置
    mindis = 2**32   #num1和num2之间的距离
    i = 0
    while i < n:
        if arr[i] == num1:
            lastPos1 = i
            if lastPos2 != -1:
                dis = abs(lastPos2 - lastPos1)
                if dis < mindis:
                    mindis = dis
        if arr[i] == num2:
            lastPos2 = i
            if lastPos1 != -1:
                dis = abs(lastPos2 - lastPos1)
                if dis < mindis:
                    mindis = dis
        i += 1
    return mindis

if __name__=="__main__":
    arr = [4,5,6,4,7,4,6,4,7,8,5,6,4,3,10,8]
    num1 = 4
    num2 = 8
    print minDistance(arr,num1,num2)
