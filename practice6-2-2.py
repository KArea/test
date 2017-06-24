#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class FinalAnt:
    def __init__(self,x=0,y=0,color='black'):
        self.x = x
        self.y = y
        self.color = color        
    def crawl(self,x,y):
        self.x += x
        self.y += y
        print('爬行……')
        self.info()        
    def jump(self,x,y):
        self.x += x
        self.y += y
        print('跳跃！')
        self.info()        
    def fly(self,x,y):
        self.x += x
        self.y += y
        print('飞行……')
        self.info()       
    def attack(self):
        print('用嘴咬！')        
    def impact(self):
        print('用身子撞击！')         
    def info(self):
        print('当前位置：(%d,%d)'%(self.x,self.y))

ac = FinalAnt()
ac.attack()
ac.impact()
ac.crawl(1,2)
ac.jump(3,4)
ac.fly(5,6)
