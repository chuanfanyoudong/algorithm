"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: jieba_test.py
@time: 2019/5/4 18:58
"""

import jieba

tmp_list = "我来到这里"
result = jieba.lcut(tmp_list)
print(result)