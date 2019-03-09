# python

## 启动脚本

```python
#!/bin/sh

#export SPARK_HOME=$SPARK16_HOME
export HADOOP_HEAPSIZE=2048
export HADOOP_CLIENT_OPTS="-Xmx2048m"

export HADOOP_USER_NAME="driver_ecosys"
export HADOOP_USER_PASSWORD=WSe0OMfJ6QcQvONAaTEChD9WEEh2LRYP

export PYSPARK_DRIVER_PYTHON=/home/luban/miniconda3/bin/python

spark-submit -v \
    --conf "spark.dynamicAllocation.minExecutors=100" \
    --conf "spark.dynamicAllocation.maxExecutors=1000" \
    --conf "spark.yarn.executor.memoryOverhead=3072" \
    --driver-memory 2g \
    --executor-memory 10g \
    --executor-cores 6 \
    --master yarn-client \
    --queue root.celuemoxingbu_driver_ecosys \
    ./cross_city.py


```

## 读取HDFS上的分布式文件

```python 
for j in range(367):
    city_id = 'part-00'+str("%03d" % j)
    #读取文件
    day = sc.textFile('/user/bigdata_driver_ecosys_test/liuzhu/split_train_explore_instance/20190302_20190305/'+city_id, 2)
    
    for i in ['2019-03-03','2019-03-04','2019-03-05']:
        #文件处理
        #文件保存
        instance = day.map(lambda x: [x.split("\t")[3], x]).filter(lambda x: x[0][0:10] == i).map(lambda x: x[1]).saveAsTextFile('/user/bigdata_driver_ecosys_test/liuzhu/split_train_explore_instance/%s/%s' % (i,city_id))
```

### 常用函数

```python 
#读取文件
data = sc.textFile(filename, 2)
#保存文件
#一般而言，saveAsTextFile会按照执行task的多少生成多少个文件，比如part-00000一直到part-0000n，n自然就是task的个数，亦即是最后的stage的分区数.
data.saveAsTextFile(filename)
#保存为一个文件
data.repartition(1).saveAsTextFile(filename)
data.coalesce(1).saveAsTextFile(filename)
```



##  常用函数

### withColumn()

语法：`withColumn(colName, col)`

功能：增加新的一列数据。

```python
from pyspark.sql.functions import *
from pyspark.sql.types import IntegerType, FloatType

def round_discount(data, discount_l):
    for i in discount_l:
        if(np.round(np.abs(data-i),3)<=0.025):
            return i
    return data

def round_discount_udf(slot_list):
    return udf(lambda l: round_discount(l,slot_list),FloatType())

#其中col()表达式表明使用其他列数据。
data = spark.sql('...')
data = data.withColumn("discount", round_discount_udf([0.8, 0.85, 0.9, 0.95, 1.0])\
                       (col('discount_nocarpool')))

data = data.filter('discount >=0.8').groupby('discount').\
        agg(count('label').alias("bubble"), sum('label').alias('order'))

data = data.withColumn('ecr', data['order'] / data['bubble'])
data = data.withColumn('deta_ecr',  data['ecr'] / data.filter('discount = 1').\
                       select('ecr').collect()[0][0] - 1)

```

### alisa()

功能：使用新列名

```python 
data = data.filter('discount >=0.8').groupby('discount').\
        agg(count('label').alias("bubble"), sum('label').alias('order'))
```

### collect()

功能：Spark内有collect方法，是Action操作里边的一个算子，这个方法可以将RDD类型的数据转化为数组，同时会从远程集群是拉取数据到driver端。

### filter()

功能：过滤数据

```python
from pyspark import SparkContext

def even_squares(num):
    return num.filter(lambda x: x % 2 == 0).map(lambda x: x * x)


if __name__ == "__main__":

    sc = SparkContext('local', 'word_count')
    nums = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8])
    res = sorted(even_squares(nums).collect())
    print (res)
```



