"""
要求AI随机出，用户自定义，可实现5局3胜后自动结束
"""

import random

def Game(User,AI):   
    print(f'你使出：{User}') 
    print(f'AI使出：{AI}')
    result = data[User] - data[AI]
    if result == 0:
        print('平局')
        return '平局'
    elif result == -1 or result == 2:
        print('胜利')
        return '胜利'
    elif result == 1 or result == -2:
        print('失败')
        return '失败'



def Start():
    Point = 0
    for _ in range(5):
        User = input('快出拳：')
        if User not in data:
            print('请出：石头/剪刀/布')
            continue
        AI = random.choice(list(data.keys()))
        result = Game(User, AI)
        if result == '胜利':
            Point += 1
        elif result == '失败':
            Point -= 1
        elif result == '平局':
            Point += 0

        if Point == 3 or Point == -3:
            break

    if Point > 0:
        print('你赢了')
    elif Point < 0:
        print('死亡')
    else:
        print('平分秋色')



data = {
    "石头": 0,
    "剪刀": 1,
    "布": 2
}

Start()