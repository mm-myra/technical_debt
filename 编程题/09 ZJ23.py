"""

ZJ23 找零 

https://www.nowcoder.com/practice/944e5ca0ea88471fbfa73061ebe95728?tpId=137&tags=&title=&difficulty=0&judgeStatus=0&rp=0


描述
Z国的货币系统包含面值1元、4元、16元、64元共计4种硬币，以及面值1024元的纸币。现在小Y使用1024元的纸币购买了一件价值为N(0<N≤1024)N (0 < N \le 1024)N(0<N≤1024)的商品，请问最少他会收到多少硬币？
输入描述：
一行，包含一个数N。
输出描述：
一行，包含一个数，表示最少收到的硬币数。
示例1
输入：

200

输出：

17

说明：

花200，需要找零824块，找12个64元硬币，3个16元硬币，2个4元硬币即可。

备注：

对于100%的数据，N(0<N≤1024)N (0 < N \le 1024)N(0<N≤1024)。
"""

class Solution:
    def change(total, price, money):
        change = total - price
        coin = 0
        i = 1
        while change > 0:
            tmp = money[-i]
            # print(tmp)
            coin = coin + change//tmp
            change = change%tmp
            # print(coin, change)
            i=i+1
        return coin


if __name__ == '__main__':
    n = int(input())
    s = Solution.change(1024, n, [1, 4, 16, 64])
    print(s)



'''
1. /是精确除法，//是向下取整除法，%是求模
2. %求模是基于向下取整除法规则的
3. 四舍五入取整round, 向零取整int, 向下和向上取整函数math.floor, math.ceil
4. //和math.floor在CPython中的不同
5. /在python 2 中是向下取整运算
6. C中%是向零取整求模。

'''