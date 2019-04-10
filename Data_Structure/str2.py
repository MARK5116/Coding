#coding:utf-8

#如何求两个字符串的最长公共子字符串
#方法一：动态规划法
def getMaxSubStr(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    sb = ''
    maxs = 0 #用来记录最长公共子字符串的长度
    maxI = 0 #用来记录最长公共子字符串的最后一个字符的位置
    #记录公共子字符串的长度信息
    M = [([None]*(len1+1)) for i in range(len2+1)]
#    print(M)
    i = 0
    while i < len1+1:
        M[i][0] = 0
        i += 1
    j = 0
    while j < len2+1:
        M[0][j] = 0
        j += 1
    i = 1
    while i < len1+1:
        j = 1
        while j < len2+1:
            if list(str1)[i-1] == list(str2)[j-1]:
                M[i][j] = M[i-1][j-1] + 1
                if M[i][j] > maxs:
                    maxs = M[i][j]
                    maxI = i
            else:
                M[i][j] = 0
            j += 1
        i += 1
    #找出公共子字符串
    i = maxI - maxs
    while i < maxI:
        sb = sb + list(str1)[i]
        i += 1
    return sb


if __name__=="__main__":
    str1 = "abccade"
    str2 = "dgcadde"
    print getMaxSubStr(str1, str2)
