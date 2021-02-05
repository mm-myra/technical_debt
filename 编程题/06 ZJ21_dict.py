"""
特征提取

https://www.nowcoder.com/practice/5afcf93c419a4aa793e9b325d01957e2?tpId=137&tags=&title=&diffculty=0&judgeStatus=0&rp=0&tab=answerKey

题目描述
       小明是一名算法工程师，同时也是一名铲屎官。某天，他突发奇想，想从猫咪的视频里挖掘一些猫咪的运动信息。
       为了提取运动信息，他需要从视频的每一帧提取“猫咪特征”。一个猫咪特征是一个两维的vector<x, y>。
       如果x_1=x_2 and y_1=y_2，那么这俩是同一个特征。
       因此，如果喵咪特征连续一致，可以认为喵咪在运动。
       也就是说，如果特征<a, b>在持续帧里出现，那么它将构成特征运动。
       比如，特征<a, b>在第2/3/4/7/8帧出现，那么该特征将形成两个特征运动2-3-4 和7-8。
现在，给定每一帧的特征，特征的数量可能不一样。小明期望能找到最长的特征运动。
输入描述:

第一行包含一个正整数N，代表测试用例的个数。

每个测试用例的第一行包含一个正整数M，代表视频的帧数。

接下来的M行，每行代表一帧。其中，第一个数字是该帧的特征个数，接下来的数字是在特征的取值；比如样例输入第三行里，2代表该帧有两个猫咪特征，<1，1>和<2，2>
所有用例的输入特征总数和<100000

N满足1≤N≤100000，M满足1≤M≤10000，一帧的特征个数满足 ≤ 10000。
特征取值均为非负整数。

输出描述:

对每一个测试用例，输出特征运动的长度作为一行

示例1
输入
复制

1
8
2 1 1 2 2
2 1 1 1 4
2 1 1 2 2
2 2 2 1 4
0
0
1 1 1
1 1 1

输出
复制

3

说明

特征<1,1>在连续的帧中连续出现3次，相比其他特征连续出现的次数大，所以输出3

备注:

如没有长度大于2的特征运动，返回1
"""


'''
思路：
1)难点在于读取数据
2)字典的使用
'''
if __name__ == '__main__':
    # 第一行 N 为：测试用例的个数
    N = int(input())
    # 遍历：每个测试用例
    for i in range(N):
        res = 0
        last_feature = {}  # # 用来记录：上一帧频率
        # 测试用例的第一行：M：视频的帧数
        M = int(input())
        # 遍历：每帧
        for k in range(M):
            # 每行为一帧
            line = list(map(int, input().split()))
            # 每行的第一个数字为 当前帧的特征的个数
            feature_number = line.pop(0)
            # 用来记录：当前帧频率
            current_feature = {}
            for x in range(feature_number):
                # 当前特征
                feature = (line[x*2], line[x*2+1])
                # print(feature, '**********feature')
                # 从上次的 特帧记录中查找，然后个数+1，无的话是0+1
                current_feature[feature] = last_feature.get(feature, 0) + 1
                # print(current_feature, '&&&&&&&&&&&&current_feature')
                # 记录最大连续帧
                res = max(res, current_feature[feature])
            # 下次循环前，更新
            # print(last_feature, '$$$$$$$$last_feature')
            # print(current_feature, '*############*current_feature')
            last_feature = current_feature
        print(res if res >= 2 else 1)
