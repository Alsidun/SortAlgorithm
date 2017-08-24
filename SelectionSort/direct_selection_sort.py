# -*- coding: utf-8 -*-

""" 实现直接选择排序 """

# 算法核心思想：比较 + 交换
#             从待排序序列中，找到关键字最小的元素，如果最小的元素不是待排序序列的第一个元素，将其和第一个元素交换，从剩余的元素中，
#             选择最小的元素，重复上述步骤，直到排序结束
# 算法介绍网址：https://zh.wikipedia.org/wiki/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F


def direct_selection_sort(lists):
    """ 实现简单选择排序

        Args:
            lists: list
                带排序的数组
    """

    for i in range(len(lists)):
        for j in range(i + 1, len(lists)):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]


if __name__ == '__main__':
    print u'直接选择排序示例：\n'

    array = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
    print u'待排序数组：'
    print array

    direct_selection_sort(array)
    print u'\n排序后数组：'
    print array
