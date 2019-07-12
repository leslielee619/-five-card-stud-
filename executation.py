# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 23:11:23 2019

@author: 14682
"""
"""
写的也比较笨，应该将列表都写入json，然后从json里面读取即可，这样便不会占用内存
这个模块就是运行后得到各个牌型的统计结果，并且得到一个直方图。
"""
import census_hist


frequencies1,frequencies2 = census_hist.census(1e6)
census_hist.hist(frequencies1,1e6)
census_hist.hist(frequencies2,1e6)

