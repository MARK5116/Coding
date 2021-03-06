#coding:utf-8

#选择排序
def select_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[min] > arr[j]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]

    return arr

#插入排序
def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > key:
                arr[j+1] = arr[j]
                arr[j] = key
            j -= 1
    return arr

#归并排序
def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j +=1

    result += left[i:]
    result += right[j:]
    return result
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    num = len(arr) / 2
    left = merge_sort(arr[:num])
    right = merge_sort(arr[num:])
    return merge(left,right)

if __name__ == "__main__":
    raw_arr = [38,65,97,76,13,27,49]
    print(raw_arr)
#    select_arr = select_sort(raw_arr)
    #print(select_arr)
    #insert_arr = insert_sort(raw_arr)
    #print(insert_arr)
    #print(raw_arr)
    merge_arr = merge_sort(raw_arr)
    print(merge_arr)

