import streamlit as st
import pandas as pd
import io
from bs4 import BeautifulSoup
import requests
import spacy
from util import Util
from patterns import Patterns
from http import cookiejar 
from outbreak_detection import OutbreakDetector
from temporalExtractor import TemporalInformationExtractor 
from data_processing_score import DataProcessingScore
import json
from urllib.parse import urlparse
from urllib.parse import parse_qs
from sutime import SUTime

class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

def get_url_from_googlenews(url):
    parsed_url = urlparse(url)
    return parse_qs(parsed_url.query)['url'][0]

def main():	
    st.set_page_config(layout="wide")
    st.title("Dataset quality")
    file = st.file_uploader("Upload a file", type=("csv", "xls","xlsx")) 
    dataScores = []   
    patterns = []
    util = Util()  
    outbreak_detector = OutbreakDetector()
    URL = 'https://www.google.com/search?q=inurl:'
    URLEND = '&as_qdr=y25'
    temporalExtractor = TemporalInformationExtractor()
    dataProcessingScore = DataProcessingScore()
    if file:
        uploaded_file = io.TextIOWrapper(file)
        
        
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file, error_bad_lines=False)
            pd.set_option('display.max_rows', 500)
            st.success("Total Row count:"+ str(len(df)))
            nlp = spacy.load('en_core_web_sm')
            pattern = Patterns()
            pattern.addPattern(nlp, patterns)
            #pattern.addAgentPattern(nlp, patterns)
            #nlpsci = spacy.load('en_core_sci_sm')
            for index, row in df.iterrows():
                url = row['url']
                if (isinstance(url, str)):
                    if('news.google.com' in url):
                        url = get_url_from_googlenews(url)
                st.text(url)
                page = ''
                #page1 = ''
                
                
                try:
                    session = requests.Session()
                    session.cookies.set_policy(BlockAll())
                    page = requests.get(url, verify=False)
                    #page1 = session.get(URL+row['url']+URLEND, verify=False)
                
                
                
                #st.text(row['url'] +"    "+ str(page.status_code))
                    soup = BeautifulSoup(page.content, 'html.parser')
                    metadataScore = util.getMetadataScore(soup)
                    doc = nlp(row['title']+'.'+ row['text'])
                    
                    contentScore = util.getContentScore(metadataScore, dataProcessingScore, doc.ents ,page.status_code)
                    sentences = outbreak_detector.getOutbreakSentences(doc)
                    #tmpInformation = temporalExtractor.getTempralInformation(doc)
                    outbreak = 'NA'
                    if(len(sentences) > 0):
                        outbreak = 'Outbreak:'+ str(sentences)+',No. of outbreak Sentences:'+ str(len(sentences))
                    #util.getPublishDate(page1)
                    #util.printEntity(doc)
                    dataScores.append({'ArticleID':row['id'],'Title':row['title'],'Text':row['text'],'URL':url,
                                       'Publisher': metadataScore.publisher,'Subject': metadataScore.subject,
                                       'Description': metadataScore.description, 
                                       'Source': metadataScore.source,'Type': metadataScore.type, 
                                       'Language': metadataScore.language,
                                       'Rights': metadataScore.rights, 'Date': metadataScore.date, 'keywords': metadataScore.keywords, 
                                       'Metadata Score': metadataScore.score, 'Status Code':page.status_code, 'Accessibility': contentScore.accessibility,
                                       'Reliability': contentScore.reliability,'Clarity': contentScore.clarity, 'Authority': contentScore.authority,
                                       'Accuracy': outbreak,'Content Score': contentScore.score,
                                       'Spatial Entities': dataProcessingScore.spatialEntities,
                                       'Temporal Entities': dataProcessingScore.temporalEntities,
                                       'Thematic Entities': dataProcessingScore.thematicEntities,
                                       'Data Processing Score': dataProcessingScore.score})
               
                except:
                    print('URL Exception')
            st.text(len(dataScores))    
            util.populateCSV(dataScores)
            
            
                
if __name__ == '__main__':
	main()	