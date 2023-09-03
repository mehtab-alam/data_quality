#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 02:55:10 2021

@author: syed
"""
import spacy
import streamlit as st
from spacy.tokenizer import Tokenizer

outbreak_keywords =  [ #mortality 
                        'death',
                        'die',
                        'kill',
                        'cull'
                        'claim',
                        'fatality',
                        'decease',
                        'deceased',
                        #hospitalized
                        'hospitalization',
                        'hospital',
                        'hospitalize',
                        'recovery', 
                        #cases
                        'case',
                        'infect',
                        'infection',
                        'strike',
                        'stricken',
                        #case status
                        'suspect', 
                        'suspected',
                        'report',
                        'reported'
                        'outbreak',
                        'confirm',
                        'confirmed',
                        'positive']

outbreak_attributes = [
                # count precisions
                'approximate',
                'max',
                'min',
                'average',
                # case status
                'confirmed',
                'suspected',
                # count anchors
                'cumulative',
                'incremental',
                'ongoing',
                # count units
                'case',
                'death',
                'recovery',
                'hospitalization',
                # count periods
                'annual',
                'monthly',
                'weekly',
            ]
class OutbreakDetector:
    
    def getOutbreakSentences(self, doc):
        sentences = []
        for sentence in doc.sents:
           
           for token in sentence:
               if token.lemma_.lower() in outbreak_keywords:
                    sentences.append(sentence)
                    break
        return sentences
    