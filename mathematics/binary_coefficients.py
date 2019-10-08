# 杨辉三角 ：  又称帕斯卡三角形
def pascal_triangle(line_number):
    """
    :param line_number:  行数
    :return: 二维列表list
    """
    list1 = list()
    list1.append([1])
    i = 1
    while i <= line_number:
        j = 1
        l1 = [1]
        while j < i:
            l1.append(list1[i - 1][j] + list1[i - 1][j - 1])
            j += 1
        l1.append(1)
        list1.append(l1)
        i += 1
    return list1
