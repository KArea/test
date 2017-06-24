# -*- coding: utf-8 -*-
print('---------------我爱python-------------')
guess = int(input('不妨猜一下我现在心里想的是哪个数字：'))
n = 2
while  n != 0:
    n = n-1   
    if guess == 8:
        print('我艹你是我肚子里的蛔虫吗？！')
        print('哼，猜中了也没有奖励！')
        break
    else:
        guess = int(input('哎呀，猜错了，请重新输入吧：'))
        if guess > 8:
            print('哥，大了大了~~')
        else:
            print('嘿，小了！小了！！')
print('游戏结束，不玩啦^_^')
