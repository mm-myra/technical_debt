"""
雀魂启动！

https://www.nowcoder.com/practice/448127caa21e462f9c9755589a8f2416?tpId=137

题目描述
小包最近迷上了一款叫做雀魂的麻将游戏，但是这个游戏规则太复杂，小包玩了几个月了还是输多赢少。
于是生气的小包根据游戏简化了一下规则发明了一种新的麻将，只留下一种花色，并且去除了一些特殊和牌方式（例如七对子等），具体的规则如下：

    总共有36张牌，每张牌是1~9。每个数字4张牌。
    你手里有其中的14张牌，如果这14张牌满足如下条件，即算作和牌

    14张牌中有2张相同数字的牌，称为雀头。
    除去上述2张牌，剩下12张牌可以组成4个顺子或刻子。顺子的意思是递增的连续3个数字牌（例如234,567等），刻子的意思是相同数字的3个数字牌（例如111,777）


例如：
1 1 1 2 2 2 6 6 6 7 7 7 9 9 可以组成1,2,6,7的4个刻子和9的雀头，可以和牌
1 1 1 1 2 2 3 3 5 6 7 7 8 9 用1做雀头，组123,123,567,789的四个顺子，可以和牌
1 1 1 2 2 2 3 3 3 5 6 7 7 9 无论用1 2 3 7哪个做雀头，都无法组成和牌的条件。

现在，小包从36张牌中抽取了13张牌，他想知道在剩下的23张牌中，再取一张牌，取到哪几种数字牌可以和牌。
输入描述:

输入只有一行，包含13个数字，用空格分隔，每个数字在1~9之间，数据保证同种数字最多出现4次。

输出描述:

输出同样是一行，包含1个或以上的数字。代表他再取到哪些牌可以和牌。若满足条件的有多种牌，请按从小到大的顺序输出。若没有满足条件的牌，请输出一个数字0

示例1
输入
复制

1 1 1 2 2 2 5 5 5 6 6 6 9

输出
复制

9

说明

可以组成1,2,6,7的4个刻子和9的雀头


示例 2
输入 1 1 1 2 3 4 5 6 7 8 9 9 9
输出 1 2 3 4 5 6 7 8 9

"""


def is_hupai(cards, own):
    # 剩余0张牌，即可胡牌
    if own == 0:
        return True
    else:
        # 判断顺子-递增的连续3个数字牌：
        for i in range(1, 10):
            # 判断刻子-相同数字的3个数字牌：
            if cards[i] >= 3:
                cards[i] -= 3
                own -= 3
                if is_hupai(cards, own) is True:
                    return True
            if i < 8:
                if cards[i] > 0 and cards[i+1] > 0 and cards[i+2] > 0:
                    cards[i] -= 1
                    cards[i+1] -= 1
                    cards[i+2] -= 1
                    own -= 3
                    if is_hupai(cards, own) is True:
                        return True
        return False


def hupai(cards_add):
    # 从0到9查找雀头
    for sparrow_head in range(1, 10):
        if cards_add[sparrow_head] < 2:
            continue
        else:
            # print('********sparrow_head***********:', sparrow_head)
            cards_without_head = cards_add.copy()
            cards_without_head[sparrow_head] -= 2
            # print(cards_without_head, '去掉雀头的cards_without_head')
            if is_hupai(cards_without_head, 12) is True:
                return True
    return False


if __name__ == '__main__':
    init = list(map(int, input().strip().split()))
    # 记录当前手中的牌，index 为数字， cards[index]为牌数
    cards = [0]*10
    for i in init:
        cards[i] += 1
    # print(cards)
    result = ''
    # 从1到9，循环尝试最后一张牌，若已经有该数字 的4张，则跳过
    for last_card in range(1, 10):
        # print('+++++++++++++++++last_card++++++++++++++++++++++:', last_card)
        if cards[last_card] == 4:
            continue
        else:
            cards_add = cards.copy()
            cards_add[last_card] += 1
            # 判断：当前的牌情况是否可以胡牌
            # print(cards_add, 'cards_add')
            if hupai(cards_add) is True:
                result = result + str(last_card) + ' '
                # print('@@@@@@@@@@@@@@@hupai:last_card:', last_card)
    if result != '':
        print(result)
    else:
        print(0)

'''
优化解法：

def IShepai(cards):
    # 总牌数
    lenth = len(cards)
    if lenth == 0:
        return True
    count1 = cards.count(cards[0])
    # 判断雀头以及胡牌 包括递归
    if lenth % 3 != 0 and count1 >= 2 and IShepai(cards[2:]) is True:
        return True
    # 判断刻子 AAA 包括递归
    if count1 >= 3 and IShepai(cards[3:]) is True:
        return True
    # 判断顺子 ABC 包括递归
    if cards[0]+1 in cards and cards[0]+2 in cards:
        cards_new = cards[1:]
        cards_new.remove(cards[0]+1)
        cards_new.remove(cards[0]+2)
        if IShepai(cards_new) is True:
            return True
    return False


if __name__ == '__main__':
    cards = list(map(int, input().split()))
    res = ""
    for i in range(1, 10):
        if cards.count(i) == 4:
            continue
        else:
            cards_i = sorted(cards + [i])
            print(cards_i)
            if IShepai(cards_i) is True:
                res += str(i) + " "
    if res != "":
        print(res)
    else:
        print(0)

'''
