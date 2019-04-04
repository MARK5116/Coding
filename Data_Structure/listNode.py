#coding:utf-8

#如何实现链表的逆序
class LNode:
    def __init__(self, x, p=None):
        self.data=x      #数据域
        self.nxet=p   #下一个结点的引用
if __name__=="__main__":
    i = 1
    #链表头结点
    head = LNode(0) 
    #head.next = None
    #tmp = None
    cur = head
    #构造单链表
    while i < 8:
        tmp = LNode(i)
        #tmp.data = i
        #tmp.next = None
        cur.next = tmp
        cur = cur.next
        i += 1 
    print("逆序前：")
    print(cur.data)
    while cur != None:
       print(cur.data)
       cur = cur.next
