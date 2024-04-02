import pandas as pd
import streamlit as st
from sqlalchemy import *
from mysql import *

def ChannelData(data):
    FullChannelDetails = data
    
    requiredChannelDetails = ({
        "CHANNELID" : [FullChannelDetails["items"][0]["snippet"]["customUrl"]],
        "CHANNELNAME" : [FullChannelDetails["items"][0]["snippet"]["title"]],
        "CHANNELTYPE" : [FullChannelDetails["items"][0]["kind"]],
        "CHANNELVIEWS" : [FullChannelDetails["items"][0]["statistics"]["viewCount"]],
        "CHANNELDESCRIPTION" : [FullChannelDetails["items"][0]["snippet"]["description"]],
        "CHANNELSTATUS" : [FullChannelDetails["items"][0]["snippet"]["title"]]       
        })
    StoredChannelData = pd.DataFrame(requiredChannelDetails)
    engine = create_engine('mysql://ramya:root123@localhost/youtubeharvesting')
    StoredChannelData.to_sql('channel', con=engine, if_exists='append', index=False)    
    
    return requiredChannelDetails

    
def UploadChannelData(requiredChannelDetails):
       if(requiredChannelDetails!=null):
        StoredChannelData = pd.DataFrame(requiredChannelDetails)
        engine = create_engine('mysql://ramya:root123@localhost/youtubeharvesting')
        StoredChannelData.to_sql('channel', con=engine, if_exists='append', index=False)    
    
    
def VideoData(data):
    FullVideoDetails = data
    
    requiredChannelDetails = {"VIDEOID" : [FullVideoDetails["items"][0]["id"]],
        "VIDEONAME" : [FullVideoDetails["items"][0]["snippet"]["title"]],
        "VIDEOTYPE" : [FullVideoDetails["items"][0]["kind"]],
        "VIDEOVIEWS" : [FullVideoDetails["items"][0]["statistics"]["viewCount"]],
        "VIDEODESCRIPTION" : [FullVideoDetails["items"][0]["snippet"]["description"]],
        "VIDEOSTATUS" : [FullVideoDetails["items"][0]["snippet"]["title"]]}
  
    StoredChannelData = pd.DataFrame(requiredChannelDetails)
    st.write(StoredChannelData)
