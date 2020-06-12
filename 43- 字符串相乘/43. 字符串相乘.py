# @Time : 2020/6/12 16:13 
# @Author : Monkey
# @Software: PyCharm
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 如果有一个为0则退出
        if num1 == '0' or num2 == '0':
            return '0'
        n1, n2 = [], []
        # 将两个数据转成列表，如123转成[100, 20, 3]
        for i in range(len(num1)):
            n1.append(int(num1[i])*pow(10, len(num1)-i-1))
        for i in range(len(num2)):
            n2.append(int(num2[i])*pow(10, len(num2)-i-1))
        result = 0
        # 然后让两个列表相乘
        for i in n1:
            for j in n2:
                result += i*j
        return str(result)
