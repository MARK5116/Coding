# 数组

## leetcode

26. Remove Duplicates from Sorted Array

https://blog.csdn.net/qq_28119401/article/details/52972467

27. Remove Element

https://blog.csdn.net/qq_28119401/article/details/52972484

35. Search Insert Position



53. Maximum Subarray

https://blog.csdn.net/zl87758539/article/details/51676108

# 字符串

## leetcode

38. Count and Say

<https://blog.csdn.net/Lucy_R/article/details/79003142>

# 二叉树

### 三种遍历方式

![avatar](/Users/didi/Desktop/屏幕快照 2019-04-09 下午11.17.38.png)

```python
#coding=utf-8

class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        if self.root.elem == -1:        #如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  #此结点的子树还没有齐。
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)     #如果该结点存在右子树，将此结点丢弃。


    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print root.elem,
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)


    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.middle_digui(root.lchild)
        print root.elem,
        self.middle_digui(root.rchild)


    def later_digui(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print root.elem,


    def front_stack(self, root):
        """利用堆栈实现树的前序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:  #从根节点开始，一直找它的左子树
                print node.elem,
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()         #while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.rchild           #开始查看它的右子树


    def middle_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                #从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()       #while结束表示当前节点node为空，即前一个节点没有左子树了
            print node.elem,
            node = node.rchild         #开始查看它的右子树


    def later_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:             #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:              #将myStack2中的元素出栈，即为后序遍历次序
            print myStack2.pop().elem,


    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print node.elem,
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)
                           
if __name__ == '__main__':
    """主函数"""
    elems = range(10)           #生成十个数据作为树节点
    tree = Tree()               #新建一个树对象
    for elem in elems:                  
        tree.add(elem)          #逐个添加树的节点

    print '队列实现层次遍历:'
    tree.level_queue(tree.root)

    print '\n\n递归实现先序遍历:'
    tree.front_digui(tree.root)
    print '\n递归实现中序遍历:' 
    tree.middle_digui(tree.root)
    print '\n递归实现后序遍历:'
    tree.later_digui(tree.root)

    print '\n\n堆栈实现先序遍历:'
    tree.front_stack(tree.root)
    print '\n堆栈实现中序遍历:'
    tree.middle_stack(tree.root)
    print '\n堆栈实现后序遍历:'
    tree.later_stack(tree.root)

```

# 链表

## 链表的创建以及基本操作

```python
class LNode(object):
    #结点初始化函数, p 即模拟所存放的下一个结点的地址
    #为了方便传参, 设置 p 的默认值为 0 
    def __init__(self, data, p=0):
        self.data = data
        self.next = p

class LinkList(object):
    def __init__(self):
        self.head = None

    #链表初始化函数, 方法类似于尾插
    def initList(self, data):
        #创建头结点
        self.head = LNode(data[0])
        p = self.head
        #逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = LNode(i)
            p.next = node
            p = p.next

    #链表判空
    def isEmpty(self):
        if self.head.next == 0:
            print "Empty List!"
            return 1
        else:
            return 0

    #取链表长度
    def getLength(self):
        if self.isEmpty():
            exit(0)

        p = self.head
        len = 0
        while p:
            len += 1
            p = p.next
        return len

    #遍历链表
    def traveList(self):
        if self.isEmpty():
            exit(0)
        print '\rlink list traving result: ',
        p = self.head
        while p:
            print p.data,
            p = p.next

    #链表插入数据函数
    def insertElem(self, key, index):
        if self.isEmpty():
            exit(0)
        if index<0 or index>self.getLength()-1:
            print "\rKey Error! Program Exit."
            exit(0)

        p = self.head
        i = 0
        while i<=index:
            pre = p
            p = p.next
            i += 1

        #遍历找到索引值为 index 的结点后, 在其后面插入结点
        node = LNode(key)
        pre.next = node
        node.next = p

    #链表删除数据函数
    def deleteElem(self, index):
        if self.isEmpty():
            exit(0)
        if index<0 or index>self.getLength()-1:
            print "\rValue Error! Program Exit."
            exit(0)

        i = 0
        p = self.head
        #遍历找到索引值为 index 的结点
        while p.next:
            pre = p
            p = p.next
            i += 1
            if i==index:
                pre.next = p.next
                p = None
                return 1

        #p的下一个结点为空说明到了最后一个结点, 删除之即可
        pre.next = None


#初始化链表与数据
data = [1,2,3,4,5]
l = LinkList()
l.initList(data)            
l.traveList()

#插入结点到索引值为3之后, 值为666
l.insertElem(666, 3)
l.traveList()

#删除索引值为4的结点
l.deleteElem(4)
l.traveList()
```

## leetcode

21. Merge Two Sorted Lists

