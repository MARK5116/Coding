import numpy as np
import pandas as pd
from pyspark.sql import functions as F
import math
from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .appName("long dis") \
        .enableHiveSupport() \
        .getOrCreate()

spark.sql("create temporary function getHexCellVertexesAndCenter as 'com.didichuxing.bigdata.Utils.getHexCellVertexesAndCenter'")
spark.sql("create temporary function getGridID as 'com.didichuxing.bigdata.Utils.getGridID'")

features = [\
  'pre_total_fee_you',
  'pre_total_fee_pin',
  'area',
  'eta',
  'order_type',
  'discount_nocarpool',
  'discount_nocarpool_you',
  'discount_nocarpool_pin',
  'road_distance',
  'day_of_week',
  'semi_hour_of_day',
  'passenger_os_type',
  'gender',
  'age_level',
  'cnt_complain_orders_30_d_fast',
  'cnt_finish_orders_7_d_fast',
  'pct_call_orders_7_d_share_fast',
  'total_finish_orders_fast',
  'has_car_probability',
  'avg_secs_strive_14_d_fast',
  'cnt_pay_succ_orders_14_d_fast',
  'days_tab_14_d_bus',
  'pct_call_orders_30_d_share_fast',
  'pct_call_orders_14_d_share_fast',
  'cnt_send_orders_30_d_beatles',
  'cnt_call_30_d_taxi',
  'total_cnt_succ_orders_taxi',
  'avg_secs_strive_7_d_fast',
  'amt_paid_finish_orders_14_d_fast',
  'pct_finish_orders_14_d_share_fast',
  'is_businessman',
  'cnt_finish_orders_30_d_fast',
  'pct_finish_orders_30_d_share_fast',
  'cnt_call_orders_30_d_fast',
  'is_tourist',
  'cnt_call_orders_30_d_gulf',
  'pct_finish_orders_7_d_share_fast',
  'avg_dist_finish_orders_30_d_fast',
  'cnt_cancel_before_strive_30_d_fast',
  'cnt_finish_orders_14_d_fast',
  'cnt_cancel_after_strive_30_d_fast',
  'start_ecr',
  'dest_ecr',
  'start_time_ecr',
  'start_dest_ecr',
  'start_dest_time_ecr',
  'pid_day_ecr',
  'pid_start_ecr',
  'pid_dest_ecr',
  'ecr_7_days',
  'ecr_14_days',
  'ecr_21_days',
  'ecr_28_days',
  'ecr_35_days',
  'ecr_42_days',
  'ecr_49_days',
  'ecr_56_days',
  'ecr_var',
  'coordstream_driver_empty_cnt',
  'coordstream_driver_nonempty_cnt',
  'realtime_no_broadcast_order',
  'coordstream_driver_strived_wait_cnt',
  'coordstream_driver_strived_wait_sum',
  'biz_bubble_minute_cnt',
  'biz_order_create_minute_cnt',
  'driver_strive_order_minute_cnt',
  'passenger_wait_pick_time_minute_cnt',
  'dynamic_minute_cnt',
  'dynamic_minute_sum',
  'passenger_order_cancel_before_strive_minute_cnt',
  'passenger_order_cancel_after_strive_minute_cnt',
  'biz_order_finish_charge_minute_cnt',
  'biz_order_dynamic_create_minute_cnt',
  'coordstream_driver_across_wait_cnt',
  'coordstream_driver_across_wait_sum',
  'driver_strive_order_response_minute_sum',
  'passenger_wait_pick_time_minute_sum',
  'coordstream_driver_empty_wait_sum'
]

def colum_fn(name):
    return ',sum(if(%s = -999, 0, %s)) / sum(if(%s = -999, 0, 1)) %s' % (name,name,name,name)

data = 'select sum(if(pre_total_fee = -999, 0, pre_total_fee)) / sum(if(pre_total_fee = -999, 0, 1))'
for name in features:
   data+=colum_fn(name)

dat = data + ' from bigdata_driver_ecosys_test.ecr_ether_v1_pid_sd where concat(year,month,day) between 20190101 and 20190101 and cast(area as INT) in (11)'

dat = spark.sql(dat)
dat = dat.toPandas()
print(dat)

data1 = dat.values
#print(len(data1[0]))
result = [0]
data1[0][25] = -999
data1[0][49] = -999
for i in range(len(data1[0])):
    #result.append(i+1)
    #result.append(str(':'))
    #print(data1[0][i])
    result.append('%d:%f' % (i+1,data1[0][i]))
    
result = ' '.join(str(x) for x in result)
print(result)
