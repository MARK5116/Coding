# python基础

## 转移字符

| 转义字符 | 输出               |
| -------- | ------------------ |
|          | '                  |
| \"       | "                  |
| \a       | ‘bi’响一声         |
| \b       | 退格               |
| \f       | 换页（在打印时）   |
| \n       | 回车，光标在下一行 |
| \r       | 换行，光标在上一行 |
| \t       | 八个空格，即tab键  |
| \\       | \                  |

##python数据结构

###数组

**二维数组**

```python
len(array)     #数组行数 row
len(array[0])  #数组列数 column
```

###字符串

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
print(' ',join(str(x) for x in b_list))
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



### 字典

列表适合于将值组织到一个结构中，可以通过编号进行引用；然而字典可以通过名字来引用值。字典也可以称为映射。

字典是无序的对象集合，通过键值存取的。字典用：“{}”标识，由键（key）和键值（value）组成。键(key)必须使用不可变类型。在同一个字典中，键(key)必须是唯一的。

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
print(c)         #{'gender': 'male', 'name': 'Allen', 'age': 14}
```

- 字典键值元组表

```python
e=dict([('name','Allen'),('age',21),('gender','male')])
print(e)       #{'age': 21, 'name': 'Allen', 'gender': 'male'}
```

- 所有的键值都相同，或者赋予初始值

```python
 f=dict.fromkeys(['height','weight'],'normal')
print(f)      #{'weight': 'normal', 'height': 'normal'}
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

#### 字典基本操作

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

#### 字典方法（待定）

##内置函数

###eval()	repr()	isinstance()

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
df = open('./data/' + city +'.csv', 'w')
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

# pandas

## DataFrame

### Reindexing / Selection / Label manipulation

#### DataFrame.drop_duplicates()

功能：去除DataFrame的重复项。

```python 
dat_2 = dat.drop_duplicates(['trace_id'])
```

### Computations / Descriptive Stats

#### DataFrame.count()

功能：统计DataFrame的数量。

```python
data_1 = data.drop_duplicates(['trace_id']).count()
```

### Attributes and underlying data

#### DataFrame.values

功能：把Pandas中的dataframe转成numpy中的array。

### Combining / joining / merging

#### DataFrame.merge()

```python
result = pd.merge(dataframe1, dataframe2, how='left', on=['city_id','is_short'])
```

说明：1. Dataframe1和dataframe2为两个数据表。

1. how为连接方式，
2. on指定以哪些列连接。

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

