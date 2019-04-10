#coding:utf-8

#如何求一个字符串的所有排列
def permutation(str, start):
    if str == None:
        return
#    print(len(str))
    #完成全排序后输出当前排列的字符串
    if start == len(str)-1:
        #print(str)
        print(''.join(str))
    else:
        i = start 
        while i < len(str):
            #交换start和i所在位置的字符
            str[start],str[i] = str[i],str[start]
            #固定一个字符，对剩余字符进行全排列
            permutation(str, start+1)
            #还原start和i所在位置的字符
            str[start],str[i] = str[i],str[start]
            i += 1

def permutation_transe(s):
    str_list = list(s)
    print(str_list)
    permutation(str_list, 0)


if __name__=="__main__":
    s = "abc"
    permutation_transe(s)
