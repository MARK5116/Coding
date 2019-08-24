# 常用技巧

**问题：对于’1,2,3,4,5’这样的字符串输出采用,分隔开的1 2 3 4 5**

```shell
#解决方法1：
!/bin/bash
var=’1,2,3,4,5’
var=${var//,/ }    #这里是将var中的,替换为空格
for element in $var 
do
    echo $element
done
```

# echo命令

Shell 的 echo 指令与 PHP 的 echo 指令类似，都是用于字符串的输出。命令格式：

```shell
echo string
```

您可以使用echo实现更复杂的输出格式控制。

**1.显示普通字符串:**

```shell
echo It is a test
#输出It is a test
```

**2.显示转义字符**

```shell
echo "\"It is a test\""
#输出："It is a test"
```

双引号也可以省略

**3.显示变量**

read 命令从标准输入中读取一行,并把输入行的每个字段的值指定给 shell 变量

```shell
#!/bin/sh
read name 
echo "$name It is a test"
```

以上代码保存为 test.sh，name 接收标准输入的变量，结果将是:

```
[root@www ~]# sh test.sh
OK                     #标准输入
OK It is a test        #输出
```

**4.显示换行**

```shell
echo -e "OK! \n" # -e 开启转义
echo "It is a test"
```

输出结果：

```
OK!

It is a test
```

**5.显示不换行**

```shell
#!/bin/sh
echo -e "OK! \c" # -e 开启转义 \c 不换行
echo "It is a test"
```

输出结果：

```
OK! It is a test
```

**6.显示结果定向至文件**

```shell
#1.
echo "It is a test" > myfile

#2.
echo log > /dev/null 2>&1
/dev/null ：代表空设备文件
>  ：代表重定向到哪里，例如：echo "123" > /home/123.txt
1  ：表示stdout标准输出，系统默认值是1，所以">/dev/null"等同于"1>/dev/null"
2  ：表示stderr标准错误
&  ：表示等同于的意思，2>&1，表示2的输出重定向等同于1
1 > /dev/null 2>&1 语句含义：
1 > /dev/null ： 首先表示标准输出重定向到空设备文件，也就是不输出任何信息到终端，说白了就是不显示任何信息。
2>&1 ：接着，标准错误输出重定向（等同于）标准输出，因为之前标准输出已经重定向到了空设备文件，所以标准错误输出也重定向到空设备文件。

#3.
sh run.sh main.conf > log 2>&1
#将运行结果都输出到log日志文件中
```

**7.原样输出字符串，不进行转义或取变量(用单引号)**

```shell
echo '$name\"'
```

输出结果：

```
$name\"
```

**8.显示命令执行结果**

```shell
echo `date`
```

注意：这里使用的是反引号 **`**, 而不是单引号 **'**。

结果将显示当前日期

```
Thu Jul 24 10:08:46 CST 2014
```