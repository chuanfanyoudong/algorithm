"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: merge_sort.py
@time: 2019/4/18 14:28
"""


def merge(target_list):
    j = 1
    n = len(target_list)
    while j < n:
        low = 0
        while low < n:
            mid = low + j
            high = low + 2 * j
            merge_sort(target_list, low, high, mid)
            low += 2 * j
        j = 2 * j


def merge_sort(target_list, low, high, mid):
    """
    将两个序列组合
    """
    left = target_list[low:mid]
    right = target_list[mid:high]
    i = 0
    j = 0
    result_list = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result_list.append(left[i])
            i += 1
        else:
            result_list.append(right[j])
            j += 1
    result_list += left[i:]
    result_list += right[j:]
    target_list[low:hight] = result_list

if __name__ == '__main__':
    tmp_list = [2,5,2,3,4,6]
    print(tmp_list[10000000:])