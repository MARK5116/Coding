#  二分查找

查找key是否存在数组中，数组必须有序。

```python
def rank(key,array):
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        mid = lo + (lo+hi)/2
        if key < array[mid]:
            hi = mid - 1
        elif key > array[mid]:
            lo = mid + 1
        else:
            return mid
    return -1
```



# 排序

## 选择排序

从前往后排。

时间复杂度：O(n*n)

空间复杂度：O(1)

```python
def select_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[min] > arr[j]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]

    return arr
```

## 插入排序

时间复杂度：最好：O(n)   最坏：O(n*n)    平均：O(nn)

空间复杂度：O(1)

```python
#插入排序
def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > key:
                arr[j+1] = arr[j]
                arr[j] = key
            j -= 1
    return arr
```

## 冒泡排序

从后往前排。

时间复杂度：最好：O(n)   最坏：O(n*n)    平均：O(nn)

空间复杂度：O(1)

```python
#时间复杂度：O(n*n)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
```

## 归并排序

利用递归与分治技术

时间复杂度：每一趟归并的时间复杂度为O(n)，二路递归的最好、最坏和平均的时间复杂度为nlogn。

```python
def merge(left, right):
    i,j = 0,0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j +=1       
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    num = n/2
    left = merge_sort(arr[:num])
    right = merge_sort(arr[num:])
    return merge(left, right)
```

## 快排

**时间复杂度分析：** https://www.cnblogs.com/surgewong/p/3381438.html

最坏情况：

当基数值不能很好地分割数组，即基准值将数组分成一个子数组中有一个记录，而另一个子组组有 n -1 个记录时，下一次的子数组只比原来数组小 1，这是快速排序的最差的情况。如果这种情况发生在每次划分过程中，那么快速排序就退化成了冒泡排序，其时间复杂度为O(n2)。

最佳情况：

如果基准值都能讲数组分成相等的两部分，则出现快速排序的最佳情况。

快排是对冒泡排序的改进。

改进点：在冒泡排序中是对相邻位置上的比较和移动，每次交换只能前移或者后移一个单位；快排中，记录的比较和移动是从两端向中间进行，关键码较大的记录一次可以从前端移动到后端，记录移动距离较远，较少了总的比较次数和移动次数。

快速排序又称为分区交换排序。

基本思想：首先选择一个轴值（比较的基准点），将待排序记录分割成独立的两部分，左侧记录的关键码都小于或者等于轴值，右侧则都大于或者等于轴值，然后分别对两部分重复上述过程，直至整个序列有序。

进行一次划分过程：

（1）初始化：一般取序列第一个数作为基准点，设置两个参数i和j，分别指示与基准点比较的左侧位置和右侧位置。

（2）右侧扫描过程：将基准点记录与j指向的记录进行比较，如果j指向的记录大于基准，则j前移一个位置（j--），继续右侧扫描，如果右侧记录小于基准，则将j指向的记录赋予i指向的位置，并将i右移一位。

（3）左侧扫描过程：将基准点记录与i指向的记录进行比较，如果i指向的记录小于基准，则i后移一个位置（i++），继续左侧扫描，如果左侧记录大于基准，则将i指向的记录赋予j指向的位置，并将j左移一位。

（4）重复2，3步骤，直至i和j指向同一个位置，即基准记录的位置。

举例：原序列为a=[23  13  49  6  31  19  28]

|    首先设置基准点key=a[0], i=0,  j=6 . 此时a[0]位置挖空。    |      |      |      |      |      |      |
| :----------------------------------------------------------: | ---- | ---- | ---- | ---- | ---- | ---- |
|                                                              | 13   | 49   | 6    | 31   | 19   | 28   |
|                              i                               |      |      |      |      |      | j    |
|                 右侧扫描，key<28, j前移一位                  |      |      |      |      |      |      |
|                                                              | 13   | 49   | 6    | 31   | 19   | 28   |
|                              i                               |      |      |      |      | j    |      |
|   Key>19,不符合条件，此时将j指向的值移到i位置。i右移一位。   |      |      |      |      |      |      |
|                              19                              | 13   | 49   | 6    | 31   |      | 28   |
|                                                              | i    |      |      |      | j    |      |
| 左侧扫描，key>13, i右移一位，key<49,将i位置移到j位置，j前移一位。 |      |      |      |      |      |      |
|                              19                              | 13   |      | 6    | 31   | 49   | 28   |
|                                                              |      | i    |      | j    |      |      |
|                 右侧扫描，key<31，j前移一位.                 |      |      |      |      |      |      |
|                              19                              | 13   |      | 6    | 31   | 49   | 28   |
|                                                              |      | i    | j    |      |      |      |
|       Key>6,不符合条件，将j位置的数移到i，i右移一位。        |      |      |      |      |      |      |
|                              19                              | 13   | 6    |      | 31   | 49   | 28   |
|                                                              |      |      | i，j |      |      |      |
|                  此时i=j,则将a[i]赋值key值                   |      |      |      |      |      |      |
|                              19                              | 13   | 6    | 23   | 31   | 49   | 28   |

```python
#时间复杂度O(nlogn)
#最坏时间复杂度：O(n*n)
def qsort(arr, low, high):
    i = low
    j = high
    while i < j:
        while i < j and arr[i] < arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i +=1
        while i < j and arr[i] < arr[j]:
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            j -=1
        qsort(arr, low, i-1)
        qsort(arr, i+1, high)
```

**思考：**

1. 一直一个数组，求第k大的数，要求时间复杂度最低。

## 堆排序

**堆的定义：**

堆是具有下列性质的二叉树：每个结点的值都小于或者等于其左右孩子结点的值（小根堆），或者每个结点的值都大于或者等于其左右孩子结点的值（大根堆）。

**基本思想：**

首先将待排序的记录序列构成一个堆，选出堆中所有记录的最大者即堆顶记录，		

然后将它从堆中移走（通常将堆顶记录和堆中最后一个记录交换），并将剩余的记录再调整成堆，

这样又找到了次大的记录，一次类推，直至堆中只有一个记录为止。

 **时间复杂度：**

堆排序的时间复杂度分为两个部分：一个是建堆的时候所耗费的时间，一个是进行堆调整的时候所耗费的时间。而堆排序则是调用了建堆和堆调整。 

刚刚在上面也提及到了，建堆是一个线性过程，从len/2-0一直调用堆调整的过程，相当于o(h1)+o(h2)+…+o(hlen/2)这里的h表示节点深度，len/2表示节点深度，对于求和过程，结果为线性的O（n） 

堆调整为一个递归的过程，调整堆的过程时间复杂度与堆的深度有关系，相当于lgn的操作。 

因为建堆的时间复杂度是O（n）,调整堆的时间复杂度是lgn，**所以堆排序的时间复杂度是O（nlgn）**

```python
#在堆中做结构调整，使得父节点的值大于子节点
def max_heapify(heap, heapsize, root):
    left = root*2+1
    right = left + 1
    larger = root
    if left < heapsize and heap[larger] < heap[left]:
        larger = left
    if right < heapsize and heap[larger] < heap[right]:
        larger = right
    #如果父节点的值小于左右子节点的值，则做对调调整
    if larger != root:
        heap[larger],heap[root] = heap[root],heap[larger]
        max_heapify(heap, heapsize, larger)
#构建一个堆，将堆中所有的元素重新排序
def build_max_heap(heap):
    heapsize = len(heap)
    #从后往前取数
    for i in range((heapsize-2)//2, -1, -1):
        max_heapify(heap, heapsize, i)
#堆排序
#将根结点取出与最后一位对调，对前面len-1个节点继续进行对调调整
def heap_sort(heap):
    build_max_heap(heap)
    for i in range(len(heap)-1, -1, -1):
        heap[0],heap[i] = heap[i],heap[0]
        max_heapify(heap, i, 0)
    return heap   
```

# 二叉树

## 三种遍历方式

![avatar](/Users/didi/Desktop/屏幕快照 2019-04-09 下午11.17.38.png)

- 层序遍历

```python
def level(root):
    if root == None:
        return 0
    queue = []
    node = root
    queue.append(node)
    while queue:
        node = queue.pop(0)
        print node.val,
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
        
```



- 前序遍历

```python
def front(root):
    if root == None:
        return 0
    node = root
    stack = []
    while node or stack:
        while node:
            print node.val,
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right     
```

- 中序遍历

```python
def middle(root):
    if root == None:
        return 0
    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print node.val
        node = node.right
        
```

- 后序遍历

左右根

后序的逆序是：根右左

```python
def late(root):
    if root == None:
        return 0
    node = root
    stack1 = []
    stack2 = []
    while node or stack1:
        while node:
            stack2.append(node)
            stack1.append(node)
            node = node.right
        node = stack1.pop()
        node = node.left
    while stack2:
        print stack2.pop().val,

def later_stack(self, root):
    """利用堆栈实现树的后序遍历"""
    if root == None:
        return
    myStack1 = []
    myStack2 = []
    node = root
    myStack1.append(node)
    while myStack1: 
        #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
        node = myStack1.pop()
        if node.lchild:
            myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
                myStack2.append(node)
                #将myStack2中的元素出栈，即为后序遍历次序
                while myStack2:              
                    print myStack2.pop().elem,            
```





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
        """利用堆栈实现树的先序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            #从根节点开始，一直找它的左子树
            while node:  
                print node.elem,
                myStack.append(node)
                node = node.lchild
            #while结束表示当前节点node为空，即前一个节点没有左子树了
            node = myStack.pop()         
            #开始查看它的右子树
            node = node.rchild    


    def middle_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            #从根节点开始，一直找它的左子树
            while node:                
                myStack.append(node)
                node = node.lchild
            #while结束表示当前节点node为空，即前一个节点没有左子树了
            node = myStack.pop()       
            print node.elem,
            #开始查看它的右子树
            node = node.rchild         


    def later_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1: 
            #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        #将myStack2中的元素出栈，即为后序遍历次序
        while myStack2:              
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

## 剑指 offer

### 面试题6：重建二叉树

题目描述：

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

思路：

采用递归的方法：通过切片的方式来获取左子节点和右子节点集合。

```python
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def reConstructBinaryTree(self, pre, tin)
        if pre == None:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            #通过逐一返回根节点的方法来构建二叉树
            res = TreeNode(pre[0])
            root = tin.index(pre[0])
            res.left = self.reConstructBinaryTree(pre[1:root+1], tin[:root])
            res.right = self.reConstructBinaryTree(pre[root+1:], tin[root+1:])
        return res
```

### 面试题18 树的字结构

题目描述：

输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

思路：

本题可以分为两步，第一步：找到A中与B的根结点值相等的结点R，第二步：判断以R为根结点的子树是否包含B一样的结构。本题思路不难，但是需要格外注意对指针空值的判断。

```python
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right =None
class Solution:
    def HasSubTree(self, root1, root2):
        result = False
        if root1 and root2:
            if root1.val == root2.val:
                result = self.iseuqual(root1,root2)
            if not result:
                result = self.HasSubTree(root1.left, root2)
            if not result:
                result = self.HasSubTree(root1.right, root2)
                
        return result
    
    def iseuqual(self, root1, root2):
        if not root1:
            return False
        if not root2:
            return True
        if root1.val != root2.val:
            return False
        return self.iseuqual(root1.left, root2.left) and iseuqual(root1.right, root2.right)
```

链接：<https://blog.csdn.net/qq_20141867/article/details/81067253>

# 数组

## 常用方法

数据映射法：P114

分治法：P118

二分查找法：P122

字典法：P126

类快排法：P129

动态规划法：P132

## leetcode

1. Remove Duplicates from Sorted Array

https://blog.csdn.net/qq_28119401/article/details/52972467

1. Remove Element

https://blog.csdn.net/qq_28119401/article/details/52972484

1. Search Insert Position



1. Maximum Subarray

https://blog.csdn.net/zl87758539/article/details/51676108



# 字符串

## 常用方法

动态规划：P184



## leetcode

1. Count and Say

<https://blog.csdn.net/Lucy_R/article/details/79003142>

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

1. Merge Two Sorted Lists

# 哈希表（Hash table）

使用哈希表可以进行非常快速的查找操作，查找时间为常数，同时不需要元素排列有序；python的内建数据类型：字典，就是用哈希表实现的。

python中的这些东西都是哈希原理：字典(dictionary)、集合(set)、计数器(counter)、默认字典Defaut dict)、有序字典(Order dict).

例题：

- leetcode：128.

# leetcode

#### 128. 最长连续序列

https://leetcode-cn.com/problems/longest-consecutive-sequence/

给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

思路：

用一个字典存储中间值。遍历数组，对于数字i，找到i-1和i+1对应的value值,如果不存在则记0。然后把i的value值设为i-1,i+1的value值之和，并加1，相当于连接起来。同时置最左端和最右端的数的value值为i的value值（中间的数都已经出现过，不会再用到了）。然后更新一次最大值。
原文：https://blog.csdn.net/yurenguowang/article/details/77869313 

```python
def longestConsecutive(nums):
    if nums == None or len(nums) == 0:
        return 0
    arr = set(nums)
    maxlength = 0
    hash_dict = {}
    for key in arr:
        left = 0
        right = 0
        if key - 1 in hash_dict:
            left = hash_dict[key-1]
        if key + 1 in hash_dict:
            right = hash_dict[key+1]
        hash_dict[key] = 1 + left + right 
        hash_dict[key-left] = 1 + left + right
        hash_dict[key+right] = 1 + left + right
        maxlength = max(maxlength, hash_dict[key]） 
    return maxlength                
```

