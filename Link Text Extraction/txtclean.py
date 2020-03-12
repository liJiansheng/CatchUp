from datetime import datetime
#import boto3
#from botocore.client import Config
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import re

def handler(event, context):
    
    #cur_dt = "{:%B %d, %Y}".format(datetime.now())

    #BUCKET_NAME = 'newsscrape'
    #FILE_NAME = cur_dt + "latest.csv"
    txt=[]
    txtDict={}
    
    for r in event['link']:
        scraptxt=scrap_webpage(r)
        content_text = BeautifulSoup(scraptxt).get_text()
        letters_only = re.sub("[^a-zA-Z]", " ", content_text)
        txt.append(letters_only)
    txtDict['content']=txt
    txt_df=pd.DataFrame.from_dict(txtDict)
    txt_str=txt_df.to_json()
    txt_json=json.loads(txt_str)
# S3 Connect
    #s3 = boto3.client('s3')
    #headers = {'Content-type: application/json'}
    # Uploaded File
    #s3.put_object(Bucket=BUCKET_NAME, Key=FILE_NAME, Body=txt)
    req = requests.post(url = "https://enigmatic-island-62258.herokuapp.com/",json=txt_json) 

    return req.text
    
def scrap_webpage(l):
    webpage_url = l
    page = requests.get(webpage_url)
    try:
        soup = BeautifulSoup(page.content, "html.parser")
    # search all html lines containing table data
        news_text = soup.find_all('p')
        df = pd.DataFrame.from_dict(news_text)
        write_data = df.to_csv(index=False)
    except:
        print("No text extracted!")
        write_data="No text" 

    return write_data