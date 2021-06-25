'''
https://www.nowcoder.com/practice/623a5ac0ea5b4e5f95552655361ae0a8?tpId=13&tqId=11203&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中第一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
返回描述：
如果数组中有重复的数字，函数返回true，否则返回false。
如果数组中有重复的数字，把重复的数字放到参数duplication[0]中。（ps:duplication已经初始化，可以直接赋值使用。） 

'''


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        d={}
        for num in numbers:
            if num not in d:
                d[num]=0
            else:
                duplication[0]=num
                return True
        return False

if __name__ == '__main__':
    n = [1,2,3,4,5,6,7]
    a = [0]
    s=Solution
    print(Solution.duplicate(s, n, a))
    print(a)


'''
注意：以下方法不能查找到第一个重复的数字

def duplicate(nums: list) -> int:
    for i, num in enumerate(nums):
        while i != num:
            if num == nums[num]:
                return True, num
            else:
                nums[i], nums[num] = nums[num], nums[i]
                num = nums[i]
    return False, None

'''
