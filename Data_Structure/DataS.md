# 常用算法思想

## 贪心算法

基本概念：

贪心算法是指：在每一步求解的步骤中，它要求“贪婪”的选择最佳操作，并希望通过一系列的最优选择，能够产生一个问题的（全局的）最优解。

 

贪心算法每一步必须满足一下条件：

1、可行的：即它必须满足问题的约束。

2、局部最优：他是当前步骤中所有可行选择中最佳的局部选择。

3、不可取消：即选择一旦做出，在算法的后面步骤就不可改变了。

例题：

1. 53. Maximum Subarray（求最大子数组之和问题）[link](#53. Maximum Subarray)

## 排列组合

```python
import math
value = math.factorial(3)
print(value)

def A_n_m(n,m):
    temp1=math.factorial(n)
    temp2=math.factorial(n-m)
    return(int(temp1/temp2))
    
def C_n_m(n,m):
    temp1=A_n_m(n,m)
    temp2=A_n_m(m,m)
    return(int(temp1/temp2))
    
n=5
m=2
  
re=C_n_m(n,m)
print(re)
```

## 动态规划

### 背包问题

```python 
def dp_bag(n, c, w, v):
    """
    测试数据：
    n = 6  物品的数量，
    c = 10 书包能承受的重量，
    w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
    v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    """
    # 置零，表示初始状态
    #j为当前的背包容量，前 i 个物品最佳组合对应的价值
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j>= w[i-1] and value[i][j]<value[i-1][j-w[i-1]]+v[i-1]:
                value[i][j] = value[i-1][j-w[i-1]] + v[i-1]

    return value

```

常见问题：

1. Leetcode 62. 不同路径 [link](#62. Unique Paths)
2. Leetcode 63 不同路径（有障碍物）[link](#63. Unique Paths II)
3. Leetcode 64最小路径和 [link](#64. Minimum Path Sum)

## 递归

常见问题：

1. Leetcode101. 对称树[link](#101. Symmetric Tree)
2. leetcode100 相同树[link](#100. Same Tree)

## 深度优先搜索（DFS）

相关链接：https://www.jianshu.com/p/bff70b786bb6

https://blog.csdn.net/victoryshen/article/details/80227222

https://blog.csdn.net/qq_40276310/article/details/80668401

https://blog.csdn.net/weixin_43272781/article/details/82959089

https://www.cnblogs.com/George1994/p/6346751.html

理解：

深度优先搜索属于图算法的一种，是一个针对图和树的遍历算法，英文缩写为DFS即Depth First Search。

深度优先搜索是图论中的经典算法，利用深度优先搜索算法可以产生目标图的相应拓扑排序表，利用拓扑排序表可以方便的解决很多相关的图论问题，如最大路径问题等等。一般用堆数据结构来辅助实现DFS算法。

其过程简要来说是对每一个可能的分支路径深入到不能再深入为止，而且每个节点只能访问一次。

过程：

图的深度优先搜索(Depth First Search, DFS)，和树的前序遍历非常类似。

1.从顶点v出发，首先访问该顶点;

2.然后依次从它的各个未被访问的邻接点出发深度优先搜索遍历图;

3.直至图中所有和v有路径相通的顶点都被访问到。

4.若此时尚有其他顶点未被访问到，则另选一个未被访问的顶点作起始点，重复上述过程，直至图中所有顶点都被访问到为止。

常见问题：

1. 树是否对称[link](#101. Symmetric Tree)

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

# 堆栈



例题：

1. 224. Basic Calculator [link](#224. Basic Calculator)

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

## leetcode

1. leetcode 100 相同树[link](#100. Same Tree)
2. Leetcode101. 对称树[link](#101. Symmetric Tree)
3. Leetcode 102 层次遍历二叉树[link](#102. Binary Tree Level Order Traversal)
4. Leetcode 103 Z字宽度遍历二叉树[link](#103. Binary Tree Zigzag Level Order Traversal)
5. leetcode 104 树的最大深度 [link](# 104. Maximum Depth of Binary Tree)
6. Leetcode 107 与102类似 [link](#107. Binary Tree Level Order Traversal II)

## 剑指 offer

1. 面试题6：重建二叉树[link](#面试题6：重建二叉树)
2. 面试题18： 树的字结构 [link](#面试题18 树的字结构)

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

s为字符串
s.isalnum() 所有字符都是数字或者字母
s.isalpha() 所有字符都是字母
s.isdigit() 所有字符都是数字
s.islower() 所有字符都是小写
s.isupper() 所有字符都是大写
s.istitle() 所有单词都是首字母大写，像标题
s.isspace() 所有字符都是空白字符、\t、\n、\r

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

## 常见问题

1. 链表反转

```python
class Node:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next

def reverse(link):
    pre = link
    cur = link.next
    pre.next = None
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre

if __name__ == '__main__':
    link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
    root = reverse(link)
    while root:
        print(root.data)
        root =root.next
```

## leetcode

1. 21.合并两个有序的链表[link](#21. Merge Two Sorted Lists)

234. 234.回文链表[link](#234.Palindrome Linked List)

# 哈希表（Hash table）

使用哈希表可以进行非常快速的查找操作，查找时间为常数，同时不需要元素排列有序；python的内建数据类型：字典，就是用哈希表实现的。

python中的这些东西都是哈希原理：字典(dictionary)、集合(set)、计数器(counter)、默认字典Defaut dict)、有序字典(Order dict).

例题：

- leetcode：128.

# leetcode

### 21. Merge Two Sorted Lists

原题：https://leetcode.com/problems/merge-two-sorted-lists/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        result = ListNode(0)
        node = result
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        
        return result.next
```



### 53. Maximum Subarray

原文链接：https://blog.csdn.net/qq_37466121/article/details/85270073

题目要求 （高频题）
给定一个整数数组nums，找到具有最大和的连续子数组（包含至少一个数字）并返回其和。

示例
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

思路方法

贪心算法思想： 设置两个变量，一个用来存储局部最优值，一个用来比较全局最优值。

所以问题就变成了，我们怎么去求当前的局部最优值和全局最优。

局部最优：就是以当前遍历元素为结尾的最大子数组

算法精髓

- 局部最优有两种可能：一个是当前局部最优 + 当前遍历元素；另一个就只是当前遍历元素。

- 然后全局最优就是在，上边选出的局部最优和当前全局最优中进行比较，取更大的，即可。然后对每个元素都进行上述两个操作，返回最大子数组的和。

一次遍历即可完成，时间复杂度O(n), 空间复杂度O(1)，妥妥的解决此类问题！



```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #贪心算法
        sub_max = all_max = -2**32
        for key in nums:
            sub_max = max(sub_max+key, key)
            all_max = max(sub_max,all_max)
        return all_max
```

### 62. Unique Paths

原题：https://leetcode.com/problems/unique-paths/

解题思路：https://blog.csdn.net/L141210113/article/details/88823381

题意：从左上角到右下角有多少条路径

题目分析：

这一题是以及经典的动态规划入门题，可以建立二维数组解决，它每一个点的路径数与左边和上面的点路径数相关。
解题思路：
看下面这个图从左上出发，向右有一条路径，向下有一条路径，到右下可以先向右走再过去或者先向下走再过去，2 = 1 + 1。

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0]*m]*n
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i-1][j] + arr[i][j-1]
                    
        return arr[n-1][m-1]
```

### 63. Unique Paths II

原题：https://leetcode.com/problems/unique-paths-ii/

解题：https://blog.csdn.net/fuxuemingzhu/article/details/83154114

题意：

给出了一个m * n的地图，上面有个机器人位于左上角，现在他想到达右下角。但是这个地图某些位置可能有障碍物。它每次只能向右边或者下边走一步，问能到达右下角的方式有多少种。

思路：动态规划
第一行第一列的所有方式只有1种，到达其他位置的方式是这个位置上面 + 这个位置左边用DP的话，注意需要判断某个位置是不是有障碍物，如果有障碍物，那么到达这个地方的方法是0。总体思路和上面记忆化搜索差不多。

时间复杂度是O(m * n)，空间复杂度是O(m * n)。

```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        arr = [[0]*(n+1)]*(m+1)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if obstacleGrid[i-1][j-1]==1:
                    arr[i][j] = 0
                else:
                    if i == j == 1:
                        arr[i][j] = 1
                    else:
                        arr[i][j] = arr[i-1][j] + arr[i][j-1]
        
        return arr[m][n]
```

### 64. Minimum Path Sum

原题：https://leetcode.com/problems/minimum-path-sum/

解题：https://blog.csdn.net/fuxuemingzhu/article/details/82620422

题意：

求一个矩阵从左上角到右下角的最短路径和。

思路：动态规划（DP）

从左上角开始到某个点的最短路径一定等于其上方、左方最短路径+当前的值。因此写成双重循环即可。

这个算法的时间啊复杂度是O(m * n)，空间复杂度是O(m * n)。

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    before = 0
                elif i == 0:
                    before = grid[i][j-1]
                elif j == 0:
                    before = grid[i-1][j]
                else:
                    before = min(grid[i-1][j], grid[i][j-1])
                grid[i][j] = before + grid[i][j]
        return grid[m-1][n-1]
```



### 100. Same Tree

原题：https://leetcode.com/problems/same-tree/

解题：https://www.cnblogs.com/loadofleaf/p/5502249.html

题意：

判断两个二叉树是否相同

思路：

递归，逐一遍历，判断是否相同。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if p != None and q == None:
            return False
        if p == None and q != None:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```



### 101. Symmetric Tree

原题：https://leetcode.com/problems/symmetric-tree/

解题：https://blog.csdn.net/coder_orz/article/details/51579528

题意：

给定一个二叉树，判断它是否是自己的镜像（中心对称）。

思路方法

**思路一**：递归

递归，对于每个节点，检查树的左右节点值是否相等，同时判断：左节点的左子树和右节点的右子树是否对称、右节点的左子树和左节点的右子树是否对称。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.mirror(root.left, root.right)
    def mirror(self, left, right):
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        return self.mirror(left.left, right.right) and self.mirror(left.right, right.left)
```

**思路二**：深度优先搜索

非递归算法。算是将上面的递归方法改写成非递归方法，实际上是深度优先搜索（DFS）。

```python 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stackl, stackr = [root.left], [root.right]
        while len(stackl) > 0 and len(stackr) > 0:
            left = stackl.pop()
            right = stackr.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            if left.val != right.val:
                return False
            stackl.append(left.left)
            stackl.append(left.right)
            stackr.append(right.right)
            stackr.append(right.left)
        return len(stackl) == 0 and len(stackr) == 0
```

### 102. Binary Tree Level Order Traversal

原题链接：https://leetcode.com/problems/binary-tree-level-order-traversal/

解题：https://blog.csdn.net/fuxuemingzhu/article/details/79616156

题意：层次遍历二叉树

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        node = root
        myQueue = []
        res = []
        if root == None:
            return myQueue
        myQueue.append(root)
        while myQueue:
            level = []
            for i in range(len(myQueue)):
                node = myQueue.pop(0)
                level.append(node.val)
                if node.left != None:
                    myQueue.append(node.left)
                if node.right != None:
                    myQueue.append(node.right)
            res.append(level)
        
        return res
```

### 103. Binary Tree Zigzag Level Order Traversal

原题链接：https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

解题：https://www.cnblogs.com/chruny/p/5251462.html

题意：

Z字宽度遍历树。

思路：

这题可以用比较取巧的方法。首先获得宽度遍历的结果，然后将第二层的翻转就可以了。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        node = root
        myQueue = []
        res = []
        if root == None:
            return res
        myQueue.append(node)
        key = -1
        while myQueue:
            level = []
            
            for i in range(len(myQueue)):
                node = myQueue.pop(0)
                level.append(node.val)
                if node.left != None:
                    myQueue.append(node.left)
                if node.right != None:
                    myQueue.append(node.right)
            if key == -1:
                res.append(level)
                key = 1
            elif key == 1:
                res.append(level[::-1])
                key = -1
            
        return res
```



### 104. Maximum Depth of Binary Tree

原文链接：https://blog.csdn.net/IT_job/article/details/80224403

要求：

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

​    3

   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        else:
            l = 1 + self.maxDepth(root.left)
            r = 1 + self.maxDepth(root.right)
            return max(l,r)
```

### 107. Binary Tree Level Order Traversal II

原题链接：https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

解题：https://blog.csdn.net/coder_orz/article/details/51583729

题意：

给定一个二叉树，返回其从下到上的层序遍历（从左到右，从下到上）

思路：

这道题实际上完全可以先得到从上到下的层序遍历，再逆序结果，但这样就没意思了，所以应该尝试避免reverse操作。不过方法还是类似的。 
相关问题：[102. Binary Tree Level Order Traversal [easy\] 

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        node = root
        if root == None:
            return res
        myQueue = []
        myQueue.append(node)
        while myQueue:
            level = []
            for i in range(len(myQueue)):
                node = myQueue.pop(0)
                level.append(node.val)
                if node.left != None:
                    myQueue.append(node.left)
                if node.right != None:
                    myQueue.append(node.right)
            res.append(level)
            
        return res[::-1]
```



### 128. 最长连续序列

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

### 179. Largest Number

原题：https://leetcode.com/problems/largest-number/

解题：https://www.jianshu.com/p/960cf375c40a

题意：

将已知整数数组组成最大的数字，以字符串的形式输出。

思路：

关键点就在于，如何对比两个数的大小？（理解为两个数谁应该放在前面），解法是按照顺序拼接两个字母串进行比较，如果a ＋b串 大于 b＋a串，那么a比较大（即题意中理解的a应该放在前面），反之b比较大。

```python
class Solution:
    def smaller(self, a, b):
        strA = str(a) + str(b)
        strB = str(b) + str(a)
        if strA > strB:
            return False
        else:
            return True
    
    def largestNumber(self, nums: List[int]) -> str:
        
        res = ''
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if self.smaller(nums[i], nums[j]):
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        for val in nums:
            res += str(val)
        if res[0] == '0':
            return '0'
        return res
```



### 224. Basic Calculator

原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/84133441

题目描述：
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
题目大意：
实现一个基本计算器，输入的是只含有括号数字加减号的字符串。

解题方法：
栈
这个题没有乘除法，也就少了计算优先级的判断了。众所周知，实现计算器需要使用一个栈，来保存之前的结果，把后面的结果计算出来之后，和栈里的数字进行操作。

使用了res表示不包括栈里数字在内的结果，num表示当前操作的数字，sign表示运算符的正负，用栈保存遇到括号时前面计算好了的结果和运算符。

操作的步骤是：

- 如果当前是数字，那么更新计算当前数字；
- 如果当前是操作符+或者-，那么需要更新计算当前计算的结果res，并把当前数字num设为0，sign设为正负，重新开始；
- 如果当前是(，那么说明后面的小括号里的内容需要优先计算，所以要把res，sign进栈，更新res和sign为新的开始；
- 如果当前是)，那么说明当前括号里的内容已经计算完毕，所以要把之前的结果出栈，然后计算整个式子的结果；
- 最后，当所有数字结束的时候，需要把结果进行计算，确保结果是正确的。

```python
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res,num,sign = 0,0,1
        for key in s:
            if key.isdigit():
                num = num*10 + int(key)
            elif key == '+' or key == '-':
                res = res + num*sign
                num = 0
                sign = 1 if key == '+' else -1
            elif key == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif key == ')':
                res = res + num*sign
                num = 0
                res *= stack.pop()
                res += stack.pop()
                
        res = res + num*sign
        return res
```



### 234.Palindrome Linked List

https://blog.csdn.net/weixin_36372879/article/details/82596003

Given a singly linked list, determine if it is a palindrome.

**Example 1:**

```
Input: 1->2
Output: false
```

**Example 2:**

```
Input: 1->2->2->1
Output: true
```

要求：时间复杂度O(N),空间复杂度O(1)

思路：

1. 采用快慢指针来找到链表中点
2. 找到中点之后，采用空间复杂度O(1)的反转链表的算法，将链表反转，需要注意的是，反转过程中语句的顺序，head = head.next一定要在第二句，而不是最后，要不然就断链了，因为p指向了head更改p相当于更改了head,当head指向next之后，才能更改p
3. 最后判读反转后的链表和原来的链表的val值进行比较。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverlist(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
            
        return new_head
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            
            slow = slow.next
        new_head = self.reverlist(slow)
        while new_head:
            if new_head.val != head.val:
                return False
            new_head = new_head.next
            head = head.next
        return True
```

# 剑指 offer

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
        return self.iseuqual(root1.left, root2.left) and self.iseuqual(root1.right, root2.right)
```

链接：<https://blog.csdn.net/qq_20141867/article/details/81067253>