# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:50:12 2019

@author: leslie lee
"""
"""
经历了几个小时的思考，我发现：
对这个牌值大小进行统计后，五张牌只有下列几种结果
11111 顺子或单牌
1112  一个对
113   三张相同
122   两个对
14    四张相同
23    一个对加三张相同

我通过遍历得到一个统计相同牌值有多少个的字典，然后将字典中的值转成列表，再对列表进行
排序便会得到上面的序列
"""
"""
梭哈时顺子有：
8 9 T J Q  
9 T J Q K 
T J Q K A

同时我为了简便，将10改成T
"""
def check_straight_flush(hand):    
    
    """检测是不是同花顺"""
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False

def check_four_of_a_kind(hand):
    """检测是不是四张相同"""
    frequencies={}
    frequencies_list=[]
    
    ranks = [i[0] for i in hand]
    for rank in ranks:
        if rank not in frequencies :
            frequencies[rank] = 1
        else :
            frequencies[rank] += 1
    for  frequency in frequencies.values():
        frequencies_list.append(int(frequency))
        
    frequencies_list.sort()    
    
    #判断list中是否有值为4
    if frequencies_list[1] == 4:
        return True
    else:
        return False
        
def check_full_house(hand):
    """ 检测是不是三张相同加一个对子"""
    frequencies={}
    frequencies_list=[]
    ranks = [i[0] for i in hand]
    for rank in ranks:
        if rank not in frequencies:
            frequencies[rank] = 1
        else:
            frequencies[rank] += 1
    
    for  frequency in frequencies.values():
        frequencies_list.append(int(frequency))
        
    frequencies_list.sort()  
    
    if frequencies_list[0] == 2:
        return True
    else:
        return False
        

def check_flush(hand):
    
    """检测是不是同花"""
    frequencies={}
    frequencies_list=[]
    suits = [i[2] for i in hand]
    for suit in suits:
        if suit not in frequencies :
            frequencies[suit] = 1
        else :
            frequencies[suit] += 1
    
    for  frequency in frequencies.values():
        frequencies_list.append(int(frequency))
        
    frequencies_list.sort() 
    
    if frequencies_list[0] == 5:
        return True
    else:
        return False
   
def check_straight(hand):
    
    """检测是不是顺子"""
    
    frequencies={}
    frequencies_list=[]
    ranks = [i[0] for i in hand]
    for rank in ranks:
        if rank not in frequencies:
            frequencies[rank] = 1
        else:
            frequencies[rank] += 1
    
    for  frequency in frequencies.values():
        frequencies_list.append(int(frequency))
        
    frequencies_list.sort() 
    
    #列出顺子的种类，并且对三种顺子及自己拿到的牌用统一的sort方法排序
    straight1 = ['8','9','T','J','Q']  
    straight2 = ['9','T','J','Q','K']
    straight3 = ['T','J','Q','K','A']
    straight1.sort()
    straight2.sort()
    straight3.sort()
    ranks.sort()
    
    if len(frequencies_list) == 5:
        if ranks == straight1 or ranks == straight2 or ranks == straight3 :
            return True
        else:
            return False
    else:
        return False    
    

def check_three_of_a_kind(hand):
    
    """检测是不是三张相同"""
    frequencies={}
    frequencies_list=[]
    ranks = [i[0] for i in hand]
    for rank in ranks:
        if rank not in frequencies:
            frequencies[rank] = 1
        else:
            frequencies[rank] += 1
    
    for  frequency in frequencies.values():
        frequencies_list.append(int(frequency))
        
    frequencies_list.sort() 
    
    if frequencies_list[1] == 1:
        if frequencies_list[2] == 3:
            return True
        else:
            return False
    else:
        return False       
                    
                

def check_two_pairs(hand):
    
    """检测是不是两个对子"""
    frequencies={}
    frequencies_list=[]
    ranks = [i[0] for i in hand]
    for rank in ranks:
        if rank not in frequencies:
            frequencies[rank] = 1
        else:
            frequencies[rank] += 1
    
    for  frequency in frequencies.values():
        frequencies_list.append(int(frequency))
        
    frequencies_list.sort() 
    
    if frequencies_list[1] == 2:
        return True
    else:
        return False       
                    
            
                    

def check_one_pairs(hand):
    
    """检测是不是一个对子"""
    frequencies={}
    frequencies_list=[]
    ranks = [i[0] for i in hand]
    for rank in ranks:
        if rank not in frequencies:
            frequencies[rank] = 1
        else:
            frequencies[rank] += 1
    
    for  frequency in frequencies.values():
        frequencies_list.append(int(frequency))
        
    frequencies_list.sort() 
    
    if frequencies_list[1] == 1:
        if frequencies_list[2] == 1:
            if frequencies_list[3] == 2:
                return True
            else:
                return False     
        else:
            return False   
    else:
        return False   
    
def judge(hand):
    if check_four_of_a_kind(hand):
        return 1
    elif check_full_house(hand):
        return 2
    elif check_flush(hand):
        return 3
    elif check_straight(hand):
        return 4
    elif check_three_of_a_kind(hand):
        return 5
    elif check_two_pairs(hand):
        return 6
    elif check_one_pairs(hand):
        return 7
    elif check_straight_flush(hand):
        return 8
    else:
        return 9
