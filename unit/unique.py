# 2020-12-30 10：14
def unique(data, n):
    if n == 0:  # 基本情况
        return True
    else:
        if data[n] == data[n - 1]:  # 条件判断
            return False
        else:
            return unique(data, n - 1)  # 往基本情况靠近


# 正确算法
def unique2(S):
    """Return True if there are no duplicate elements in sequence S."""
    temp = sorted(S)  # create a sorted copy of S
    for j in range(1, len(temp)):
        if temp[j - 1] == temp[j]:
            return False  # found duplicate pair
    return True  # if we reach this, elements wew unique


if __name__ == '__main__':
    import numpy as np

    for i in range(100):
        data = np.random.randint(0, 9, size=(100,))
        if unique(data, len(data) - 1) == unique2(data):
            pass
        else:
            print("计算错误")
