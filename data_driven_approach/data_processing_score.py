#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 03:05:40 2021

@author: syed
"""

class DataProcessingScore:
    def __init__(self, SE='Accessable', TE='NA', THE='NA', sc = 0):
        self.spatialEntities = SE
        self.temporalEntities = TE
        self.thematicEntities = THE
        self.score = sc    