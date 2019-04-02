"""
@author: zkjiang
判断数组中连续子数组四target的个数
这个题开始不会，只会想到n2的暴力方法，后面看到大佬，用的是一个字典
从第一个开始累加数组，字典的键是当前累加到的和，字典的值是当前累加到的和出现的次数
然后如果当前和减去K也存在于字典中，那么最终结果就加上当前和减去K为键的次数（value值）
例子：
[1,2,3,1,1]
target：5
遍历1的时候，发现sum是1，字典中加入1:1
遍历2的时候，发现sum是1+2 = 3字典中加入3:1
。。。字典中加入：6:1，此时判断6-5是不是在字典中，在的话，最终结果加入key为6-5也就是1的值
。。。字典中加入：7:1，此时判断7-5=2不在字典中，pass
。。。字典中加入：8:1，此时判断8-5=3在字典中，最终结果加1
说白了就是认为我的目标数组是两个数组相减，一个数组是从0到目标数组的尾巴，另一个数组是从0到目标数组的头
@time: 2019/4/1 19:52
"""

class Solution(object):
    def subarraySum(self, nums, k):
        sum_dict = {}
        # 记录和值
        sum = 0
        sum_dict[0] = 1
        result = 0
        # 遍历数组
        for num in nums:
            sum += num
            # 判断sum-k是否在字典中，在的话就加上其值
            if sum - k in sum_dict:
                result += sum_dict[sum-k]
            # 判断sum是否在字典中，在的话加1不在的话赋值为1
            sum_dict[sum] = sum_dict[sum] + 1 if sum in sum_dict else 1
        return result