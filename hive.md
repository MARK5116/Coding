# hive

## 特殊方法 

### 问题1

**查找数据存在A表中，但是不存在B表**

https://www.cnblogs.com/xwdreamer/archive/2012/06/01/2530597.html

```sql
select * from A left join B on A.id=B.id where B.id is null
```

## 常用命令

###查看分区

```sql
hive> show partitions table_name; 
```

###删除表

```hive
hive> drop table if exists table_name;
```

###查看表的描述

```hive
hive> DESCRIBE table_name;
```

###修改表

```sql
hive> ALTER TABLE table_name SET TBLPROPERTIES('comment' = '这是表注释!');
```

###修改字段

```sql
hive> ALTER TABLE table_name CHANGE COLUMN muid muid_new STRING COMMENT '这里是列注释!'; 
```

###修改字段注释

```sql
hive> alter table table_name CHANGE COLUMN muid_old muid_new int comment '这里是列注释';
```

###查询不同的值

```sql
hive> select distinct 字段名 from table_name;
hive> select count(distinct 字段名) from table_name;
```



###把数据文件复制/移动到Hive表对应的地址

```sql
hive> LOAD DATA [LOCAL] INPATH 'filepath' [OVERWRITE] INTO TABLE tablename [PARTITION (partcol1=val1,partcol2=val2 ...)]
```

描述：

- filepath 可以是： 
  相对路径，如project/data1
  绝对路径，如/user/hive/project/data1
  完整的URL，如hdfs://namenode:9000/user/hive/project/data1
  目标可以是一个表或是一个分区。如果目标表是分区表，必须指定是要加载到哪个分区。
- filepath 可以是一个文件，也可以是一个目录(会将目录下的所有文件都加载)。
- 如果命令中带LOCAL，表示： 
  load命令从本地文件系统中加载数据，可以是相对路径，也可以是绝对路径。对于本地文件系统，也可以使用完整的URL，如file:///user/hive/project/data1
  load命令会根据指定的本地文件系统中的filepath复制文件到目标文件系统，然后再移到对应的表
- 如果命令中没有LOCAL，表示从HDFS加载文件，filepath可以使用完整的URL方式，或者使用fs.default.name定义的值
- 命令带OVERWRITE时加载数据之前会先清空目标表或分区中的内容，否则就是追加的方式。

注：

1、hive 中，Load data导入多出现一列null或者全部数据都是null。

问题：*出现一列**null**原因：导入的文件编码问题，需要设置成**utf8**，（**如果改了编码，还是出现一列**null**，就把分隔符由**/t* *改成英文逗号**,**）*

解决：导入的数据全部都是null，原因：createtable时需要指定，

```sql
row formate delimited
fields terminated by ','
Stored as textfile
```

### 根据表名查询HDFS路径

`hive -e "desc formatted [表名]"` 来获取表的信息，从而得知表的 HDFS 路径。

## 常用的hiveQL函数

### 集合统计函数

| 函数    | 说明               |      |
| ------- | ------------------ | ---- |
| avg()   | 忽略列值为Null的行 |      |
| count() | 忽略列值为Null的行 |      |
| max()   |                    |      |
| min()   |                    |      |
| sum()   |                    |      |

```sql
--1. 个数统计函数: count
hive> select count(distinct t) from lxw_dual;

--2. 总和统计函数: sum
hive> select sum(distinct t) from lxw_dual;

--3. 平均值统计函数: avg
hive> select avg (distinct t) from lxw_dual;

--4. 最小值统计函数: min
hive> select min(t) from lxw_dual;

--5. 最大值统计函数: max
hive> select max(t) from lxw_dual;

--6. 非空集合总体变量函数:var_pop

--7. 非空集合样本变量函数:var_samp

--8. 总体标准偏离函数:stddev_pop

--9. 样本标准偏离函数:stddev_samp

--10．中位数函数:percentile

--11. 中位数函数:percentile
hive> select percentile(score,<0.2,0.4>) from lxw_dual；取0.2，0.4位置的数据

--12. 近似中位数函数:percentile_approx

--13. 近似中位数函数:percentile_approx

--14. 直方图:histogram_numeric
hive> select histogram_numeric(100,5) from lxw_dual;
[{"x":100.0,"y":1.0}]
```

### 分组数据

1. group by 数据分组

group by 必须在where之后，order by 之前。

2. having 过滤分组

与where区别：where过滤行，在数据分组前进行过滤；having过滤分组，在数据分组后进行过滤。

```sql
-- 列出至少有两个订单的顾客
select
    cust_id,
    count(*) as order
from Order
group by cust_id
having count(*) >= 2
```

### limit

limit子句用于限制查询结果返回的数量。

**用法**：`select * from tableName limit i,n `

参数：

- i : 为查询结果的索引值（默认从0开始）；
- n : 为查询结果返回的数量

举例：

1. 查询第二条数据

```sql
select * from student limit 1,1;
```

### 解析json字符串

```sql
get_json_object(string json_string, string path)
--说明：第一个参数填写json对象变量
-- 第二个参数使用$表示json变量标识，然后用 . 或 [] 读取对象或数组；如果输入的json字符串无效，那么返回NULL。 
-- 每次只能返回一个数据项。
```

举例：data 为 test表中的字段，数据结构如下：

```sql
data =
{
 "store":
        {
         "fruit":[{"weight":8,"type":"apple"}, {"weight":9,"type":"pear"}],  
         "bicycle":{"price":19.95,"color":"red"}
         }, 
 "email":"amy@only_for_json_udf_test.net", 
 "owner":"amy" 
}

--比如：
--hive>select get_json_object(data, '$.owner') from test;
--hive>select get_json_object(data, '$.store.fruit[0].weitht') from test;
```

```sql
hive> select coalesce(get_json_object(param['dynamic_price'], '${'$'}.600.noncarpool'), get_json_object(param['dynamic_price'],'${'$'}.600')) dynamic_price from table_name

```



### 条件判断函数

`collect_list(name)`

将name组成一个list，函数返回的类型是array< ？ >类型，？表示该列的类型，如果去重，使用`collect_set()`

`array_contains(array arr, element)`

判断元素是否存在与array列表中。

```sql
--1.if
--说明:  当条件testCondition为TRUE时，返回valueTrue；否则返回valueFalseOrNull
if(boolean testCondition, T valueTrue, T valueFalseOrNull)

--hive> select if(1=2,100,200) from dual;   返回：200
--hive> select if(array_contains(t_cityid_list, b.city_id), 0, 1) is_out_city from table_name;
--判断是否为空
--hive> select if(order_id is NULL,0,1) from table_name;

--2.条件判断函数：case
--说明：如果 a 等于 b ，那么返回 c ；如果 a 等于 d ，那么返回 e ；否则返回 f
CASE a WHEN b THEN c [WHEN d THEN e]* [ELSE f] END，

--hive> Select case 100 when 50 then 'tom' when 100 then 'mary' else 'tim' end from dual;
--hive> select case when...

--3.非空查找函数：COALESCE
--语法: COALESCE(T v1, T v2, …)   返回值: T
--说明:  返回参数中的第一个非空值；如果所有值都为NULL，那么返回NULL

hive> select COALESCE(null,'100','50′) from dual;  --输出：100
```

### 字段合并

```sql
--将两个字段合并成一个字段
concat(year, month, day) between '20181026' and '20181026'

hive> select concat(a, '_', b) from tablename;
```

### 关系运算

```sql
--1.等值比较: =

--2.不等值比较: <> 或者 !=

--3.空值判断: IS NULL

--4.非空判断: IS NOTNULL

--5.LIKE比较: LIKE
--注意：否定比较时候用NOT ALIKE B

```

### 逻辑操作符

```sql
--1.A AND B

--2.A && B

--3.A || B

--4. ! A

--5.A IN (val1, val2, ...)
--若A与任意值相等则返回true。

--6.A NOT IN (val1, val2, ...)

--7.[NOT] EXISTS (subquery)
```

### hive日期时间格式转换

`unix_timestamp()`是hive系统时间，格式是timestamp，精确到秒。
 `unix_timestamp(ymdhms)`是把时间转换成timestamp格式，是`2018-05-23 07:15:50`格式。
  `unix_timestamp() - unix_timestamp(ymdhms)`是两个时间转换为timestamp之后相减，timestamp单位是秒，相减之后是两个时间之间相差的秒数。
 `CAST((unix_timestamp() - unix_timestamp(ymdhms)) % 60 AS int)`是相差的秒数。
 `CAST((unix_timestamp() - unix_timestamp(ymdhms)) / 60 AS int) % 60`是相差的分钟数。
  `CAST((unix_timestamp() - unix_timestamp(ymdhms)) / (60 * 60) AS int) % 24`是相差的小时数。
 `concat(CAST((unix_timestamp() - unix_timestamp(ymdhms)) / (60 * 60 * 24) AS int)`是相差的天数。

```sql
--获得当前时区的UNIX时间戳
hive>select unix_timestamp(preshow_time,"yyyy-MM-dd HH:mm:ss") from dual;

--转化UNIX时间戳到当前时区的时间格式
hive> select from_unixtime(unix_timestamp(preshow_time,"yyyy-MM-dd HH:mm:ss"),'HH') as hh from dual;
-- 输出：20111208
```

### 数据类型转换

```sql
--cast(name as int)
--hive> select cast(param['pre_total_fee'] as double) pre_total_fee_kuai from table_name;
```

### 多条件连接

```hive
() n left join(...)m on n.a = m.a and n.b = m.b
```

### having条件

在 SQL 中增加 HAVING 子句原因是，WHERE 关键字无法与合计函数一起使用。

```hive
select
      distinct a.pid pid,
      a.b_day date
    from (
        SELECT
          --area,
          pid,
          concat(year,month,day) b_day,
          count(distinct combine_bubble_id) as cnt
        from gulfstream_dwd.dwd_order_prefee_show
        where concat(year, month, day) between '20190603' and '20190610'
        AND product_id in (3)
        and area in (1)
        group by pid,
        --area,
        concat(year,month,day)
        having cnt < 50
        ) a
```

### ROW_NUMBER() OVER函数

基本使用：https://www.cnblogs.com/liuzhenlei/p/8026278.html

语法：ROW_NUMBER() OVER(PARTITION BY COLUMN ORDER BY COLUMN)

理解：

简单的说row_number()从1开始，为每一条分组记录返回一个数字，这里的ROW_NUMBER() OVER (ORDER BY xlh DESC) 是先把xlh列降序，再为降序以后的每条xlh记录返回一个序号。

row_number() OVER (PARTITION BY COL1 ORDER BY COL2)

 表示根据COL1分组，在分组内部根据 COL2排序，而此函数计算的值就表示每组内部排序后的顺序编号（组内连续的唯一的)。

相关应用链接：https://blog.csdn.net/qq_25221835/article/details/82762416

举例：

1. 如何查询各个用户最长的连续登陆天数？

原题：https://bbs.csdn.net/topics/392243867

```sql
SELECT  
  [UID],
  COUNT(*) AS 记录数
FROM ( 
    SELECT  
      *,
      RN1 - ROW_NUMBER() OVER ( PARTITION BY [UID] ORDER BY RN1 ) AS Grp
    FROM( 
        SELECT  
          *,
          ROW_NUMBER() OVER ( ORDER BY RAND() ) AS RN1 
        FROM table
        ) AS t
     ) AS t2
GROUP BY [UID],
t2.Grp 
order by min ([RN1]);
```

