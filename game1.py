# -*- coding: utf-8 -*-
print('---------------猜数游戏-------------')
import random
secret = random.randint(1,10)
print('不妨猜一下我现在心里想的是哪个数字')
n = 3
while  n != 0:
    n = n-1
    guess = int(input('请输入数字：'))
    if guess == secret:
        print('我艹你是我肚子里的蛔虫吗？！')
        print('哼，猜中了也没有奖励！')
        break
    else:       
        if guess > secret:
            print('哥，大了大了~~')
        else:
            print('嘿，小了！小了！！')
else:
    print('\n三次都猜错啦！')
print('游戏结束，不玩啦^_^')
