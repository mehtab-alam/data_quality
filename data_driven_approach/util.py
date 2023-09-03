#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:56:16 2021

@author: syed
"""
import re
from metadata import MetadataScore
import csv
import streamlit as st
from content import ContentScore
from spacy import displacy
from bs4 import BeautifulSoup
from data_processing_score import DataProcessingScore

class Util:
    
    def getPublishDate(self, page):
        
        st.success(page.content)
        soup = BeautifulSoup(page.content, 'html.parser')
        spans = soup.find_all('span', attrs={'class':'aCOpRe'})
        st.success(len(spans))
        for span in spans:
            st.success(span.string)
    
    def printEntity(self, doc):
        HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""
        html = displacy.render(doc, style="ent")
        # Newlines seem to mess with the rendering
        html = html.replace("\n", " ")
        st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)
    
    def getMetadataScore(self,soup):
        lang = soup.find_all('html', {"lang" : re.compile(r".*")})
        metadataScore = MetadataScore('NA', 'NA','NA','NA','NA','NA', 'NA', 'NA', 'NA', 0)
        for attr in lang:
            metadataScore.language = attr.get('lang')
        meta = soup.find_all('meta', {"property" : re.compile(r".*")})
        keys = soup.find_all('meta', {"name" : re.compile(r".*")})
        for keyGroup in keys:
            if('keyword' in keyGroup.get('name')): 
                metadataScore.keywords = keyGroup.get('content')
        for metadata in meta:
            if('url' in metadata.get('property')):
                metadataScore.source = metadata.get('content')
            if('site' in metadata.get('property')):    
                metadataScore.publisher = metadata.get('content')
            if('title' in metadata.get('property')):
                metadataScore.subject = metadata.get('content')
            if('description' in metadata.get('property') ):
                metadataScore.description = metadata.get('content')
            if('og:type' in metadata.get('property')): 
                metadataScore.type = metadata.get('content')
            if('locale' in metadata.get('property')): 
                metadataScore.language = metadata.get('content') 
            
            if('time' in metadata.get('property') or 'date' in metadata.get('property')): 
                metadataScore.date = metadata.get('content')
            if('right' in metadata.get('property')): 
                metadataScore.copyright = metadata.get('content')    
        metadataScore.metascore() 
        return metadataScore

    def populateCSV(self,metadatascores):
    	csv_columns = ['ArticleID','Title','Text','URL','Publisher','Subject','Description', 
                    'Source','Type', 'Language','Rights', 'Date', 'keywords', 'Metadata Score',
                    'Status Code','Accessibility', 'Reliability', 'Accuracy','Clarity','Authority','Content Score',
                    'Spatial Entities','Temporal Entities','Thematic Entities','Data Processing Score']
    
    	csv_file = "data_quality-General.csv"
    	try:
    	    with open(csv_file, 'w') as csvfile:
    	        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    	        writer.writeheader()
    	        for data in metadatascores:
    	            writer.writerow(data)
                    
    	    st.success("Output file: **"+ csv_file+"**")        
    	except IOError:
    	    print("I/O error")

    def getContentScore(self,metadataScore, dataScore,ents,statusCode):
        contentScore = ContentScore('Accessible', 'NA','NA','NA','NA','NA', 'NA', 0)
        hosts = []
        agents = []
        locations = []
        dates =[]
        if(statusCode >= 400 and statusCode <= 410):
            contentScore.accessibility = 'Restricted'
            contentScore.score += 1
        if(statusCode == 404):
            contentScore.accessibility = 'Not Available'
            contentScore.score += 1
        else:
            contentScore.score += 3
        if(metadataScore.score > 13):
            contentScore.clarity = 'Sufficient Metadata'
            contentScore.score += 3
        else:
            contentScore.clarity = 'Insufficient Metadata'
            contentScore.score += 1
        if(metadataScore.publisher != 'NA'):    
            contentScore.authority = metadataScore.publisher
            contentScore.score += 3
        else:
            contentScore.score += 1
            
        for ent in ents:
            if(ent.label_ =='GPE' or ent.label_ =='LOC' and ent.text.casefold() not in (loc.casefold() for loc in locations)):
                locations.append(ent.text)    
            if(ent.label_ =='HOST' and ent.text.casefold() not in (host.casefold() for host in hosts)):
                hosts.append(ent.text) 
            if(ent.label_ =='AGENT' and ent.text.casefold() not in (agent.casefold() for agent in agents)):
                agents.append(ent.text)
            if(ent.label_ =='DATE' and ent.text.casefold() not in (date.casefold() for date in dates)):
                dates.append(ent.text)
               
        if(len(hosts) > 0):
            contentScore.score += 1
        if(len(agents) > 0):
            contentScore.score += 1
        if(len(locations) > 0):
            contentScore.score += 1
        if(len(hosts) > 0 or len(agents) > 0 or len(locations) > 0):
            dataScore.spatialEntities = "Spatial Entities---"+ str(locations)
            dataScore.temporalEntities = "Temporal Entities---"+ str(dates)
            dataScore.thematicEntities = "Thematic Entities--- Host(s):"+str(hosts)+",Agent(s):"+ str(agents)
            contentScore.reliability = "Location(s):"+ str(locations)+ ",Host(s):"+str(hosts)+",Agent(s):"+ str(agents)
        return contentScore    
    