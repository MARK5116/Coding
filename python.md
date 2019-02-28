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