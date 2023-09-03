#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:42:49 2021

@author: syed
"""

class MetadataScore:
    def __init__(self, p='NA', su='NA', de='NA', s='NA',t='NA',l='NA',r='NA',d='NA', k = 'NA', sc = 0):
        self.publisher = p
        self.subject = su
        self.description = de
        self.source = s
        self.type = t
        self.language = l
        self.rights = r
        self.date = d
        self.keywords = k
        self.score = sc
    
    def metascore(self):
        if(self.publisher == 'NA'):
            self.score += 1
        else:
            self.score += 2
        if(self.subject == 'NA'):
            self.score += 1
        else:
            self.score += 2
        if(self.description == 'NA'):
            self.score += 1
        else:
            self.score += 2
        if(self.source == 'NA'):
            self.score += 1
        else:
            self.score += 2 
        if(self.type == 'NA'):
            self.score += 1
        else:
            self.score += 2
        if(self.language == 'NA'):
            self.score += 1
        else:
            self.score += 2
        if(self.rights == 'NA'):
            self.score += 1
        else:
            self.score += 2
        if(self.date == 'NA'):
            self.score += 1
        else:
            self.score += 2  
            
            
# =============================================================================
#     def __str__(self): 
#         return "%s    %s     %s     %s     %s     %s     %s     %s   %d" %(self.publisher,
#                                                                           self.subject, self.description,
#                                                                           self.source, self.type, self.language,
#                                                                           self.rights, self.date, self.score)
# =============================================================================