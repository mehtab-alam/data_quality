#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 00:57:56 2021

@author: syed
"""

from py_heideltime import py_heideltime
import streamlit as st

class TemporalInformationExtractor:
    
    def getTempralInformation(self, doc):
        temporalEntities = []
        for sentence in doc.sents:
            #results = py_heideltime(sentence.text)
            results = py_heideltime(sentence.text, language='English',  document_type='news')
            # st.text(str(results))
            temporalEntities.append(sentence)
                    
        return temporalEntities