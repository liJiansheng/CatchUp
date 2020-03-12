from datetime import datetime
import boto3
from botocore.client import Config
#import  urllib3.request import
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

def handler(event, context):
    
    cur_dt = "{:%B %d, %Y}".format(datetime.now())

    BUCKET_NAME = 'newsscrape'
    FILE_NAME = cur_dt + "latest.csv"
    txt=""

    for r in event['link']:
        txt = txt+scrap_webpage(r)
    # S3 Connect
    s3 = boto3.client('s3')

    # Uploaded File
    s3.put_object(Bucket=BUCKET_NAME, Key=FILE_NAME, Body=txt)

    return "{'data':'received!'}"
    
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