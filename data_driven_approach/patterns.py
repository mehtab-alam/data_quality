#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 23:38:40 2021

@author: syed
"""




class Patterns:
    
    def addPattern(self, nlp, patterns):
        self.addHostPattern(patterns)
        self.addAgentPattern(patterns)
        ruler = nlp.add_pipe("entity_ruler", config={"validate": True})
        ruler.add_patterns(patterns)
        #ruler.add_patterns(patterns2)
        
        nlp.to_disk("./pipeline/entity_ruler")
    
    def addAgentPattern(self, patterns):
        #regex = r"(?)H\d+N\d+" 
        pattern = {"label": "AGENT", "pattern": [{"TEXT":{"REGEX": "H\d+N\d+"}}]}
        pattern1 = {"label": "AGENT", "pattern": [{"LOWER":"low"}, {"LOWER":"pathogenic"}]}
        pattern2 = {"label": "AGENT", "pattern": [{"LOWER":"high"}, {"LOWER":"pathogenic"}]}
        pattern3 = {"label": "AGENT", "pattern": [{"TEXT":{"REGEX": "[lh]pai"}}]}
        pattern4 = {"label": "AGENT", "pattern": [{"TEXT":{"REGEX": "[LH]PAI"}}]}
        pattern5 = {"label": "AGENT", "pattern": [{"LOWER":"highly"}, {"LOWER":"pathogenic"}]}
        
        patterns.append(pattern)
        patterns.append(pattern1)
        patterns.append(pattern2)
        patterns.append(pattern3)
        patterns.append(pattern4)
        patterns.append(pattern5)
        return patterns
    
    def addHostPattern(self, patterns):
        #regex = r"(?)H\d+N\d+"
        pattern1 = {"label": "HOST", "pattern": [{"LOWER":"poultry"}]}
        pattern2 = {"label": "HOST", "pattern": [{"LOWER":"chicken"}]}
        pattern3 = {"label": "HOST", "pattern": [{"LOWER":"duck"}]}
        pattern4 = {"label": "HOST", "pattern": [{"LOWER":"peacock"}]}
        pattern5 = {"label": "HOST", "pattern": [{"LOWER":"pig"}]}
        pattern6 = {"label": "HOST", "pattern": [{"LOWER":"goat"}]}
        pattern7 = {"label": "HOST", "pattern": [{"LOWER":"cattle"}]}
        pattern9 = {"label": "HOST", "pattern": [{"LOWER":"bird"}]}
        pattern10 = {"label": "HOST", "pattern": [{"LOWER":"human"}]}
        pattern11 = {"label": "HOST", "pattern": [{"LOWER":"chickens"}]}
        pattern12 = {"label": "HOST", "pattern": [{"LOWER":"ducks"}]}
        pattern13 = {"label": "HOST", "pattern": [{"LOWER":"peacocks"}]}
        pattern14 = {"label": "HOST", "pattern": [{"LOWER":"pigs"}]}
        pattern15 = {"label": "HOST", "pattern": [{"LOWER":"goats"}]}
        pattern16 = {"label": "HOST", "pattern": [{"LOWER":"cattles"}]}
        pattern17 = {"label": "HOST", "pattern": [{"LOWER":"peacocks"}]}
        pattern18 = {"label": "HOST", "pattern": [{"LOWER":"birds"}]}
        pattern19 = {"label": "HOST", "pattern": [{"LOWER":"humans"}]}
        
        pattern20 = {"label": "HOST", "pattern": [{"LOWER":"eagle"}]}
        pattern21 = {"label": "HOST", "pattern": [{"LOWER":"eagles"}]}
        pattern22 = {"label": "HOST", "pattern": [{"LOWER":"falcon"}]}
        pattern23 = {"label": "HOST", "pattern": [{"LOWER":"falcons"}]}
        pattern24 = {"label": "HOST", "pattern": [{"LOWER":"goose"}]}
        pattern25 = {"label": "HOST", "pattern": [{"LOWER":"gooses"}]}
        pattern26 = {"label": "HOST", "pattern": [{"LOWER":"guineafowl"}]}
        pattern27 = {"label": "HOST", "pattern": [{"LOWER":"guineafowls"}]}
        pattern28 = {"label": "HOST", "pattern": [{"LOWER":"gull"}]}
        pattern29 = {"label": "HOST", "pattern": [{"LOWER":"gulls"}]}
        pattern30 = {"label": "HOST", "pattern": [{"LOWER":"heron"}]}
        pattern31 = {"label": "HOST", "pattern": [{"LOWER":"herons"}]}
        pattern32 = {"label": "HOST", "pattern": [{"LOWER":"ostrich"}]}
        pattern33 = {"label": "HOST", "pattern": [{"LOWER":"ostriches"}]}
        pattern34 = {"label": "HOST", "pattern": [{"LOWER":"pigeon"}]}
        pattern35 = {"label": "HOST", "pattern": [{"LOWER":"pigeons"}]}
        pattern36 = {"label": "HOST", "pattern": [{"LOWER":"turkey"}]}
        pattern37 = {"label": "HOST", "pattern": [{"LOWER":"turkeys"}]}
        pattern38 = {"label": "HOST", "pattern": [{"LOWER":"quail"}]} 
        pattern39 = {"label": "HOST", "pattern": [{"LOWER":"quails"}]} 
        
        patterns.append(pattern1)
        patterns.append(pattern2)
        patterns.append(pattern3)
        patterns.append(pattern4)
        patterns.append(pattern4)
        patterns.append(pattern5)
        patterns.append(pattern6)
        patterns.append(pattern7)
        patterns.append(pattern9)
        patterns.append(pattern10)
        patterns.append(pattern11)
        patterns.append(pattern12)
        patterns.append(pattern13)
        patterns.append(pattern14)
        patterns.append(pattern15)
        patterns.append(pattern16)
        patterns.append(pattern17)
        patterns.append(pattern18)
        patterns.append(pattern19)
        patterns.append(pattern20)
        patterns.append(pattern21)
        patterns.append(pattern22)
        patterns.append(pattern23)
        patterns.append(pattern24)
        patterns.append(pattern25)
        patterns.append(pattern26)
        patterns.append(pattern27)
        patterns.append(pattern28)
        patterns.append(pattern29)
        patterns.append(pattern30)
        patterns.append(pattern31)
        patterns.append(pattern32)
        patterns.append(pattern33)
        patterns.append(pattern34)
        patterns.append(pattern35)
        patterns.append(pattern36)
        patterns.append(pattern37)
        patterns.append(pattern38)
        patterns.append(pattern39)
        
        
        return patterns
      
        
        
           