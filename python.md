# python基础

## 浅拷贝／深拷贝

<https://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html>

## 数据格式转换

### DataFrame - list

```python
#DataFrame - list
# -*- coding:utf-8-*-
import numpy as np
import pandas as pd

train_data = np.array(data_x)#np.ndarray()
train_x_list=train_data.tolist()#list

#list - DataFrame
from pandas.core.frame import DataFrame
a=[[1,2,3,4],[5,6,7,8]]
data=DataFrame(a)#这时候是以行为标准写入的
data.rename(columns={0:'a',1:'b'},inplace=True)#注意这里0和1都不是字符串
```

### DataFrame - RDD

```python
#rdd - DataFrame
from __future__ import print_function
from pyspark.sql import SparkSession
from pyspark.sql import Row
#读取RDD数据
files = '/user/driver_ecosys/zhengchen/nn/output5'
data_rdd = sc.textFile(files)
data_rdd = data_rdd.map(lambda l: l.split("\t"))
data_rdd = data_rdd.map(lambda p: Row(trace_id=p[0], label=p[1], ecr=p[2], subsidy=p[3]))
#将RDD转化为DF
data_df = spark.createDataFrame(data_rdd)
```

## 常用技巧

**整数输出格式：**

```python 
for i in range(1,366):
    m = "%03d" % i      #输出001
    print('part00'+str(m))
```

**将列表中数字字符串转换为整数再排序：**

```python
numbers = ['2', '4', '1', '3']
numbers = map(int, numbers)
#正序
numbers = sorted(numbers, reverse = False)
#倒序
numbers = sorted(numbers, reverse = True)
```

**一行代码定义List**

```python
numble = [1,2,3,4,5]

odds = []
for n in numble:
    if n % 2 == 1:
        odds.append(n*2)
#oddss = [n*2 for n in numble if n%2==1]       
print odds
print oddss
```

## 转义字符

在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符。如下表：

| 转义字符    | 描述            |
| ----------- | --------------- |
| \(在行尾时) | 续行符          |
| \\          | 反斜杠符号      |
| \'          | 单引号          |
| \"          | 双引号          |
| \a          | 响铃            |
| \b          | 退格(Backspace) |
| \e          | 转义            |
| \000        | 空              |
| \n          | 换行            |
| \v          | 纵向制表符      |
| \t          | 横向制表符      |
| \r          | 回车            |
| \f          | 换页            |

## 变量类型

### 多个变量赋值

```python
a = b = c = 1
a, b, c = 1, 2, "john"
```

### 数据类型

- Numbers（数字）

  数字类型：

  int（有符号整型），long（长整型[也可以代表八进制和十六进制]），float（浮点型），complex（复数）

- String（字符串）

- List（列表）

- Tuple（元组）

  不可变，可以索引

- Dictionary（字典）

  无序，通过键来获取数据

  ```python
  print dict[key]        # 输出键为 key 的值
  print dict.keys()      # 输出所有键
  print dict.values()    # 输出所有值
  ```

### 数据类型转换

| 函数                                                         | 描述                                                |
| ------------------------------------------------------------ | --------------------------------------------------- |
| [int(x [,base\])](https://www.runoob.com/python/python-func-int.html) | 将x转换为一个整数                                   |
| [long(x [,base\] )](https://www.runoob.com/python/python-func-long.html) | 将x转换为一个长整数                                 |
| [float(x)](https://www.runoob.com/python/python-func-float.html) | 将x转换到一个浮点数                                 |
| [complex(real [,imag\])](https://www.runoob.com/python/python-func-complex.html) | 创建一个复数                                        |
| [str(x)](https://www.runoob.com/python/python-func-str.html) | 将对象 x 转换为字符串                               |
| [repr(x)](https://www.runoob.com/python/python-func-repr.html) | 将对象 x 转换为表达式字符串                         |
| [eval(str)](https://www.runoob.com/python/python-func-eval.html) | 用来计算在字符串中的有效Python表达式,并返回一个对象 |
| [tuple(s)](https://www.runoob.com/python/att-tuple-tuple.html) | 将序列 s 转换为一个元组                             |
| [list(s)](https://www.runoob.com/python/att-list-list.html)  | 将序列 s 转换为一个列表                             |
| [set(s)](https://www.runoob.com/python/python-func-set.html) | 转换为可变集合                                      |
| [dict(d)](https://www.runoob.com/python/python-func-dict.html) | 创建一个字典。d 必须是一个序列 (key,value)元组。    |
| [frozenset(s)](https://www.runoob.com/python/python-func-frozenset.html) | 转换为不可变集合                                    |
| [chr(x)](https://www.runoob.com/python/python-func-chr.html) | 将一个整数转换为一个字符                            |
| [unichr(x)](https://www.runoob.com/python/python-func-unichr.html) | 将一个整数转换为Unicode字符                         |
| [ord(x)](https://www.runoob.com/python/python-func-ord.html) | 将一个字符转换为它的整数值                          |
| [hex(x)](https://www.runoob.com/python/python-func-hex.html) | 将一个整数转换为一个十六进制字符串                  |
| [oct(x)](https://www.runoob.com/python/python-func-oct.html) | 将一个整数转换为一个八进制字符串                    |

#### eval()	repr()	isinstance()

- isinstance()

功能：判断一个对象是否是一个已知的类型

- eval()

功能：将字符串str转化为dict, list, tuple数据类型

- repr()

功能：和eval()相反，将dict, list, tuple数据类型转化为str

举例：

```python
def eval_test(line):
    line = repr(line)   #将tuple转化为str
    lines = eval(line)  #将str转化为tuple
    if isinstance(lines, tuple):      #判断是否为tuple类型
        id = lines[0]
        subjectList = eval(lines[1])　　#将str转化为list
        sl_list = []
        for sl in subjectList:
            del sl["subject_type"]
            del sl["code"]
            del sl["subject_id"]
            del sl["weight"]
            del sl["concept_stock"]
            del sl["second_relation"]
            del sl["third_relation"]
            sl_list.append(sl)
        subject_manualList = eval(lines[2])
        print(sl_list)
        sm_list = []
        for sm in subject_manualList:
            del sm["subject_type"]
            del sm["code"]
            del sm["subject_id"]
            del sm["weight"]
            del sm["concept_stock"]
            del sm["second_relation"]
            del sm["third_relation"]
            sm_list.append(sm)
        print(sm_list)
if __name__ == "__main__":
    data = ('01e6bfd535f255c1651e72427149cefe', '[{"subject_id":"154","code":"600696.SH","third_relation":{},"subject_type":"股票","original_company_name":"p2p","concept_stock":"互联网+","second_relation":{},"subject_name":"ST岩石","weight":0.1790862502086199,"tags":[],"opinion":""}]', '[{"subject_id":"154","code":"600696.SH","third_relation":{},"subject_type":"股票","original_company_name":"p2p","concept_stock":"互联网+","second_relation":{},"subject_name":"ST岩石","weight":0.1790862502086199,"tags":[],"opinion":"0"}]')
    eval_test(data)
```

## 运算符

### 算数运算符

| 运算符 | 描述                                            | 实例                                               |
| ------ | ----------------------------------------------- | -------------------------------------------------- |
| +      | 加 - 两个对象相加                               | a + b 输出结果 30                                  |
| -      | 减 - 得到负数或是一个数减去另一个数             | a - b 输出结果 -10                                 |
| *      | 乘 - 两个数相乘或是返回一个被重复若干次的字符串 | a * b 输出结果 200                                 |
| /      | 除 - x除以y                                     | b / a 输出结果 2                                   |
| %      | 取模 - 返回除法的余数                           | b % a 输出结果 0                                   |
| **     | 幂 - 返回x的y次幂                               | a**b 为10的20次方， 输出结果 100000000000000000000 |
| //     | 取整除 - 返回商的整数部分（**向下取整**）       | `>>> 9//2 4 >>> -9//2 -5`                          |

### 比较运算符

| 运算符 | 描述                                                         | 实例                                     |
| ------ | ------------------------------------------------------------ | ---------------------------------------- |
| ==     | 等于 - 比较对象是否相等                                      | (a == b) 返回 False。                    |
| !=     | 不等于 - 比较两个对象是否不相等                              | (a != b) 返回 true.                      |
| <>     | 不等于 - 比较两个对象是否不相等                              | (a <> b) 返回 true。这个运算符类似 != 。 |
| >      | 大于 - 返回x是否大于y                                        | (a > b) 返回 False。                     |
| <      | 小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。 | (a < b) 返回 true。                      |
| >=     | 大于等于	- 返回x是否大于等于y。                           | (a >= b) 返回 False。                    |
| <=     | 小于等于 -	返回x是否小于等于y。                           | (a <= b) 返回 true。                     |

### 赋值运算符

| 运算符 | 描述             | 实例                                  |
| ------ | ---------------- | ------------------------------------- |
| =      | 简单的赋值运算符 | c = a + b 将 a + b 的运算结果赋值为 c |
| +=     | 加法赋值运算符   | c += a 等效于 c = c + a               |
| -=     | 减法赋值运算符   | c -= a 等效于 c = c - a               |
| *=     | 乘法赋值运算符   | c *= a 等效于 c = c * a               |
| /=     | 除法赋值运算符   | c /= a 等效于 c = c / a               |
| %=     | 取模赋值运算符   | c %= a 等效于 c = c % a               |
| **=    | 幂赋值运算符     | c **= a 等效于 c = c ** a             |
| //=    | 取整除赋值运算符 | c //= a 等效于 c = c // a             |

### 位运算符

| 运算符 | 描述                                                         | 实例                                                         |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| &      | 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0 | (a & b) 输出结果 12 ，二进制解释： 0000 1100                 |
| \|     | 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。 | (a \| b) 输出结果 61 ，二进制解释： 0011 1101                |
| ^      | 按位异或运算符：当两对应的二进位相异时，结果为1              | (a ^ b) 输出结果 49 ，二进制解释： 0011 0001                 |
| ~      | 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。**~x** 类似于 **-x-1** | (~a ) 输出结果 -61 ，二进制解释： 1100 0011，在一个有符号二进制数的补码形式。 |
| <<     | 左移动运算符：运算数的各二进位全部左移若干位，由 **<<** 右边的数字指定了移动的位数，高位丢弃，低位补0。 | a << 2 输出结果 240 ，二进制解释： 1111 0000                 |
| >>     | 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，**>>** 右边的数字指定了移动的位数 | a >> 2 输出结果 15 ，二进制解释： 0000 1111                  |

### 逻辑运算符

| 运算符 | 逻辑表达式 | 描述                                                         | 实例                    |
| ------ | ---------- | ------------------------------------------------------------ | ----------------------- |
| and    | x and y    | 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。 | (a and b) 返回 20。     |
| or     | x or y     | 布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。 | (a or b) 返回 10。      |
| not    | not x      | 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。 | not(a and b) 返回 False |

### 成员运算符

| 运算符 | 描述                                                    | 实例                                              |
| ------ | ------------------------------------------------------- | ------------------------------------------------- |
| in     | 如果在指定的序列中找到值返回 True，否则返回 False。     | x 在 y 序列中 , 如果 x 在 y 序列中返回 True。     |
| not in | 如果在指定的序列中没有找到值返回 True，否则返回 False。 | x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。 |

### 身份运算符

| 运算符 | 描述                                        | 实例                                                         |
| ------ | ------------------------------------------- | ------------------------------------------------------------ |
| is     | is 是判断两个标识符是不是引用自一个对象     | **x is y**, 类似 **id(x) == id(y)** , 如果引用的是同一个对象则返回 True，否则返回 False |
| is not | is not 是判断两个标识符是不是引用自不同对象 | **x is not y** ， 类似 **id(a) != id(b)**。如果引用的不是同一个对象则返回结果 True，否则返回 False。 |

### 运算符优先级

| 运算符                   | 描述                                                   |
| ------------------------ | ------------------------------------------------------ |
| **                       | 指数 (最高优先级)                                      |
| ~ + -                    | 按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@) |
| * / % //                 | 乘，除，取模和取整除                                   |
| + -                      | 加法减法                                               |
| >> <<                    | 右移，左移运算符                                       |
| &                        | 位 'AND'                                               |
| ^ \|                     | 位运算符                                               |
| <= < > >=                | 比较运算符                                             |
| <> == !=                 | 等于运算符                                             |
| = %= /= //= -= += *= **= | 赋值运算符                                             |
| is is not                | 身份运算符                                             |
| in not in                | 成员运算符                                             |
| not and or               | 逻辑运算符                                             |

## 条件语句

```python
if 判断条件：
    执行语句……
else：
    执行语句……
```

pass表示空语句

## 循环语句

### while循环

```python
while 判断条件：
    执行语句……
```

while 语句时还有另外两个重要的命令 continue，break 来跳过循环，

continue 用于跳过该次循环，

break 则是用于退出整个循环，

pass表示空语句

此外"判断条件"还可以是个常值，表示循环必定成立，具体用法如下：

```python
# continue 和 break 用法
 
i = 1
while i < 10:   
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print i         # 输出双数2、4、6、8、10
 
i = 1
while 1:            # 循环条件为1必定成立
    print i         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break
```

### for循环

```python
for iterating_var in sequence:
   statements(s)
```

For语句时还有另外两个重要的命令 continue，break 来跳过循环，

continue 用于跳过该次循环，

break 则是用于退出整个循环，

pass表示空语句

### 嵌套循环



##python数据结构

### 数字

Python 支持四种不同的数值类型：整型(Int)、长整型(long integers)、浮点型(floating point real values)、复数(complex numbers)。

Python 中数学运算常用的函数基本都在 math 模块、cmath 模块中。

Python math 模块提供了许多对浮点数的数学运算函数。

Python cmath 模块包含了一些用于复数运算的函数。

#### 数学函数

| 函数                                                         | 返回值 ( 描述 )                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [abs(x)](https://www.runoob.com/python/func-number-abs.html) | 返回数字的绝对值，如abs(-10) 返回 10                         |
| [ceil(x)](https://www.runoob.com/python/func-number-ceil.html) | 返回数字的上入整数，如math.ceil(4.1) 返回 5。                |
| [cmp(x, y)](https://www.runoob.com/python/func-number-cmp.html) | 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1    |
| [exp(x)](https://www.runoob.com/python/func-number-exp.html) | 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045         |
| [fabs(x)](https://www.runoob.com/python/func-number-fabs.html) | 返回数字的绝对值，如math.fabs(-10) 返回10.0                  |
| [floor(x)](https://www.runoob.com/python/func-number-floor.html) | 返回数字的下舍整数，如math.floor(4.9)返回 4                  |
| [log(x)](https://www.runoob.com/python/func-number-log.html) | 如math.log(math.e)返回1.0,math.log(100,10)返回2.0            |
| [log10(x)](https://www.runoob.com/python/func-number-log10.html) | 返回以10为基数的x的对数，如math.log10(100)返回 2.0           |
| [max(x1, x2,...)](https://www.runoob.com/python/func-number-max.html) | 返回给定参数的最大值，参数可以为序列。                       |
| [min(x1, x2,...)](https://www.runoob.com/python/func-number-min.html) | 返回给定参数的最小值，参数可以为序列。                       |
| [modf(x)](https://www.runoob.com/python/func-number-modf.html) | 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。 |
| [pow(x, y)](https://www.runoob.com/python/func-number-pow.html) | x**y 运算后的值。                                            |
| [round(x [,n\])](https://www.runoob.com/python/func-number-round.html) | 返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。 |
| [sqrt(x)](https://www.runoob.com/python/func-number-sqrt.html) | 返回数字x的平方根                                            |

#### 随机数函数

| 函数                                                         | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [choice(seq)](https://www.runoob.com/python/func-number-choice.html) | 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。 |
| [randrange ([start,\] stop [,step])](https://www.runoob.com/python/func-number-randrange.html) | 从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1 |
| [random()](https://www.runoob.com/python/func-number-random.html) | 随机生成下一个实数，它在[0,1)范围内。                        |
| [seed([x\])](https://www.runoob.com/python/func-number-seed.html) | 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。 |
| [shuffle(lst)](https://www.runoob.com/python/func-number-shuffle.html) | 将序列的所有元素随机排序                                     |
| [uniform(x, y)](https://www.runoob.com/python/func-number-uniform.html) | 随机生成下一个实数，它在[x,y]范围内。                        |

###数组

### 列表List

特点：可重复，类型可不同。

#### 索引列表的值

二维数组：

```python
len(array)     #数组行数 row
len(array[0])  #数组列数 column
```

#### 更新列表

可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项。

#### 删除列表元素

可以使用 del 语句来删除列表的元素

#### 常用函数

| 序号 | 函数                                                         |
| ---- | ------------------------------------------------------------ |
| 1    | [cmp(list1, list2)](https://www.runoob.com/python/att-list-cmp.html) 比较两个列表的元素 |
| 2    | [len(list)](https://www.runoob.com/python/att-list-len.html) 列表元素个数 |
| 3    | [max(list)](https://www.runoob.com/python/att-list-max.html) 返回列表元素最大值 |
| 4    | [min(list)](https://www.runoob.com/python/att-list-min.html) 返回列表元素最小值 |
| 5    | [list(seq)](https://www.runoob.com/python/att-list-list.html) 将元组转换为列表 |

#### 常用方法

| 序号 | 方法                                                         |
| ---- | ------------------------------------------------------------ |
| 1    | [list.append(obj)](https://www.runoob.com/python/att-list-append.html) 在列表末尾添加新的对象 |
| 2    | [list.count(obj)](https://www.runoob.com/python/att-list-count.html) 统计某个元素在列表中出现的次数 |
| 3    | [list.extend(seq)](https://www.runoob.com/python/att-list-extend.html) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） |
| 4    | [list.index(obj)](https://www.runoob.com/python/att-list-index.html) 从列表中找出某个值第一个匹配项的索引位置 |
| 5    | [list.insert(index, obj)](https://www.runoob.com/python/att-list-insert.html) 将对象插入列表 |
| 6    | [list.pop([index=-1\])](https://www.runoob.com/python/att-list-pop.html) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 |
| 7    | [list.remove(obj)](https://www.runoob.com/python/att-list-remove.html) 移除列表中某个值的第一个匹配项 |
| 8    | [list.reverse()](https://www.runoob.com/python/att-list-reverse.html) 反向列表中元素 |
| 9    | [list.sort(cmp=None, key=None, reverse=False)](https://www.runoob.com/python/att-list-sort.html) 对原列表进行排序 |

###字符串

#### 字符串运算符

下表实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"：

| 操作符 | 描述                                                         | 实例                                 |
| ------ | ------------------------------------------------------------ | ------------------------------------ |
| +      | 字符串连接                                                   | >>>a + b 'HelloPython'               |
| *      | 重复输出字符串                                               | >>>a * 2 'HelloHello'                |
| []     | 通过索引获取字符串中字符                                     | >>>a[1] 'e'                          |
| [ : ]  | 截取字符串中的一部分                                         | >>>a[1:4] 'ell'                      |
| in     | 成员运算符 - 如果字符串中包含给定的字符返回 True             | >>>"H" in a True                     |
| not in | 成员运算符 - 如果字符串中不包含给定的字符返回 True           | >>>"M" not in a True                 |
| r/R    | 原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。 | >>>print r'\n' \n >>> print R'\n' \n |
| %      | 格式字符串                                                   | 请看下一章节                         |

#### 字符串格式化

```python
print "My name is %s and weight is %d kg!" % ('Zara', 21) 
#输出：My name is Zara and weight is 21 kg!
```

python字符串格式化符号:

| 符   号 | 描述                                 |
| ------- | ------------------------------------ |
| %s      | 格式化字符串                         |
| %d      | 格式化整数                           |
| %f      | 格式化浮点数字，可指定小数点后的精度 |

#### Unicode 字符串

Python 中定义一个 Unicode 字符串和定义一个普通字符串一样简单：

```python
u'Hello World !'
#输出：u'Hello World !'
```

####字符串方法

链接：https://www.jianshu.com/p/b758332c44bb

##### strip() 

删除首尾某字符或空格

功能：用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。

**注意：**该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。

语法：`str.strip([chars])`

- chars -- 移除字符串头尾指定的字符序列。

- return:    返回处理后的新字符串。

比如：去首尾空格：`str.strip()`

##### split()　　

分割字符

功能：Python **split()** 通过指定分隔符对字符串进行分割，如果参数 num 有指定值，则仅分隔 num 个子字符串。

语法：`str.split(str="", num=string.count(str)).`

- str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
- num -- 分割次数。
- return:    返回分割后的字符串列表。

#####join()　　

拼接字符串。

功能：用于将序列中的元素以指定的字符连接生成一个新的字符串。

语法：`str.join(sequence)`

- sequence -- 要连接的元素序列。
- return:   返回通过指定字符连接序列中元素后生成的新字符串。

常用：

'x'.join(y)，x可以是任意分割字符，y是列表或元组。以列表为例，可以将列表中的每一个元素两头的引号给去除，同时，元素与元素之间以字符‘x’作为分割标志，并且列表最外面的中括号也能去除掉。元组同理。

举例：

```python
a_list=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
print(' '.join(a_list))
#输出：monday tuesday wednesday thursday friday saturday sunday

b_list = [1,2,3,4]
print(' '.join(str(x) for x in b_list))
#输出：1 2 3 4

```

##### replace()      

替换字符串

语法：`str.replace(old, new[, max])`

功能：字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

**title()		首字母大写**

功能：使每个单词的首字母大写。

语法：`str.title()`

**upper() 	 　全部大写**

功能：将每个单词的字母全部大写

**lower()  	 全部小写**

功能：将每个单词的字母全部小写

#####format()

格式化字符串的函数 **str.format()**.

基本语法是通过 **{}** 和 **:** 来代替以前的 **%** 。

format 函数可以接受不限个参数，位置可以不按顺序。

实例:

```python
# 不设置指定位置，按默认顺序 
"{} {}".format("hello", "world")    
#输出：'hello world'   

#设置指定位置
"{1} {0} {1}".format("hello", "world")
#输出：'world hello world'
```

实例：

```python
citys = [23]
params = {
    'START_DATE': start_date.strftime('%Y%m%d'),
    'END_DATE': end_date.strftime('%Y%m%d'),
    'CITY_ID': ','.join([str(x) for x in citys]),
}

bubble_sql_template = '''
  select
    *
  from bigdata_driver_ecosys_test.bubble_base
  where concat(year, month, day) between '{START_DATE}' and '{END_DATE}'
    and city_id in ({CITY_ID})
'''
bubble_sql = bubble_sql_template.format(**params)
bubble_df = spark.sql(bubble_sql).cache()
```

##### count()

功能：统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。

语法：

```python
str.count(sub, start= 0,end=len(string))
```

实例:

```python
str.count(sub, 4, 40) :  2
str.count(sub) :  1
```

##### find()

功能：检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，

语法：

```python
str.find(str, beg=0, end=len(string))
```

返回值：如果包含子字符串返回开始的索引值，否则返回-1。

实例：

```python
#!/usr/bin/python   
str1 = "this is string example....wow!!!" str2 = "exam"  
print str1.find(str2)    #输出：15
print str1.find(str2, 10)   #输出：15
print str1.find(str2, 40)   #输出：-1
```

##### index()

功能：检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。

语法：

```python
str.index(str, beg=0, end=len(string))
```

##### join()

功能：用于将序列中的元素以指定的字符连接生成一个新的字符串。

语法：

```
str.join(sequence)
```

实例：

```python
str = "-"
seq = ("a", "b", "c")
str.join( seq )    #输出：a-b-c
```

### 元组Tuple

Python的元组与列表类似，不同之处在于元组是只读的，不能修改。元组用“()”表示。

```python
#创建空元组
tup1 = ()
#元组中只包含一个元素时，需要在元素后面添加逗号
tup1 = (50,)
```

#### 元组访问

```python
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]
```

#### 修改元组

```python
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
 
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
tup3 = tup1 + tup2
print tup3
```

#### 删除元组

元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组。

#### 元组运算符

| Python 表达式                | 结果                         | 描述         |
| ---------------------------- | ---------------------------- | ------------ |
| len((1, 2, 3))               | 3                            | 计算元素个数 |
| (1, 2, 3) + (4, 5, 6)        | (1, 2, 3, 4, 5, 6)           | 连接         |
| ('Hi!',) * 4                 | ('Hi!', 'Hi!', 'Hi!', 'Hi!') | 复制         |
| 3 in (1, 2, 3)               | True                         | 元素是否存在 |
| for x in (1, 2, 3): print x, | 1 2 3                        | 迭代         |

#### 常用函数

| 序号 | 方法及描述                                                   |
| ---- | ------------------------------------------------------------ |
| 1    | [cmp(tuple1, tuple2)](https://www.runoob.com/python/att-tuple-cmp.html) 比较两个元组元素。 |
| 2    | [len(tuple)](https://www.runoob.com/python/att-tuple-len.html) 计算元组元素个数。 |
| 3    | [max(tuple)](https://www.runoob.com/python/att-tuple-max.html) 返回元组中元素最大值。 |
| 4    | [min(tuple)](https://www.runoob.com/python/att-tuple-min.html) 返回元组中元素最小值。 |
| 5    | [tuple(seq)](https://www.runoob.com/python/att-tuple-tuple.html) 将列表转换为元组。 |

### 字典Dict

列表适合于将值组织到一个结构中，可以通过编号进行引用；然而字典可以通过名字来引用值。字典也可以称为映射。

字典是无序的对象集合，通过键值存取的。字典用：“{}”标识，由键（key）和键值（value）组成。

- 键(key)必须使用不可变类型。在同一个字典中，键(key)必须是唯一的。

- 在单个 dictionary 里，dictionary 的值并不需要全都是同一数据类型，可以根据需要混用和匹配。
- Dictionary 的值可以是任意数据类型，包括字符串、整数、对象，甚至其它的 dictionary。

#### 创建字典

- 传统的文字表达式

```python
d={'name':'Allen','age':21,'gender':'male'}
```

- 动态分配键值

```python
d={}
d['name']='Allen'
d['age']=21
d['gender']='male'
print(d)       #{'age': 21, 'name': 'Allen', 'gender': 'male'}
```

- 字典键值表

```python
c = dict(name='Allen', age=14, gender='male')
print(c)         
#输出：{'gender': 'male', 'name': 'Allen', 'age': 14}
```

- 字典键值元组表

```python
e=dict([('name','Allen'),('age',21),('gender','male')])
print(e)       
#输出：{'age': 21, 'name': 'Allen', 'gender': 'male'}
```

- 所有的键值都相同，或者赋予初始值

```python
 f=dict.fromkeys(['height','weight'],'normal')
print(f)      
#输出：{'weight': 'normal', 'height': 'normal'}
```

#### 字典访问

`dic = {'a':"hello",'b':"how",'c':"you"}`

- 方法一

```python
for key in dic:
　　print(key,dic[key])     #dic[key]为取键值
　　print(key + str(dic[key]))
```

- 方法二

```python
for (k,v) in dic.items():
　　print "dic[%s]="%k,v
```

- 方法三

```python
for k,v in dic.iteritems():
　　print "dic[%s]="%k,v
```

#### 删除字典

```python
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
del dict['Name'] # 删除键 'Name'
dict.clear()     # 清空字典
del dict         # 删除字典
```

#### 常用方法

| 序号 | 函数及描述                                                   | 实例                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | len(dict) 计算字典元素个数，即键的总数。                     | `>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'} >>> len(dict) 3` |
| 2    | str(dict) 输出字典，以可打印的字符串表示。                   | `>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'} >>> str(dict) "{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"` |
| 3    | type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型。 | `>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'} >>> type(dict) <class 'dict'>` |

```python
len(dict)		#返回字典中键值对的数量
dict[key]		#返回键key上的值
dict[key] = v   #修改键key的值为v
del dict[key]   #删除键key
key in dict     #检查字典中是否含有键key
print(dict)     #输出整个字典
print(dict.keys()) 　#输出所有键
print(dict.values()) #s输出说有的键值
```

#### 常用函数

| 序号 | 函数及描述                                                   |
| ---- | ------------------------------------------------------------ |
| 1    | [radiansdict.clear()](https://www.runoob.com/python3/python3-att-dictionary-clear.html) 删除字典内所有元素 |
| 2    | [radiansdict.get(key, default=None)](https://www.runoob.com/python3/python3-att-dictionary-get.html) 返回指定键的值，如果值不在字典中返回default值 |
| 3    | [key in dict](https://www.runoob.com/python3/python3-att-dictionary-in.html) 如果键在字典dict里返回true，否则返回false |
| 4    | [radiansdict.items()](https://www.runoob.com/python3/python3-att-dictionary-items.html) 以列表返回可遍历的(键, 值) 元组数组 |
| 5    | [radiansdict.keys()](https://www.runoob.com/python3/python3-att-dictionary-keys.html) 返回一个迭代器，可以使用 list() 来转换为列表 |
| 6    | [radiansdict.values()](https://www.runoob.com/python3/python3-att-dictionary-values.html) 返回一个迭代器，可以使用 list() 来转换为列表 |

### 集合Set

是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算。

## 内置函数

###  enumerate

enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

语法：

```python
enumerate(sequence, [start=0])
```

参数：

- sequence -- 一个序列、迭代器或其他支持迭代对象。
- start -- 下标起始位置。

实例：

1. 使用 enumerate() 方法的实例：

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1)) #下标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```

2. 普通的 for 循环

```python
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print i, element
'''
0 one
1 two
2 three
'''
```

### max min sort

Python 的内置函数 max, min, sorted 中的参数 key.

Python 的内置函数max, min, sorted 都支持参数key，要求参数key是一个函数，该只接收一个参数（也就是该内置函数要处理的元素），key函数返回的结果作为比较大小或排序的依据。

通过对key的设定，可以灵活的进行找最大/小或排序。

```python
x = [-1, -2, -3]
max(x, key=abs) # 绝对值最大的元素，-3
min(x, key=abs) # 绝对值最小的元素，-1

# 对于接收多个参数的函数，可以用lambda表达式封装
import math
max(x, key=lambda item: math.pow(2, item)) 

sorted(x, abs) # 按照元素的绝对值排序，[-1, -2, -3]
```

### int 

int() 函数用于将一个字符串或数字转换为整型。

实例：

```python
int(3.6)        #3
#将二进制转化为十进制
a = '111'
int(a, 2)      #8
```



### bin()

**bin()** 返回一个整数 int 或者长整数 long int 的二进制表示。

举例：

```python
bin(10)      #'0b1010'
```





##日期和时间

Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。

时间间隔是以秒为单位的浮点小数。

每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。

```python
#获取当前时间
import time
ticks = time.time()
print "当前时间戳为:", ticks
#当前时间戳为: 1459994552.51
```



```python
#1.获取时间
#获取当前时间
import datetime
datetime.datetime.now()

#获取前一周的时间
import datetime
time = datetime.datetime.now() - datetime.timedelta(days = 7)

#设置开始结束时间
end_date =  datetime.datetime.now() - datetime.timedelta(days = 9)
start_date = end_date - datetime.timedelta(days = 7)

#时间格式转换
#datetime -> string
datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#输出：'2015-01-12 23:13:08'

#datetime <- string
datetime.datetime.strptime("2014-12-31 18:20:10", "%Y-%m-%d %H:%M:%S")
#输出：datetime.datetime(2014, 12, 31, 18, 20, 10)


```



##python异常处理

功能：处理python运行中出现的异常和错误，可以用来调试python程序。

**什么是异常？**

异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。

一般情况下，在Python无法正常处理程序时就会发生一个异常。异常是Python对象，表示一个错误。

当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。

###异常处理

try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。

如果你不想在异常发生时结束你的程序，只需在try里捕获它。

**语法：**

```python
try:
    语句      #进行别的代码
except <name>:
    语句      #如果在try部分引发了‘name’异常
except <name>,<data>:
    语句      #如果引发了‘name’异常，获得附加的数据
else:
    语句      #如果没有异常发生
```

**try的工作原理：**

- 如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
- 如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印缺省的出错信息）。
- 如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。

**实例1：**打开一个文件，在该文件中的内容写入内容，且并未发生异常。

```python
# _*_ coding: utf-8 _*_

try:
    fh = open("testfile","w")
    fh.write("这是一个测试文件！")
except IOError:
    print("Error:没有找到文件或读取文件失败")
else：
	print("内容写入文件成功")
    fh.close()
```

以上程序输出结果：

```python
$ python test.py 
内容写入文件成功
$ cat testfile       # 查看写入的内容
这是一个测试文件，用于测试异常!!
```

**实例2：**

打开一个文件，在该文件中的内容写入内容，但文件没有写入权限，发生了异常：

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()
```

在执行代码前为了测试方便，我们可以先去掉 testfile 文件的写权限，命令如下：

```python
chmod -w testfile
```

再执行以上代码：

```python
$ python test.py 
Error: 没有找到文件或读取文件失败
```

##正则表达式

###匹配单个字符

```python 
re.match(r"速度与激情/d","速度与激情3")

re.match(r"速度与激情[1-8]","速度与激情3")

re.match(r"速度与激情[1-345-8]","速度与激情3")

re.match(r"速度与激情[1-8a-z]","速度与激情a")
```

| 字符 | 功能                             |
| ---- | -------------------------------- |
| .    | 匹配任意一个字符（除了\n）       |
| []   | 匹配[]中列举的字符               |
| \d   | 匹配数字，即0-9                  |
| \D   | 匹配非数字                       |
| \s   | 匹配空白，即空格，tab键          |
| \S   | 匹配非空白                       |
| \w   | 匹配单词字符，即a-z, A-Z, 0-9, _ |
| \w   | 匹配非单词字符                   |

###匹配多个字符

| 字符  | 功能                                                         |
| ----- | ------------------------------------------------------------ |
| *     | 匹配前一个字符出现0次或者无限次，即可有可无，“.*”表示匹配所有 |
| +     | 匹配前一个字符出现1次或者无限次，即至少有1次                 |
| ？    | 匹配前一个字符出现1次或者0次，即要么有1次，要么没有          |
| {m}   | 匹配前一个字符出现m次                                        |
| {m,n} | 匹配前一个字符出现从m次到n次                                 |

**案例：**

```python 
re.match(r"速度与激情/d{1,3}","速度与激情12")   #表示三位数字

re.match(r"\d{10}","1234567890")     #表示十一位数

re.match(r"\d{3,4}-?\d{7,8}","0530-1234567")
```

###匹配开头结尾

| 字符 | 功能           |
| ---- | -------------- |
| ^    | 匹配字符串开头 |
| $    | 匹配字符串结尾 |

**案例：**

```python
import re

def main():
    names = ["age","_age","1age","age1","a_age","age_1_","age!","a#123","____"]
    ret = re.match(r"^[a-bA-B_][a-bA-B0-9_]*$",name)
    if ret:
        print("变量名：%s  符合要求....通过正则匹配出来的数据是：%s" % (name,ret.group()))
    else:
        print("变量名：%s  不符合要求" % name)
        
if __name__ == "__main__":
    main()
```

**案例：**

```python 
import re

def main():
    email = input("请输入一个邮箱地址：")
    #如果在正则表达式中使用到普通符号，比如：.和？等。需要在他们前面加一个反斜杠进行转义（\）
    ret = re.match(r"[a-zA-Z_0-9]{4,20}@163\.com$",email)
    if ret:
        print("%s 符合要求..." % email)
    else:
        print("%s 不符合要求..." % email)
if __name__ == "__main__":
    main()
```

###匹配分组

| 字符          | 功能                             |
| ------------- | -------------------------------- |
| \|            | 匹配左右任意一个表达式           |
| （ab）        | 将括号中的字符作为一个分组       |
| \num          | 引用分组num匹配到的字符串        |
| （？P<name>） | 分组起别名                       |
| （？P=name）  | 引用别名为name分组匹配到的字符串 |

**案例：**

```python 
re.match(r"[a-zA-Z0-9_]{4,20}@（126|163）\.com$","langwang@126.com").group()
输出：langwang@126.com

re.match(r"[a-zA-Z0-9_]{4,20}@（126|163）\.com$","langwang@126.com").group(1)
输出：126

re.match(r"（[a-zA-Z0-9_]{4,20}）@（126|163）\.com$","langwang@126.com").group(1)
输出：langwang

html = "<body><h1>hahhhah</h1></body>"
re.match(r"<(\w*)><(\w*)>.*</\2></\1>",html).group()
输出："<body><h1>hahhhah</h1></body>"

re.match(r"<(？P<P1>\w*)><(?P<P2>\w*)>.*</?P=P2></?P=P1>",html).group()

```

###特殊正则表达式

```python
[\u4e00-\u9fa5]     #匹配简体中文的正则表达式
```

##python  File和流

###打开文件

**open()方法:**

功能：用于打开文件，并返回文件对象。如果文件无法被打开，会抛出`OSError`错误。

注意：使用`open()`方法一定要关闭文件对象，即使用`close()` 。

格式：`open(file,mode = 'r')`

完整的语法格式为：

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

参数说明:

- file: 必需，文件路径（相对或者绝对路径）。
- mode: 可选，文件打开模式
- buffering: 设置缓冲
- encoding: 一般使用utf8
- errors: 报错级别
- newline: 区分换行符
- closefd: 传入的file参数类型
- opener:

mode 参数有：

| 模式 | 描述                                                         |
| ---- | ------------------------------------------------------------ |
| t    | 文本模式 (默认)。                                            |
| x    | 写模式，新建一个文件，如果该文件已存在则会报错。             |
| b    | 二进制模式。                                                 |
| +    | 打开一个文件进行更新(可读可写)。                             |
| U    | 通用换行模式（不推荐）。                                     |
| r    | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
| rb   | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。 |
| r+   | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
| rb+  | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。 |
| w    | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb   | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。 |
| w+   | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb+  | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。 |
| a    | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| ab   | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+   | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

默认为文本模式，如果要以二进制模式打开，加上 b 。

###file 对象

file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：

| 序号               | 方法及描述                                                   |
| ------------------ | ------------------------------------------------------------ |
| `file.close()`     | 关闭文件。关闭后文件不能再进行读写操作。                     |
| 2                  | [file.flush()](http://www.runoob.com/python3/python3-file-flush.html)刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。 |
| 3                  | [file.fileno()](http://www.runoob.com/python3/python3-file-fileno.html)返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。 |
| 4                  | [file.isatty()](http://www.runoob.com/python3/python3-file-isatty.html)如果文件连接到一个终端设备返回 True，否则返回 False。 |
| 5                  | [file.next()](http://www.runoob.com/python3/python3-file-next.html)返回文件下一行。 |
| `file.read()`      | [file.read([size\])](http://www.runoob.com/python3/python3-file-read.html)从文件读取指定的字节数，如果未给定或为负则读取所有。 |
| `file.readline()`  | [file.readline([size\])](http://www.runoob.com/python3/python3-file-readline.html)读取整行，包括 "\n" 字符。 |
| `file.readlines()` | [file.readlines([sizeint\])](http://www.runoob.com/python3/python3-file-readlines.html)读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。 |
| `file.seek()       | [file.seek(offset[, whence\])](http://www.runoob.com/python3/python3-file-seek.html)设置文件当前位置 |
| `file.tell()`      | [file.tell()](http://www.runoob.com/python3/python3-file-tell.html)返回文件当前位置。 |
| 11                 | [file.truncate([size\])](http://www.runoob.com/python3/python3-file-truncate.html)从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。 |
| `file.write()`     | [file.write(str)](http://www.runoob.com/python3/python3-file-write.html)将字符串写入文件，返回的是写入的字符长度。 |
| 13                 | [file.writelines(sequence)](http://www.runoob.com/python3/python3-file-writelines.html)向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。 |

###基本的文件方法

####读和写

**读文件**

```python
f = open('/Users/michael/test.txt', 'r')
f.read()
f.close()
```

- 如果文件不存在，`open()`函数就会抛出一个`IOError`的错误。
- 如果文件打开成功，接下来，调用`read()`方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示。
- 最后一步是调用`close()`方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的。

由于文件读写时都有可能产生`IOError`，一旦出错，后面的`f.close()`就不会调用。所以，为了保证无论是否出错都能正确地关闭文件,使用下面得方法：

```python
with open('/path/to/file', 'r') as f:
    print(f.read())
```

**写文件**

```python
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
f.close()

#以变量命名文件名
#方法一：
df = open('./data/' + city +'.csv', 'w')
#方法二：
city = 2
df = open('./data/%s.csv' % (city))
df.write(result + '\n')
```

- 写文件和读文件是一样的，唯一区别是调用`open()`函数时，传入标识符`'w'`或者`'wb'`表示写文本文件或写二进制文件.
- 反复调用`write()`来写入文件，但是务必要调用`f.close()`来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用`close()`方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用`close()`的后果是数据可能只写了一部分到磁盘，剩下的丢失了。

常用方式：

```python
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
```

#### 字符编码

要读取非UTF-8编码的文本文件，需要给`open()`函数传入`encoding`参数，例如，读取GBK编码的文件：

```python
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
f.read()
输出：'测试'
```

遇到有些编码不规范的文件，你可能会遇到`UnicodeDecodeError`，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，`open()`函数还接收一个`errors`参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

```python
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
```

#### 二进制文件

前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用`'rb'`模式打开文件即可：

```python
f = open('/Users/michael/test.jpg', 'rb')
f.read()
输出：b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
```

####读写行

`file.readline()`读取一个文件中的所有行，并将其作为列表返回。读取换行符。

`file.writelines()`写入一个字符串的列表，程序不会增加新行，需要自行添加。

####关闭文件

｀file.close()`



## python算法

链接：http://python.jobbole.com/81453/

编程的基本算法：推导、递归和规约。

Induction(推导)和Recursion(递归)其实彼此相互对应，也就是说一个Induction能够写出一个相应的Recursion，而一个Recursion也正好对应着一个Induction式子，也可以换个方式理解，Induction是从n-1到n的推导，而Recursion是从n到n-1的递归(下面有附图可以帮助理解)。

此外，Induction和Recursion其实都是某种Reduction，即Induction和Recursion的本质就是对问题进行规约！为了能够对问题使用Induction或者说Recursion，Reduction一般是将一个问题变成另一个只是规模减小了的相同问题。

### Reduction(规约)

Reduction(规约)意味着对问题进行转换。例如将一个未知的问题转换成我们能够解决的问题，转换的过程可能涉及到对问题的输入输出的转换。

### Induction(推导)

Induction(推导)是一个数学意义上的推导，类似数学归纳法，主要是用来证明某个命题是正确的。

首先我们证明对于基础情况(例如在k=1时)是正确的，然后证明该命题递推下去都是正确的(一般假设当k=n-1时是正确的，然后证明当k=n时也是正确的即可)

### Recursion(递归)

Recursion(递归)经常发生于一个函数调用自身的情况。



# re模块

**正则表达式（Regular Expression）**是字符串处理的常用工具，通常被用来检索、替换那些符合某个模式（Pattern）的文本。在 Python 中是通过**re 模块** 提供对正则的支持。

## re模块的使用过程

```python 
#coding=utf-8
import re
#使用match()进行匹配操作
result = re.match(正则表达式，要处理的字符串)
#re.match(r"速度与激情/d","速度与激情3")
#使用group()方法来提取匹配到的数据
result.group()
```

## re模块功能用法

### search()

不用从头开始匹配。

需求：匹配出文章阅读的次数

```python
#coding=utf-8
import re

ret = re.search(r"\d+","阅读次数为 9999")
ret.group()

输出：'9999'
```

### findall()

 ```python 
#coding=utf-8
import re

ret = re.findall(r"\d+","python = 9999, c = 4554, c++ = 2432")
print(ret)

输出：
['9999','4554','2432']

 ```

### sub()

将匹配到的数据进行替换。

**方法1：**

```python
#coding=utf-8
import re

ret = re.sub(r"\d+",'998',"python = 997")
print(ret)

输出：python = 998
```

### split()

根据匹配切割字符串，并返回一个列表

```python
#coding=utf-8
import re

ret = re.split(r":| ","info:xiaozhang 33 shangdong")
print(ret)

输出：['info','xiaozhang','33','shangdong']
```



# numpy

## 常用函数

### np.abs()

功能：求绝对值。

### np.reshape()

```python
z = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]])

print(z)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
'''
print(z.shape)
#(4, 4)
print(z.reshape(-1))
#[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16]
print(z.reshape(-1,1))  
#我们不知道z的shape属性是多少，
#但是想让z变成只有一列，行数不知道多少，
#通过`z.reshape(-1,1)`，Numpy自动计算出有16行，
#新的数组shape属性为(16, 1)，与原来的(4, 4)配套。
'''
[[ 1]
 [ 2]
 [ 3]
 [ 4]
 [ 5]
 [ 6]
 [ 7]
 [ 8]
 [ 9]
 [10]
 [11]
 [12]
 [13]
 [14]
 [15]
 [16]]
'''
print(z.reshape(2,-1))
'''
[[ 1  2  3  4  5  6  7  8]
 [ 9 10 11 12 13 14 15 16]]
'''
```

### np.tile(A,reps)

功能：通过重复reps次A来构造出一个新数组。 

```python
import numpy as np
a = np.array([0, 1, 2])
print np.tile(a, 2)
#array([0, 1, 2, 0, 1, 2])

print np.tile(a, (2, 2))
'''
array([[0, 1, 2, 0, 1, 2],
       [0, 1, 2, 0, 1, 2]])
'''
print np.tile(a, (2, 1, 2))
'''
array([[[0, 1, 2, 0, 1, 2]],
       [[0, 1, 2, 0, 1, 2]]])
'''
```

# pandas

## DataFrame

### 数据格式转换

**将数据转为list列表**

```python
#对于文本文件
df = pd.read_csv(file) #pd.dataframe
data_ndarray = np.array(df)#np.ndarray()
data_list=data_ndarray.tolist()#list

#对于SQL
data = spark.sql(sql)
df = data.toPandas()
data_ndarray = np.array(df)#np.ndarray()
data_list=data_ndarray.tolist()#list

#对于spark RDD数据
rdd = sc.textFile(file)
df = rdd.toDF
data_list = rdd.collect()

#将list转化为dataframe
from pandas.core.frame import DataFrame
a=[[1,2,3,4],[5,6,7,8]]
data=DataFrame(a)#这时候是以行为标准写入的
data.rename(columns={0:'a',1:'b'},inplace=True)#注意这里0和1都不是字符串
```

### 查看数据

```python
#查看首或者尾数据
df.head()
df.tail()
#显示数据框的索引
df.index
#显示列名
df.columns
#显示值（所有值）
df.values
#显示数据的简短统计摘要
df.describe()
#数据转置
df.T
#通过轴来分类你的数据（相当于排序，axis=1可以理解为分类列名，=0则为索引名）
df.sort_index(axis=1, ascending=False)
#通过值来分类
df.sort_values(by='B')
#多列排序
df.sort_values(by=['A','B'],ascending=(True,False))
#查看行数和列数
df.shape()
#查看索引、数据类型和内存信息
df.info()

```

### 选择数据

```python
#在方括号中输入这个单一的列名，来获得一个Series，该操作相当于df.A
df['A']  #以Series的形式返回列
#通过对行切片来获取数据
df[0:5]   #表示前5个样本
#用标签来截取一行数据
df[[0]]
#在多个轴上通过标签来选取数据
df.loc[:,['A','B']]
df[['A','B']]   #以DataFrame形式返回多列
#同时用标签切片和标签名索引来获取数据
df.loc[1:10,['A','B']]

#查看第几个样本的所有数据
df.iloc[3]
df.iloc[3:5,0:2]  #3到5个样本的前两个字段


#使用isin()方法来过滤数据
df2[df2['E'].isin(['two','four'])]

#过滤一定条件的数据
twelve_test = datass[datass['twelvediff']==0]
```

#### 分组统计

相关链接：https://blog.csdn.net/bqw18744018044/article/details/80011090

1. 统计两列数据出现的次数

```python
count = twelve_test.groupby(['twelve_bubble_cnt', 'twelve_bubble']).count()
```

2. 统计分组后的比重

```python 
count = datass.groupby(['twelve_bubble_cnt', 'twelve_bubble']).count()
# reset_index，原行索引作为一列保留，列名为index
count_all = count.reset_index()
p = count_all.groupby(['twelve_bubble_cnt','twelve_bubble']).sum() / cou.groupby('twelve_bubble_cnt').sum()
```



### 数据清理

```python
#重命名列名
df.columns = ['a','b','c']
#批量更改列名
df.rename(columns=lambda x: x + 1)
#选择性更改列名
df.rename(columns={'old_name': 'new_ name'})
#更改索引列
df.set_index('column_one')
#批量重命名索引
df.rename(index=lambda x: x + 1)

#缺失值
#检查DataFrame对象中的空值，并返回一个Boolean数组,缺失值为Ture
pd.isnull(df)
#检查DataFrame对象中的非空值，并返回一个Boolean数组
pd.notnull(df)
#删除所有包含空值的行
df.dropna()
#删除所有包含空值的列
df.dropna(axis=1)
#删除所有小于n个非空值的行
df.dropna(axis=1,thresh=n)
#用5替换DataFrame对象中所有的空值
df.fillna(value=5)

#df['A']  #以Series的形式返回列
#将Series中的数据类型更改为float类型
s.astype(float)
#用‘one’代替所有等于1的值
s.replace(1,'one')
#用'one'代替1，用'three'代替3
s.replace([1,3],['one','three'])

#数据去重
df.drop_duplicates(['trace_id'])
```

### 数据处理

```python
#选择col列的值大于0.5的行
df[df[col] > 0.5]
df[df.col > 0.5]

#排序
#按照列col1排序数据，默认升序排列
df.sort_values(col1)
#按照列col2降序排列数据
df.sort_values(col2, ascending=False)
#先按列col1升序排列，后按col2降序排列数据
df.sort_values([col1,col2], ascending=[True,False])

#分组运算
#返回一个按列col进行分组的Groupby对象
df.groupby(col)
#返回一个按多列进行分组的Groupby对象
df.groupby([col1,col2])
#返回按列col1进行分组后，列col2的均值
df.groupby(col1)[col2]
#返回按列col1分组的所有列的均值
df.groupby(col1).agg(np.mean)
#创建一个按列col1进行分组，并计算col2和col3的最大值的数据透视表
df.pivot_table(index=col1, values=[col2,col3], aggfunc=max)

#应用：对数据进行函数的应用
#对DataFrame中的每一列应用函数np.mean
data.apply(np.mean)
#对DataFrame中的每一行应用函数np.max
data.apply(np.max,axis=1)
df.apply(lambda x: x.max() - x.min())
```

### 数据合并 

```python
#将df2中的行添加到df1的尾部
df1.append(df2)

#将df2中的列添加到df1的尾部
df.concat([df1, df2],axis=1)
#用concat()函数来连接pandas对象
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)

#对df1的列和df2的列执行SQL形式的join
df1.join(df2,on=col1,how='inner')

#链接两个数据表
pd.merge(dataframe1, dataframe2, how='left', on=['city_id','is_short'])

```

### 数据统计

```python
#查看数据值列的汇总统计
df.describe()
#返回所有列的均值
df.mean()
#返回列与列之间的相关系数
df.corr()
#返回每一列中的非空值的个数
df.count()
df.drop_duplicates(['trace_id']).count()
#返回每一列的最大值
df.max()
#返回每一列的最小值
df.min()
#返回每一列的中位数
df.median()
#返回每一列的标准差
df.std()

#统计值的频数
df['A'].value_counts()
```

### 输入/输出数据

```python
#把数据输出为csv文件
df.to_csv('foo.csv')
#读取csv文件
pd.read_csv('foo.csv')

#写出一个excel文件
df.to_excel('foo.xlsx', sheet_name='Sheet1')
#读入一个excel文件
pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
```

### Attributes and underlying data

#### DataFrame.values

功能：把Pandas中的dataframe转成numpy中的array。

### Function application, GroupBy & Window

#### DataFrame.groupby().agg()

链接：https://www.cnblogs.com/lemonbit/p/6810972.html

**简介**

分组（group by）一般是指三个过程 

- 分割（Splitting）将数据按照某个标准分组 
- 应用（Applying）对每个分组分别使用函数 
- 组合（Combining）将结果组合成数据框 
  当然还有更多的操作比如： 
- 聚合(Aggregation) 同时对分组进行多种计算，比如同时计算sum和means 
- 变换(Transformation) 标准化分组数据，根据组数据填充组空值 
- Filtration(

### Serialization / IO / Conversion

#### DataFrame.to_csv()

```python
datafrme.to_csv('name.csv')
```

# datetime

### datatime

```python
#1.获取时间
#获取当前时间
import datetime
datetime.datetime.now()

#获取前一周的时间
import datetime
time = datetime.datetime.now() - datetime.timedelta(days = 7)

#设置开始结束时间
end_date =  datetime.datetime.now() - datetime.timedelta(days = 9)
start_date = end_date - datetime.timedelta(days = 7)

#时间格式转换
#datetime -> string
datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#输出：'2015-01-12 23:13:08'

#datetime <- string
datetime.datetime.strptime("2014-12-31 18:20:10", "%Y-%m-%d %H:%M:%S")
#输出：datetime.datetime(2014, 12, 31, 18, 20, 10)

```

# matplotlib

## 绘图

### 常用函数

```python 
#修改上下界
plt.xlim(xmax=7,xmin=0)
plt.ylim(ymax=7,ymin=0)

#添加标题
plt.title("I'm a scatter diagram.") 

#给x,y命名
plt.xlabel("x")
plt.ylabel("y")

#加标注
plt.annotate("(3,6)", xy = (3, 6), xytext = (4, 5), arrowprops = dict(facecolor = 'black', shrink = 0.1))

#画子图，221表示2*2四个图的第一个
plt.subplot(221)

#保存图
plt.savefig('a.png')

#多项式函数np.poly1d()
fit = [2,3]
fit_fn = np.poly1d(fit)
print(fit_fn)  #输出：2x+3
```



### 散点图

```python
import matplotlib
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,3,4,5]

#创建图并命名
plt.figure('Scatter fig')
#设置x轴、y轴名称
ax = plt.gca()
ax.set_xlabel('x')
ax.set_ylabel('y')

#画散点图
#参数c指定点的颜色，s指定点的大小,alpha指定点的透明度
ax.scatter(x, y, c='r', s=30, alpha=0.5)

plt.show()
```

### 直线

```python 
import matplotlib.pyplot as plot

x_list = [1,2,3,4]
y_list = [1,2,3,4]

#创建图并命名
plt.figure('Line fig')
ax = plt.gca()
#设置x轴、y轴名称
ax.set_xlabel('x')
ax.set_ylabel('y')

#画连线图
#参数c指定连线的颜色，linewidth指定连线宽度，alpha指定连线的透明度
ax.plot(x_list, y_list, color='r', linewidth=1, alpha=0.6)

plt.show()
```

### 直方图

```python 
import matplotlib.pyplot as plot

#数据
x_list = [1,2,3,4]
y_list = [1,2,3,4]

plt.figure('Bar fig')
ax = plt.gca()
ax.set_xlabel('value')
ax.set_ylabel('count')

#edgecolor指定每个直方的边框颜色
#传入的xticks与y_list的长度必须相等！
ax.bar(x_list, y_list, width=0.5,
       edgecolor='none')

plt.show()
```

**并列直方图**

```python 
import numpy as np
import matplotlib.pyplot as plt

size = 5
x = np.arange(size)
a = np.random.random(size)
b = np.random.random(size)
c = np.random.random(size)

total_width, n = 0.8, 3
width = total_width / n
x = x - (total_width - width) / 2

plt.bar(x, a,  width=width, label='a')
plt.bar(x + width, b, width=width, label='b')
plt.bar(x + 2 * width, c, width=width, label='c')
plt.legend()
plt.show()
```



### 双Y轴图

```python
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y2 = [1,2,3,4]
y1 = [4,3,2,1]

fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.bar(x, y1)
ax1.set_ylabel('y1')
ax1.set_title("双y轴图")

ax2 = ax1.twinx()  # this is the important function
ax2.plot(x, y2, 'r')
ax2.set_ylabel('y2')
ax2.set_xlabel('x')
ax2.scatter(x,y2,c='r')

plt.show()
```

### 折线图

```python
import matplotlib.pyplot as plt

#折线图
x = [5,7,11,17,19,25]#点的横坐标
k1 = [0.8222,0.918,0.9344,0.9262,0.9371,0.9353]#线1的纵坐标
k2 = [0.8988,0.9334,0.9435,0.9407,0.9453,0.9453]#线2的纵坐标
plt.plot(x,k1,'s-',color = 'r',label="ATT-RLSTM")#s-:方形
plt.plot(x,k2,'o-',color = 'g',label="CNN-RLSTM")#o-:圆形
plt.xlabel("region length")#横坐标名字
plt.ylabel("accuracy")#纵坐标名字
plt.legend(loc = "best")#图例
plt.show()
```

### 条形图（分布）



# python    json  

链接：https://python3-cookbook.readthedocs.io/zh_CN/latest/c06/p02_read-write_json_data.html	

## 基本使用     

作用：读写JSON数据。读写JSON(JavaScript Object Notation)编码格式的数据。

json` 模块提供了一种很简单的方式来编码和解码JSON数据。 ` 

主要的函数是 `json.dumps()` 和 `json.loads()` 。 

将一个Python数据结构转换为JSON：

```python
import json

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}

json_str = json.dumps(data)
```

将一个JSON编码的字符串转换回一个Python数据结构：

```python
data = json.loads(json_str)
```

如果你要处理的是文件而不是字符串，你可以使用 `json.dump()` 和 `json.load()` 来编码和解码JSON数据。

例如：

```python
# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)
```

## 讨论

JSON编码支持的基本数据类型为 `None` ， `bool` ， `int` ， `float` 和 `str` ， 以及包含这些类型数据的lists，tuples和dictionaries。 对于dictionaries，keys需要是字符串类型(字典中任何非字符串类型的key在编码时会先转换为字符串)。 为了遵循JSON规范，你应该只编码Python的lists和dictionaries。 而且，在web应用程序中，顶层对象被编码为一个字典是一个标准做法。

JSON编码的格式对于Python语法而已几乎是完全一样的，除了一些小的差异之外。 比如，True会被映射为true，False被映射为false，而None会被映射为null。 下面是一个例子，演示了编码后的字符串效果：

```python
>>> json.dumps(False)
＃输出：'false'
>>> d = {'a': True,
...     'b': 'Hello',
...     'c': None}
>>> json.dumps(d)
＃输出：'{"b": "Hello", "c": null, "a": true}'

```

# python tornado

Tornado，一个编写易创建、扩展和部署的强力Web应用的梦幻选择。本文是对Tornado Web服务器进行一个概述，通过框架基础、一些示例应用和使用的最佳实践来引导。

## 案例

### 简单的web使用

tornado是一个编写对HTTP请求响应的框架。下面是一个全功能的Tornado应用的基础示例：

```python
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
```

在浏览器中输入：http://127.0.0.1:8000/

输出：　Hello, friendly user!

### 字符串服务

```python
import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])

class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/reverse/(\w+)", ReverseHandler),
            (r"/wrap", WrapHandler)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
```

这个程序是一个通用的字符串操作的Web服务端基本框架。可以用它做两件事情。

- 其一，到`/reverse/string`的GET请求将会返回URL路径中指定字符串的反转形式。
- 其二，到`/wrap`的POST请求将从参数text中取得指定的文本，并返回按照参数width指定宽度装饰的文本。下面的请求指定一个没有宽度的字符串，所以它的输出宽度被指定为程序中的get_argument的默认值40个字符。

### 关于RequestHandler类

每个RequestHandler类都只定义了一个HTTP方法的行为。

#### HTTP的状态码

- 404 Not Found

Tornado会在HTTP请求的路径无法匹配任何RequestHandler类相对应的模式时返回404（Not Found）响应码。

- 400 Bad Request

如果你调用了一个没有默认值的get_argument函数，并且没有发现给定名称的参数，Tornado将自动返回一个400（Bad Request）响应码。

- 405 Method Not Allowed

如果传入的请求使用了RequestHandler中没有定义的HTTP方法（比如，一个POST请求，但是处理函数中只有定义了get方法），Tornado将返回一个405（Methos Not Allowed）响应码。

- 500 Internal Server Error

当程序遇到任何不能让其退出的错误时，Tornado将返回500（Internal Server Error）响应码。你代码中任何没有捕获的异常也会导致500响应码。

- 200 OK

如果响应成功，并且没有其他返回码被设置，Tornado将默认返回一个200（OK）响应码。

### 案例

```python
#-*- coding: UTF-8 -*-
import time
import gensim

import json
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import logging
define("port", default=8081, help="run on the give port", type=int)
logging.basicConfig(level=logging.INFO)

class HbaseConnet:
    def __init__(self):
        self.model = ""
        #self.model = gensim.models.Word2Vec.load('./data/emontionalModel2')
    def get_topN_word(self, n,word):
        n = int(n)
        #res = self.model.most_similar(word, topn=n)
        return {"res": 11111111111}
        #return {"res": str(n)+word}
        # return self.model.most_similarity(word, n)

class indexHandler(tornado.web.RequestHandler):
    # get: 浏览器拼url, 新闻后面的参数
    def get(self):
        # self.get_argment获取参数
        key1 = self.get_argument("n")
        key2 = self.get_argument("word")
        res = H.get_topN_word(key1,key2)
        # res = {"a": 1}
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(res, ensure_ascii=False, indent=4, separators=(',', ': ')))

if __name__ == "__main__":
    # http://127.0.0.1:8081/word2vec?n=1&word=iii
    tornado.options.parse_command_line()
    logging.info("start init model...")
    H = HbaseConnet()
    logging.info("start application...")
    app = tornado.web.Application(handlers=[(r"/word2vec", indexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
```

在浏览器中输入：　http://127.0.0.1:8081/word2vec?n=1&word=iii



# 数据处理

## 数据格式

```python
#从hive中获取数据
data = spark.sql(sql)
data_df = data.toPandas()
#将dataframe格式转换为list
data_ndarray = np.array(data_df)#np.ndarray()
data_list=data_ndarray.tolist()#list
#对数据进行处理
for i in range(len(data_list)):
    data_list[i][0] = float(eval(data_list[i][1])['1.00_1'])
    data_list[i][1] = float(eval(data_list[i][1])['1.00_2'])
print data_list[:4]
#奖list转换为dataframe格式
from pandas.core.frame import DataFrame
data_dp =DataFrame(data_list)
data_dp.rename(columns={0:'ecr_you',1:'ecr_kuai',2:'label_you',3:'label_kuai'},inplace=True)
#计算auc
from sklearn.metrics import roc_auc_score
print roc_auc_score(data_dp['label_you'], data_dp['ecr_you'])
print roc_auc_score(data_dp['label_kuai'], data_dp['ecr_kuai'])
```



