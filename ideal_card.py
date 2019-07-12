# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:59:10 2019

@author: leslie lee
"""
"""
为了方便将10改成T
"""
import random

suits=['Club','Diamond','Spade','Heart']
ranks=['8','9','T','J','Q','K','A']




def init_hands():
    """将28张牌混合好，并发给两个玩家"""
    hands=[]
    
    for rank in ranks:
        for suit in suits:
            hands.append('{0} {1}'.format(rank,suit))    
    random.shuffle(hands)        
        
    """将牌发给玩家"""
    player1=[]
    player2=[]
    
    player1.append(hands[0])
    player1.append(hands[1])
    player1.append(hands[4])
    player1.append(hands[6])
    player1.append(hands[8]) 
      
    player2.append(hands[2])
    player2.append(hands[3])
    player2.append(hands[5])
    player2.append(hands[7])
    player2.append(hands[9])
    
    #print(hands)
    #print(player1)
    #print(player2)
        
    return player1,player2


#init__hands()
