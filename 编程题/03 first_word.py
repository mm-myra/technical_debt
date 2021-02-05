'''
https://www.nowcoder.com/questionTerminal/1c82e8cf713b4bbeb2a5b31cf5b0417c


[编程题]第一个只出现一次的字符
热度指数：473216时间限制：C/C++ 1秒，其他语言2秒空间限制：C/C++ 64M，其他语言128M

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.（从0开始计数）

示例1
输入
"google"
输出
4
'''


class Solution:
    def FirstNotRepeatingChar(s):
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1

    '''
    参考解法
    '''
    def FirstNotRepeatingChar1(self, s):
        return s.index(list(filter(
            lambda c: s.count(c) == 1, s
        ))[0]) if s else -1

    def FirstNotRepeatingChar2(s):
        return [i for i in range(len(s)) if s.count(s[i]) == 1][0] if s else -1


if __name__ == '__main__':
    str = input().strip()
    print((Solution.FirstNotRepeatingChar(str)))






