# 排序

## 选择排序

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

时间复杂度：最好：O(n)   最坏：O(n*n)    平均：O(nn)

空间复杂度：O(1)

```python
#时间复杂度：O(n*n)
def bubble_sort(arr):
    n = len(arr)
    for i in range(a-1):
        for j in range(a-i-1):
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
        """利用堆栈实现树的先序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                 #从根节点开始，一直找它的左子树
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

