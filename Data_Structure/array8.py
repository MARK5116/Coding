#coding:utf-8

#如何求最小三元组的距离

def minDistance(a,b,c):
    len1 = len(a)
    len2 = len(b)
    len3 = len(c)
    i = 0
    j = 0
    k = 0
    minDis = 2**32
    maxDis = 0
    while i<len1 and j<len2 and k<len3:
        maxDis = max(abs(a[i] - b[j]), abs(a[i] - c[k]), abs(b[j] - c[k]))    
        if maxDis < minDis:
            minDis = maxDis
            if a[i] - b[j] < 0 and a[i] - c[k] < 0:
                i += 1
            elif b[j] - c[k] < 0 and b[j] - a[i] < 0:
                j += 1
            elif c[k] - a[i] < 0 and c[k] - b[j] < 0:
                k += 1
        else:
            break
    return minDis


if __name__=="__main__":
    a = [3,4,5,7,15]
    b = [10,12,14,16,17]
    c = [20,21,23,24,37,40]
    minDis = minDistance(a,b,c)
    print minDis
