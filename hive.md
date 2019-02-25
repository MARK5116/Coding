# hive

## 常用命令

**查看分区**

```sql
hive> show partitions table_name; 
```

**修改表**

```hive
hive> ALTER TABLE table_name SET TBLPROPERTIES('comment' = '这是表注释!');
```

**修改字段**

```hive
hive> ALTER TABLE table_name CHANGE COLUMN muid muid_new STRING COMMENT '这里是列注释!'; 
```



## 常用的hiveQL函数

**解析json字符串**

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

**条件判断函数**

```sql
--1.if
--说明:  当条件testCondition为TRUE时，返回valueTrue；否则返回valueFalseOrNull
if(boolean testCondition, T valueTrue, T valueFalseOrNull)

--hive> select if(1=2,100,200) from dual;   返回：200

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



