"""
给你一个数，然后求出数字改变顺序最小的比他大的数

例如：35268  --》  35286
@file: change_num.py
@time: 2019/5/20 20:52
"""


def solution(target):
    # 基本思路就是倒着找出递增序列然后找到第一个不是的，把这些重新排序
    tmp_list = [int(i) for i in str(target)]
    rever_list = list(reversed(tmp_list))
    n = len(rever_list)
    tag = 0
    for i in range(1, n):
        if rever_list[i] < rever_list[i-1]:
            tag = i
            break
    minmax = 10
    final_tag = 0
    for j in range(0,tag):
        if minmax > rever_list[j] > rever_list[tag]:
            final_tag = j
    rever_list[final_tag], rever_list[tag] = rever_list[tag], rever_list[final_tag]
    rever_list[:tag] = sorted(rever_list[:tag], reverse=True)
    final_result = "".join([str(i) for i in list(reversed(rever_list))])
    print(final_result)


if __name__ == '__main__':
    target = 3674321
    solution(target)