# 特殊应用

scp -P 8022 luban@10.84.179.170:/nfs/private/jihao/git/billing_item/script/cross_city/all_city_order.csv ./jihao

```shell
hadoop fs -cat /user/bigdata_driver_ecosys_test/liuzhu/pid_sd_features/explore_instance/20190418/part-00253 | head -100 > res

cat res | python Format_conversion.py
```



**python -m SimpleHTTPServer 8000 &**

说明：SimpleHTTPServer ——一个简单的HTTP服务器。



mvn clean package

# linux后台运行和关闭、查看后台任务

fg、bg、jobs、&、nohup、ctrl+z、ctrl+c 命令

**一、&**

加在一个命令的最后，可以把这个命令放到后台执行，如

```
watch  -n 10 sh  test.sh  &  #每10s在后台执行一次test.sh脚本
```

**二、ctrl + z**

可以将一个正在前台执行的命令放到后台，并且处于暂停状态。

**三、jobs**

查看当前有多少在后台运行的命令

jobs -l选项可显示所有任务的PID，jobs的状态可以是running, stopped, Terminated。但是如果任务被终止了（kill），shell 从当前的shell环境已知的列表中删除任务的进程标识。

**四、fg**

将后台中的命令调至**前台**继续运行。如果后台中有多个命令，可以用fg %jobnumber（是命令编号，不是进程号）将选中的命令调出。

**五、bg**

将一个在后台暂停的命令，变成在**后台**继续执行。如果后台中有多个命令，可以用bg %jobnumber将选中的命令调出。

**六、kill**

- 法子1：通过jobs命令查看job号（假设为num），然后执行kill %num
- 法子2：通过ps命令查看job的进程号（PID，假设为pid），然后执行kill pid

前台进程的终止：Ctrl+c

**七、nohup**

如果让程序始终在后台执行，即使关闭当前的终端也执行（之前的&做不到），这时候需要nohup。该命令可以在你退出帐户/关闭终端之后继续运行相应的进程。关闭中断后，在另一个终端jobs已经无法看到后台跑得程序了，此时利用ps（进程查看命令）

```
ps -aux | grep "test.sh"  #a:显示所有程序 u:以用户为主的格式来显示 x:显示所有程序，不以终端机来区分
```



#文件及目录管理

## 查找某个文件位置

我们经常在linux要查找某个文件，但不知道放在哪里了，可以使用下面的一些命令来搜索：

- which 查看可执行文件的位置。
- whereis 查看文件的位置。
- locate 配合数据库查看文件位置。
- find 实际搜寻硬盘查询文件名称。

# 命令大全

## 文件管理

### cat

cat 命令用于连接文件并打印到标准输出设备上。

语法格式：

```shell
cat [-AbeEnstTuv] [--help] [--version] fileName
```

参数说明：

**-n 或 --number**：由 1 开始对所有输出的行数编号。

**-b 或 --number-nonblank**：和 -n 相似，只不过对于空白行不编号。

**-s 或 --squeeze-blank**：当遇到有连续两行以上的空白行，就代换为一行的空白行。

实例：

1. 把 textfile1 的文档内容加上行号后输入 textfile2 这个文档里：

```
cat -n textfile1 > textfile2
```

2. 把 textfile1 和 textfile2 的文档内容加上行号（空白行不加）之后将内容附加到 textfile3 文档里：

```
cat -b textfile1 textfile2 >> textfile3
```

3. 清空 /etc/test.txt 文档内容：

```
cat /dev/null > /etc/test.txt
```

### chmod

Linux/Unix 的文件调用权限分为三级 : 文件拥有者、群组、其他。利用 chmod 可以藉以控制文件如何被他人所调用。

语法：

```shell
chmod [-cfvR] [--help] [--version] mode file...
```

参数说明：

mode : 权限设定字串，格式如下 :

```
[ugoa...][[+-=][rwxX]...][,...]
```

其中：

- u 表示该文件的拥有者，g 表示与该文件的拥有者属于同一个群体(group)者，o 表示其他以外的人，a 表示这三者皆是。
- \+ 表示增加权限、- 表示取消权限、= 表示唯一设定权限。
- r 表示可读取，w 表示可写入，x 表示可执行，X 表示只有当该文件是个子目录或者该文件已经被设定过为可执行。

其他参数说明：

- -c : 若该文件权限确实已经更改，才显示其更改动作
- -f : 若该文件权限无法被更改也不要显示错误讯息
- -v : 显示权限变更的详细资料
- -R : 对目前目录下的所有文件与子目录进行相同的权限变更(即以递回的方式逐个变更)
- --help : 显示辅助说明
- --version : 显示版本

实例：

1. 将文件 file1.txt 设为所有人皆可读取 :

```
chmod ugo+r file1.txt
```

2. 将文件 file1.txt 设为所有人皆可读取 :

```
chmod a+r file1.txt
```

3. 将文件 file1.txt 与 file2.txt 设为该文件拥有者，与其所属同一个群体者可写入，但其他以外的人则不可写入 :

```
chmod ug+w,o-w file1.txt file2.txt
```

4. 将 ex1.py 设定为只有该文件拥有者可以执行 :

```
chmod u+x ex1.py
```

5. 将目前目录下的所有文件与子目录皆设为任何人可读取 :

```
chmod -R a+r *
```

6. 此外chmod也可以用数字来表示权限如 :

```
chmod 777 file
```

语法：

```
chmod abc file
```

其中a,b,c各为一个数字，分别表示User、Group、及Other的权限。

r=4，w=2，x=1

- 若要rwx属性则4+2+1=7；
- 若要rw-属性则4+2=6；
- 若要r-x属性则4+1=5。

```
chmod a=rwx file
```

和

```
chmod 777 file
```

效果相同

```
chmod ug=rwx,o=x file
```

和

```
chmod 771 file
```

##find



## locate



### mv

mv命令用来为文件或目录改名、或将文件或目录移入其它位置。

mv参数设置与运行结果

| 命令格式         | 运行结果                                                     |
| ---------------- | ------------------------------------------------------------ |
| mv 文件名 文件名 | 将源文件名改为目标文件名                                     |
| mv 文件名 目录名 | 将文件移动到目标目录                                         |
| mv 目录名 目录名 | 目标目录已存在，将源目录 移动到目标目录；目标 目录不存在则改名 |
| mv 目录名 文件名 | 出错                                                         |

### paste

paste命令用于合并文件的列。

paste指令会把每个文件以列对列的方式，一列列地加以合并。

语法：

```
paste [-s][-d <间隔字符>][--help][--version][文件...]
```

参数：

- -d<间隔字符>或--delimiters=<间隔字符> 　用指定的间隔字符取代跳格字符。

- -s或--serial 　串列进行而非平行处理，即将一个文件合并为一行数据。

  

实例

1. 使用paste指令将文件"file"、"testfile"、"testfile1"进行合并，输入如下命令：

```shell
paste file testfile testfile1 #合并指定文件内容 
```

2. 若使用paste指令的参数"-s"，则可以将一个文件中的多行数据合并为一行进行显示。例如，将文件"file"中的3行数据合并为一行数据进行显示，输入如下命令

```shell
$ paste -s file          #合并指定文件的多行数据
```

注意：参数"-s"只是将testfile文件的内容调整显示方式，并不会改变原文件的内容格式。

### rm

rm命令用于删除一个文件或者目录。

参数：

- -i 删除前逐一询问确认。
- -f 即使原档案属性设为唯读，亦直接删除，无需逐一确认。
- -r 将目录及以下之档案亦逐一删除。

实例

1. 删除文件可以直接使用rm命令，若删除目录则必须配合选项"-r"，例如：

```shell
# rm  test.txt 
rm：是否删除 一般文件 "test.txt"? y  

# rm  -r  homework  
rm：是否删除 目录 "homework"? y 
```

2. 删除当前目录下的所有文件及目录，命令行为：

```
rm  -r  * 
```

文件一旦通过rm命令删除，则无法恢复，所以必须格外小心地使用该命令。

### touch

touch命令用于修改文件或者目录的时间属性，包括存取时间和更改时间。若文件不存在，系统会建立一个新的文件。

ls -l 可以显示档案的时间记录。

实例:

1. 使用指令"touch"修改文件"testfile"的时间属性为当前系统时间：

```shell
touch testfile             #修改文件的时间属性 
```

2. 使用该指令创建一个空白文件"file"：

```shell
touch file    #创建一个名为“file”的新的空白文件 
```

### which

功能：搜索某个系统命令的位置，并且返回第一个搜索结果。也就是说，使用which命令，就可以看到某个系统命令是否存在，以及执行的到底是哪一个位置的命令。

也就是查找Linux命令的。

实例：

1. 查找可执行文件的位置、显示命令所在路径

命令：

```shell
which pwd
```

## whereis

### cp

cp命令主要用于复制文件或目录。

参数说明：

- -r：若给出的源文件是一个目录文件，此时将复制该目录下所有的子目录和文件。

实例:

```shell
cp –r test/ newtest          
```

### scp

scp命令用于Linux之间复制文件和目录。

scp是 secure copy的缩写, scp是linux系统下基于ssh登陆进行安全的远程文件拷贝命令。

实例：

1. 从本地复制到远程

- 命令格式：

```shell
#1.scp local_file remote_username@remote_ip:remote_folder 
scp /home/space/music/1.mp3 root@www.runoob.com:/home/root/others/music 

#2. scp local_file remote_username@remote_ip:remote_file 
scp /home/space/music/1.mp3 root@www.runoob.com:/home/root/others/music/001.mp3 

#3. scp local_file remote_ip:remote_folder 
scp /home/space/music/1.mp3 www.runoob.com:/home/root/others/music 

#4. scp local_file remote_ip:remote_file 
scp /home/space/music/1.mp3 www.runoob.com:/home/root/others/music/001.mp3 

```

第1,2个指定了用户名，命令执行后需要再输入密码，第1个仅指定了远程的目录，文件名字不变，第2个指定了文件名；

第3,4个没有指定用户名，命令执行后需要输入用户名和密码，第3个仅指定了远程的目录，文件名字不变，第4个指定了文件名；

- 复制目录命令格式：

```shell
#1. scp -r local_folder remote_username@remote_ip:remote_folder 
scp -r /home/space/music/ root@www.runoob.com:/home/root/others/ 
 
#2. scp -r local_folder remote_ip:remote_folder 
scp -r /home/space/music/ www.runoob.com:/home/root/others/ 
```

第1个指定了用户名，命令执行后需要再输入密码；

第2个没有指定用户名，命令执行后需要输入用户名和密码；

2. 从远程复制到本地

```shell
scp root@www.runoob.com:/home/root/others/music /home/space/music/1.mp3 
scp -r www.runoob.com:/home/root/others/ /home/space/music/
```

说明:

1.如果远程服务器防火墙有为scp命令设置了指定的端口，我们需要使用 -P 参数来设置命令的端口号，命令格式如下：

```shell
#scp 命令使用端口号 4588
scp -P 4588 remote@www.runoob.com:/usr/local/sin.sh /home/administrator
#比如
scp -P 8022 luban@10.84.179.170:/nfs/private/jihao/git/billing_item/script/cross_city/all_city_order.csv ./jihao
```

2.使用scp命令要确保使用的用户具有可读取远程服务器相应文件的权限，否则scp命令是无法起作用的。

### shuf

功能：把输入行按随机顺序输出到标准输出。

举例：

1. 将文件以乱序的形式输出

```shell
$ shuf filename
```



### split

Linux split命令用于将一个文件分割成数个。

该指令将大文件分割成较小的文件，在默认情况下将按照每1000行切割成一个小文件。

实例:

1. 使用指令"split"将文件"README"每6行切割成一个文件，输入如下命令：

```
#方法一：
$ split -6 README     #将README文件每六行分割成一个文件 

方法二：
$ split -l 6
```

以上命令执行后，指令"split"会将原来的大文件"README"切割成多个以"x"开头的小文件。而在这些小文件中，每个文件都只有6行内容。

使用指令"ls"查看当前目录结构，如下所示：

```
$ ls                         #执行ls指令  
#获得当前目录结构  
README xaa xad xag xab xae xah xac xaf xai    
```

### awk

AWK是一种处理文本文件的语言，是一个强大的文本分析工具。简单来说awk就是把文件逐行的读入，以空格为默认分隔符将每行切片，切开的部分再进行各种分析处理。

参数：

- -F fs or --field-separator fs
  指定输入文件折分隔符，fs是一个字符串或者是一个正则表达式，如-F:。

举例：

1. awk -F  #-F相当于内置变量FS, 指定分割字符

```shell
echo base.yaml | awk -F "." '{print $1}'
#输出：base
echo base.yaml | awk -F "." '{print $1"\t"$2}'
#输出：base	yaml
```



## 文档编辑

### grep

Linux grep命令用于查找文件里符合条件的字符串。

grep指令用于查找内容包含指定的范本样式的文件，如果发现某文件的内容符合所指定的范本样式，预设grep指令会把含有范本样式的那一列显示出来。若不指定任何文件名称，或是所给予的文件名为"-"，则grep指令会从标准输入设备读取数据。

举例：

```shell
#以d开头的行
grep "^d"
#以-开头的行
grep "^-"

```

### wc

Linux wc命令用于计算字数。

利用wc指令我们可以计算文件的Byte数、字数、或是列数，若不指定文件名称、或是所给予的文件名为"-"，则wc指令会从标准输入设备读取数据。

**参数**：

- -c或--bytes或--chars 只显示Bytes数。
- -l或--lines 只显示行数。
- -w或--words 只显示字数。



## 文件传输



## 磁盘管理

### cd 

切换目录。

~  代表主目录，一般用户表示：/home/用户名；root用户表示：/root

cd ./ 代表进入当前目录

cd ../ 代表进入当前目录的父目录（既上级目录）

cd / 和cd ..// 代表进入系统根目录

cd .. 代表退到父目录

cd ../..// 代表实现进入当前目录的父目录的父目录

```
cd    进入用户主目录；
cd ~  进入用户主目录；
cd -  返回进入此目录之前所在的目录；
cd ..  返回上级目录（若当前目录为“/“，则执行完后还在“/"；".."为上级目录的意思）；
cd ../..  返回上两级目录；
cd !$  把上个命令的参数作为cd参数使用。
```

### df

df命令用于显示目前在Linux系统上的文件系统的磁盘使用情况统计。

实例

显示文件系统的磁盘使用情况统计：

```
# df 
Filesystem     1K-blocks    Used     Available Use% Mounted on 
/dev/sda6       29640780 4320704     23814388  16%     / 
udev             1536756       4     1536752    1%     /dev 
tmpfs             617620     888     616732     1%     /run 
none                5120       0     5120       0%     /run/lock 
none             1544044     156     1543888    1%     /run/shm 
```

- `Filesystem` – Linux 系统中的文件系统
- `1K-blocks` – 文件系统的大小，用 1K 大小的块来表示。
- `Used` – 以 1K 大小的块所表示的已使用数量。
- `Available` – 以 1K 大小的块所表示的可用空间的数量。
- `Use%` – 文件系统中已使用的百分比。
- `Mounted on` – 已挂载的文件系统的挂载点。

### du

du命令用于显示目录或文件的大小。

du会显示指定的目录或文件所占用的磁盘空间。

语法

```
du [-abcDhHklmsSx][-L <符号连接>][-X <文件>][--block-size][--exclude=<目录或文件>][--max-depth=<目录层数>][--help][--version][目录或文件]
```

**参数说明**：

- -a或-all 显示目录中个别文件的大小。
- -b或-bytes 显示目录或文件大小时，以byte为单位。
- -c或--total 除了显示个别目录或文件的大小外，同时也显示所有目录或文件的总和
- -h或--human-readable 以K，M，G为单位，提高信息的可读性。
- -H或--si 与-h参数相同，但是K，M，G是以1000为换算单位。
- -k或--kilobytes 以1024 bytes为单位
- -m或--megabytes 以1MB为单位

实例：

1. 显示目录或者文件所占空间:

```
# du
```

只显示当前目录下面的子目录的目录大小和当前目录的总的大小，最下面的1288为当前目录的总大小

显示指定文件所占空间

```
# du log2012.log 
300     log2012.log
```

方便阅读的格式显示test目录所占空间情况：

```
# du -h test
```

2. 显示路径下所占内存

```shell
#du -sh
```



### mkdir

mkdir命令用于建立名称为 dirName 之子目录。

### pwd

pwd命令用于显示工作目录。

执行pwd指令可立刻得知您目前所在的工作目录的绝对路径名称。

### ls

 ls命令用于显示指定工作目录下之内容（列出目前工作目录所含之文件及子目录)。

参数：

- -l 除文件名称外，亦将文件型态、权限、拥有者、文件大小等资讯详细列出
- -F 在列出的文件名称后加一符号；例如可执行档则加 "*", 目录则加 "/"

举例：

1. 列出所有文件的详细信息

```shell
ls -l        #列出所有文件的
ls -l *      #列出所有文件和子目录的文件
```

2. 只列出子目录

```shell
ls -F | grep /$ 
ls -l | grep "^d"
```

3. 计算当前目录下的文件数和目录数

```shell
#计算文件数
ls -l * |grep "^-"|wc -l
#计算目录数
ls -l * |grep "^d"|wc -l
#计算py文件的个数（以什么结尾的文件）
ls *.py | wc -l
```

说明：

ls -l     

长列表输出该目录下文件信息(注意这里的文件，不同于一般的文件，可能是目录、链接、设备文件等)

grep "^-"

这里将长列表输出信息过滤一部分，只保留一般文件，如果只保留目录就是 ^d

 wc -l

 统计输出信息的行数，因为已经过滤得只剩一般文件了，所以统计结果就是一般文件信息的行数，又由于一行信息对应一个文件，所以也就是文件的个数。

## 磁盘维护

### fdisk

## 网络通讯

### ifconfig

ifconfig命令用于显示或设置网络设备。

ifconfig可设置网络设备的状态，或是显示目前的设置。

### ping



## 系统管理

### date

Linux date命令可以用来显示或设定系统的日期与时间，在显示方面，使用者可以设定欲显示的格式，格式设定为一个加号后接数个标记，其中可用的标记列表如下：

时间方面：

- % : 印出 %
- %n : 下一行
- %t : 跳格
- %H : 小时(00..23)
- %I : 小时(01..12)
- %k : 小时(0..23)
- %l : 小时(1..12)
- %M : 分钟(00..59)
- %p : 显示本地 AM 或 PM
- %r : 直接显示时间 (12 小时制，格式为 hh:mm:ss [AP]M)
- %s : 从 1970 年 1 月 1 日 00:00:00 UTC 到目前为止的秒数
- %S : 秒(00..61)
- %T : 直接显示时间 (24 小时制)
- %X : 相当于 %H:%M:%S
- %Z : 显示时区

日期方面：

- %a : 星期几 (Sun..Sat)
- %A : 星期几 (Sunday..Saturday)
- %b : 月份 (Jan..Dec)
- %B : 月份 (January..December)
- %c : 直接显示日期与时间
- %d : 日 (01..31)
- %D : 直接显示日期 (mm/dd/yy)
- %h : 同 %b
- %j : 一年中的第几天 (001..366)
- %m : 月份 (01..12)
- %U : 一年中的第几周 (00..53) (以 Sunday 为一周的第一天的情形)
- %w : 一周中的第几天 (0..6)
- %W : 一年中的第几周 (00..53) (以 Monday 为一周的第一天的情形)
- %x : 直接显示日期 (mm/dd/yy)
- %y : 年份的最后两位数字 (00.99)
- %Y : 完整年份 (0000..9999)

若是不以加号作为开头，则表示要设定时间，而时间格式为 MMDDhhmm[[CC]YY][.ss]，其中 MM 为月份，DD 为日，hh 为小时，mm 为分钟，CC 为年份前两位数字，YY 为年份后两位数字，ss 为秒数。

当您不希望出现无意义的 0 时(比如说 1999/03/07)，则可以在标记中插入 - 符号，比如说 date '+%-H:%-M:%-S' 会把时分秒中无意义的 0 给去掉，像是原本的 08:09:04 会变为 8:9:4。另外，只有取得权限者(比如说 root)才能设定系统时间。

当您以 root 身分更改了系统时间之后，请记得以 clock -w 来将系统时间写入 CMOS 中，这样下次重新开机时系统时间才会持续抱持最新的正确值。

实例:

1. 显示当前时间

```
# date
三 5月 12 14:08:12 CST 2010
# date '+%c' 
2010年05月12日 星期三 14时09分02秒
# date '+%D' //显示完整的时间
05/12/10
# date '+%x' //显示数字日期，年份两位数表示
2010年05月12日
# date '+%T' //显示日期，年份用四位数表示
14:09:31
# date '+%X' //显示24小时的格式
14时09分39秒
# date '+%s' //显示时间戳
1559556409
```

2. 按自己的格式输出

```
# date '+usr_time: $1:%M %P -hey'
usr_time: $1:16 下午 -hey
```

3. 显示时间后跳行，再显示目前日期

```
date '+%T%n%D'
```

4. 显示月份与日数

```
date '+%B %d'
```

5. 显示日期与设定时间(12:34:56)

```
date --date '12:34:56'
```

### kill

Linux kill命令用于删除执行中的程序或工作。

**语法**

```
kill [-s <信息名称或编号>][程序]　或　kill [-l <信息编号>]
```

**参数说明**：

- -l <信息编号> 　若不加<信息编号>选项，则-l参数会列出全部的信息名称。
- -s <信息名称或编号> 　指定要送出的信息。
- [程序] 　[程序]可以是程序的PID或是PGID，也可以是工作编号。

**实例**

```
杀死进程
# kill 12345

强制杀死进程
# kill -KILL 123456

彻底杀死进程
# kill -9 123456
```

杀死指定用户所有进程

```
#kill -9 $(ps -ef | grep hnlinux) //方法一 过滤出hnlinux用户进程 
#kill -u hnlinux //方法二
```

### ps

Linux ps命令用于显示当前进程 (process) 的状态。

**语法**

```
ps [options] [--help]
```

**参数**：

- ps 的参数非常多, 在此仅列出几个常用的参数并大略介绍含义
- -A 列出所有的行程
- -w 显示加宽可以显示较多的资讯
- -au 显示较详细的资讯
- -aux 显示所有包含其他使用者的行程

**实例**

```
# ps -A 显示进程信息

#显示指定用户信息
# ps -u root //显示root进程用户信息

#显示所有进程信息，连同命令行
# ps -ef //显示所有命令，连带命令行
# ps -aux

#显示spark的进程
# ps aux | grep spark
```

### top

 top命令用于实时显示 process 的动态。

实例:

1. 显示进程信息

```
# top
```

### shutdown

shutdown命令可以用来进行关机程序.

实例:

1. 立即关机

```
# shutdown -h now
```

### sudo

sudo命令以系统管理者的身份执行指令，也就是说，经由 sudo 所执行的指令就好像是 root 亲自执行。

### free

free命令用于显示内存状态。

free指令会显示内存的使用情况，包括实体内存，虚拟的交换文件内存，共享内存区段，以及系统核心使用的缓冲区等。

实例:

1. 显示内存使用情况

```
# free //显示内存使用信息
total used free shared buffers cached
Mem: 254772 184568 70204 0 5692 89892
-/+ buffers/cache: 88984 165788
Swap: 524280 65116 459164
```

## 系统设置

### clear

clear命令用于清除屏幕。

### export

export命令用于设置或显示环境变量。

在shell中执行程序时，shell会提供一组环境变量。export可新增，修改或删除环境变量，供后续执行的程序使用。export的效力仅及于该次登陆操作。

实例

1. 列出当前所有的环境变量

```
# export -p //列出当前的环境变量值
```

2. 定义环境变量

```
# export MYENV //定义环境变量
# export -p //列出当前的环境变量
```

3. 定义环境变量赋值

```
# export MYENV=7 //定义环境变量并赋值
```

## 备份压缩

### tar

打包、压缩、解压文件。

实例：

```
1.压缩文件 非打包
# touch a.c       
# tar -czvf test.tar.gz a.c   //压缩 a.c文件为test.tar.gz

2.列出压缩文件内容
# tar -tzvf test.tar.gz 
-rw-r--r-- root/root     0 2010-05-24 16:51:59 a.c

3.解压文件
# tar -xzvf test.tar.gz 

4.打包，不压缩
tar -cvf test.tar test
```

## 设备管理



## 其他命令

### tail

常用：tail -f filename

tail 命令从指定点开始将文件写到标准输出.使用tail命令的-f选项可以方便的查阅正在改变的日志文件,tail -f filename会把filename里最尾部的内容显示在屏幕上,并且不但刷新,使你看到最新的文件内容. 

**命令功能：**

用于显示指定文件末尾内容，不指定文件时，作为输入信息进行处理。常用查看日志文件。

**命令参数：**

-f 循环读取

-q 不显示处理信息

-v 显示详细的处理信息

-c<数目> 显示的字节数

-n<行数> 显示行数

--pid=PID 与-f合用,表示在进程ID,PID死掉之后结束. 

-q, --quiet, --silent 从不输出给出文件名的首部 

-s, --sleep-interval=S 与-f合用,表示在每次反复的间隔休眠S秒 。

### sh

```
-c string：命令从-c后的字符串读取。
-i：实现脚本交互。
-n：进行shell脚本的语法检查。
-x：实现shell脚本逐条语句的跟踪。
```

例子：

```shell
sh run_main_current.sh main_current.conf > log 2>&1
```



# Vim命令

## 常用命令设置

```shell
"设置编码"
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8

"显示行号"
set nu
"突出显示当前行"
set cul
"突出显示当前列"
"set cuc"
"显示括号匹配"
set showmatch

"设置缩进"
"设置Tab长度为4空格"
set tabstop=4
"设置自动缩进长度为4空格"
set shiftwidth=4
"继承前一行的缩进方式，适用于多行注释"
set autoindent

"语法高亮
set syntax=on

"回车后自动缩进
"set autoindent
"set cindent

set ts=4
set expandtab
```



### 取消自动缩进

:set noautoindent

:set paste

### 注释与反注释

方法一：v模式多行编辑

**注释**

1 Ctrl+v进入v模式

2 上下方向键选中要注释的行

3 shift+i（即大写的I）行首插入

4 输入注释符//

5 按esc返回

**反注释**

1 Ctrl+v进入v模式

2 上下方向键选中要注释的行，左右键选择要删除的字符//

3 按x删除

### 复制粘贴命令

1. 选定文本块：V
2. 复制的命令：y，即yank（提起） ，常用的命令如下： 
       y      在使用v模式选定了某一块的时候，复制选定块到缓冲区用； 
       yy    复制整行（nyy或者yny ，复制n行，n为数字）； 
       y^   复制当前到行头的内容； 
       y$    复制当前到行尾的内容； 
       yw   复制一个word （nyw或者ynw，复制n个word，n为数字）； 
       yG    复制至档尾（nyG或者ynG，复制到第n行，例如1yG或者y1G，复制到档尾）     
3. 剪切的命令：d，即delete
   d      剪切选定块到缓冲区； 
   dd    剪切整行 
   d^    剪切至行首 
   d$     剪切至行尾 
   dw    剪切一个word 
   dG     剪切至档尾  
4. 粘贴的命令：p，即put（放下） 
   p      小写p代表贴至游标后（下），因为游标是在具体字符的位置上，所以实际是在该字符的后面 
   P      大写P代表贴至游标前（上） 
   整行的复制粘贴在游标的上（下）一行，非整行的复制则是粘贴在游标的前（后）

### 跨文件复制／粘贴

可以通过分屏情况下，使用v 选中，y复制，p粘贴

1、用vim打开一个文件，例如：city1.py

2、在普通模式下，输入：":vsp city2.py"

3、切换到city.py，在普通模式下，使用v来选中复制内容，复制y，在 普通模式下ctrl+w，再按一下w，切换到city2.py

4、按一下p，就完成复制了。 

### 缩进命令

1. normal 模式下 

   当前行增加缩进：>>

   当前行减少缩进：<< 

   或者 
   :10,100> 
   第10行至第100行缩进 
   :20,80< 
   第20行至第80行反缩进

2. Visual 模式下 
   按v 即进入VISUAL模式，按一次大于号’>’缩进一次，按’6>’缩进六次，按’<’回缩

3. INSERT 模式下

   CTRL+SHIFT+T：当前行增加缩进 

   CTRL+SHIFT+D：当前行减少缩进

### vim分屏命令

https://coolshell.cn/articles/1679.html

**分屏启动Vim**

1. 使用大写的O参数来垂直分屏。

   ```
   vim -On file1 file2 ...
   ```

2. 使用小写的o参数来水平分屏。

   ```
   vim -on file1 file2 ...
   ```

**分屏**

1. 上下分割当前打开的文件。

   ```
   :split
   :sp
   Ctrl+W s
   ```

2. 上下分割，并打开一个新的文件。

   ```
   :sp filename
   :split filename
   ```

3. 左右分割当前打开的文件。

   ```
   Ctrl+W v
   :vsp
   :vsplit
   ```

4. 左右分割，并打开一个新的文件。

   ```
   :vsp filename
   :vsplit filename
   ```

**移动光标**

Vim中的光标键是h, j, k, l，要在各个屏间切换，只需要先按一下Ctrl+W

1. 把光标移到右边的屏。

   ```
   Ctrl+W l
   ```

2. 把光标移到左边的屏中。

   ```
   Ctrl+W h
   ```

3. 把光标移到上边的屏中。

   ```
   Ctrl+W k
   ```

4. 把光标移到下边的屏中。

   ```
   Ctrl+W j
   ```

5. 把光标移到下一个的屏中。.

   ```
   Ctrl+W w
   ```

**关闭分屏**

1. 关闭当前窗口。

   ```
   Ctrl+W c
   ```

2. 关闭当前窗口，如果只剩最后一个了，则退出Vim。

   ```
   Ctrl+W q
   ```

### 跳到最后一行或首行

- shift+g 跳转到最后一行
- gg 跳转到第一行

### 切屏快捷键

ctrl+tab

# git命令

**git init**

这是新项目要做的第一件事，在项目中创建一个.git存储库。存储库（repo）是你对一个项目按照时间顺序做得所有修改的集合，记录了所有更改历史。

**git config —global user.name “Your Name”**
**git config —global user.email “yourEmail@mail.com”**

这是用来设置你提交的时候用的信息，只需要在你第一次安装Git之后设置一次就行了。

**git add filename.extension**

把filename.extension替换成任何你想增添的文件，比如index.html。这可以把你制定的问价放进暂存区（staging area）或index中，你可以把暂存区想成是一个用来做相关设置，准备放进存储库的地方。

**git add .**

这个命令可以帮你把项目文件夹下的所有文件都放进暂存区，不用一个一个挪。

**git add \*.html**

这个命令可以帮你把项目文件夹下的所有.html文件都放进暂存区，当然你可以换成其他任何扩展名，就把该扩展名的所有文件都放进暂存区。

**git status**

显示所有你已经放进暂存区的的文件，以及进行了修改需要放进暂存区的文件。

**git reset filename.extension**

从暂存区中删除指定文件。

**git rm —cached filename.extension**

从暂存区中删除该文件，并将其设置为未跟踪。

**git commit -m “Description of the commit”**

从暂存区获取文件，并将他们提交到本地存储库。引号里写的部分是你的修改内容，注意写的简单清晰一点，比如“修复了用户名未更新的bug”，不要写“一些更新”这种模模糊糊的概述。

**touch .gitignore**

创建一个名叫.gitignore的文件，你可以用文本编辑器打开这个文件，写下存储库里需要忽略的文件名或者文件夹名，运行的时候这些被忽略的文件不会显示。

所以，如果你不想提交某个文件，就用这个命令吧。

**git branch branchName**

创建一个分支（branch），就是你前一个分支代码库的直接副本。

**git checkout “branchName”**

检查你创建的分支，并在这个分支内工作。你可以再次对你的代码进行任何更改，弄完之后再提交代码然后把这个分支push到GitHub上。如果除了问题或者你不再需要这个功能了，那就可以直接删掉分支。

**git merge branchName**

在master里，你可以用这个命令从你正在用的分支里提交，然后把它们和主存储库merge到一起。

**git remote add origin https://github.com/userName/project.git**

添加远程存储库的位置。在这一步之前，你的操作都是在本地完成的，需要登上你的GitHub账号创建一个远程存储库，然后把本地存储库的文件放上去。创建远程存储库后，会生成一个链接，可以放在上面的命令里。

**git remote**

和你的项目关联的远程存储库列表。

**git push -u origin master**

将本地存储库推送到远程存储库，第一次执行此命令时，直接这样写就好了 。

**git push**

在你执行完初始推送后把代码放到GitHub上。

**git clone https://github.com/userName/project.git**

把项目clone到你的本地计算机。

**git pull**

如果你和别人用一样的代码库，这个命令可以让你从远程存储库提取最新版本，更新你的本地版本，这样你就能在同伴工作的基础上继续写代码了。

## 常用

**git add file**

**git commit -m 'comment'**

**git push origin master:refs/for/master  **

