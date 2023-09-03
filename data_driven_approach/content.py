#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:51:22 2021

@author: syed
"""

class ContentScore:
    def __init__(self, access='Accessable', rel='NA', accur='NA', 
                 clar='NA',time='NA',auth='NA',rep='NA', sc = 0):
        self.accessibility = access
        self.reliability = rel
        self.accuracy = accur
        self.clarity = clar
        self.timeliness = time
        self.authority = auth
        self.reputation = rep
        self.score = sc    


    
