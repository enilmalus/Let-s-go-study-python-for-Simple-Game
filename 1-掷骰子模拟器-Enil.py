"""

掷下这个筛子五次，要求判断这五个数字是否是同顺子（3个相邻即为顺子）、葫芦（3个相同带2个相同）、两对（2对2个相同）

"""
 
import random
from collections import Counter

dice = [i for i in range(1,7)]
result = random.choices(dice, k=5)
Count = Counter(result)


for i in result:
    print(i, end=" ")

Rresult = sorted(result)
# 判断顺子
if Rresult == [1,2,3,4,5] or Rresult == [2,3,4,5,6]:
    print("顺子")

# 判断葫芦
elif Count.most_common(1)[0][1] ==3 and Count.most_common(2)[1][1] == 2:
    print("葫芦")

# 判断两对
elif Count.most_common(1)[0][1] == 2 and Count.most_common(2)[1][1] == 2:
    print("两对")

else:
    print("高牌")


"""
a = [1,2,3,4,5,6]

random.choice(a)可以随机选择列表中的一个元素
random.choices(a, k=3)可以重复3次从a中选择一个元素
"""