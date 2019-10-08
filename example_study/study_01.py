# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？


def three_numbers(num):
    """
    :param num:  需要多少个数字进行组合
    :return: 3位数列表list
    """
    num = int(num) + 1
    num_list = []
    for i in range(1, num):
        for j in range(1, num):
            for k in range(1, num):
                if i != j and i != k and j != k:
                    number = str(i) + str(j) + str(k)
                    num_list.append(number)
    return num_list
