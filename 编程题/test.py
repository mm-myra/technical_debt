"""
https://www.nowcoder.com/practice/448127caa21e462f9c9755589a8f2416?tpId=137
"""
init = list(map(int, input().strip().split()))
cards = [0]*10
own = len(init)
for i in init:
    cards[i]+=1
for i in range(0,9):
    if cards[i]==4:
        continue
    else:
        cards[i]+=1
        own+=1
        cards_cards(cards,own)
        cards[i]+=1

def count_cards(cards,own):
    number = 0
    # 查找雀头
    for i in range(0,9):
        if cards[i] >=2:
            print(cards[i])
            cards[i]-=2
        else:

## 剩余0张牌，即可胡牌
if own == 0 :
    return true
## 判断顺子：
if cards[i]!=0 and cards[i+1]!=0 and cards[i+2]!=0 and i<8:
    cards[i]-=2
    cards[i+1]-=2
    cards[i+2]-=2
if cards[i]>=3:
    cards[i]-=3




 

