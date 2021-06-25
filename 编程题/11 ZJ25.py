"""
ZJ25 头条校招 

https://www.nowcoder.com/practice/57cf0b1050834901933e9b48daafbb9a?tpId=137&tags=&title=&difficulty=0&judgeStatus=0&rp=0

描述
头条的2017校招开始了！为了这次校招，我们组织了一个规模宏大的出题团队，每个出题人都出了一些有趣的题目，而我们现在想把这些题目组合成若干场考试出来，在选题之前，我们对题目进行了盲审，并定出了每道题的难度系统。一场考试包含3道开放性题目，假设他们的难度从小到大分别为a,b,c，我们希望这3道题能满足下列条件：
a<=b<=c
b-a<=10
c-b<=10
所有出题人一共出了n道开放性题目。现在我们想把这n道题分布到若干场考试中（1场或多场，每道题都必须使用且只能用一次），然而由于上述条件的限制，可能有一些考试没法凑够3道题，因此出题人就需要多出一些适当难度的题目来让每场考试都达到要求，然而我们出题已经出得很累了，你能计算出我们最少还需要再出几道题吗？
输入描述：
输入的第一行包含一个整数n，表示目前已经出好的题目数量。
第二行给出每道题目的难度系数d1,d2,...,dn。
数据范围
对于30%的数据，1 ≤ n,di ≤ 5;
对于100%的数据，1 ≤ n ≤ 10^5,1 ≤ di ≤ 100。
在样例中，一种可行的方案是添加2个难度分别为20和50的题目，这样可以组合成两场考试：（20 20 23）和（35,40,50）。
输出描述：
输出只包括一行，即所求的答案。


示例1
输入：

4  
20 35 23 40

输出：

2

示例2
输入：
2
1 22

输出 

4

示例2
输入：
3
10 50 70
预期输出：3

"""
'''
排序+贪心
'''
import math

class Solution:
    def question(n, d):
        a=0
        # 1. 先排序
        d.sort()
        res = []
        for i in range(n):
            if len(res)%3 == 0:
                res.append(d[i])
            else:
                tmp = math.ceil((d[i]-res[-1])/10)-1
                # print (tmp)
                if tmp == 0:
                    res.append(d[i])
                else:
                    for x in range(1, tmp+1):
                        res.append(res[-1]+ 10)
                        a+=1
                        if x == 2:
                            break
                    res.append(d[i])
        if len(res)%3 != 0:
            a = a+ (3-(len(res)%3))
        return a 

if __name__ == '__main__':
    n = int(input())
    d = list(map(int, input().strip().split()))
    s = Solution.question(n, d)
    print(s)