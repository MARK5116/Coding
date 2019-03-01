# 常用技巧

## 字符串

### format()

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



### join()

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

2. how为连接方式，
3. on指定以哪些列连接。

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

