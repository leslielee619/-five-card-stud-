# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 22:08:38 2019

@author: leslie lee
"""

import judgement_criteria
import pygal
import deal_card

def census(number=1000):
    num=0
    player1_results=[]
    player2_results=[]
    frequencies1=[]
    frequencies2=[]
    while num < number:
        player1,player2=deal_card.init_hands()
        results1 = judgement_criteria.judge(player1)
        results2 = judgement_criteria.judge(player2)
        player1_results.append(results1)
        player2_results.append(results2)
        num += 1
    
    for value in range(1,10):
        frequency = player1_results.count(value)
        frequency = player2_results.count(value)
        frequencies1.append(frequency)
        frequencies2.append(frequency)
    return frequencies1,frequencies2    

def hist(frequencies,number=1000):    
    hist=pygal.Bar()
    hist.title = "进行"+str(number)+"次港式五张以后得到各种牌型大致的可能性"
    hist.x_labels = ["铁支","葫芦","同花","顺子","三条","两对","对子","同花顺",
                     "单牌"]
    hist.x_title = "牌型"
    hist.y_title = "牌型的频率"
    hist.add("港式五张",frequencies)
    name = input('提示：需要手动输入文件的名称，后缀必须为.svg\n')
    hist.render_to_file(name)
