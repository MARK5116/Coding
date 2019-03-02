# python

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

