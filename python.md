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

