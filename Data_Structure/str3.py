#coding:utf-8

#如何实现字符串的反转

def reverseStr(str):
   str_list = list(str)
   i = 0
   j = len(str_list) - 1
   while i < j:
       temp = str_list[i]
       str_list[i] = str_list[j]
       str_list[j] = temp
       i += 1
       j -= 1
   return ''.join(str_list)

if __name__=="__main__":
    str = 'abcdef'
    print str
    reverse_str = reverseStr(str)
    print reverse_str
