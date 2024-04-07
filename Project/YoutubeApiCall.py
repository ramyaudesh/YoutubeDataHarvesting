import os
import pprint
from  Dataframe import*
import streamlit as st
import googleapiclient.discovery
import googleapiclient.errors

credentials = "AIzaSyANOJcW8-b6NgYAk87VtYF1081fU-Z4rP8"
api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(
api_service_name, api_version, developerKey=credentials)


def extractData(channelId):
    
    if channelId!=0:
        # 1.Extract channel data - and get playlist id
        playlistId = channel_api_call(channelId)
            
        #2.Pass playlist id to playlist api
        videosData = playlist_api_call(playlistId)

        #3.Get videos and comments details 
        for video in videosData:
            videos_api_call(video,playlistId)
            comments_api_call(video)
        
def channel_api_call(channelIdInput):    
    if channelIdInput!=0:

        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",id=channelIdInput
        )
        channelResponse = request.execute()
        # st.write(channelResponse)
        uploads = ChannelData(channelResponse)
        return uploads
        
def playlist_api_call(playlistIdInput):
    if playlistIdInput!=0:

        request = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlistIdInput
        )
        response = request.execute()

        # st.write(response)
        videosData = PlaylistData(response)
        df=pd.DataFrame(videosData)
        videoList = df["videoId"].values.tolist()
        return videoList
         
def videos_api_call(videoIdInput,playlistIdI):
    if videoIdInput!=0:

        request = youtube.videos().list(
            part='contentDetails,id,snippet,statistics,status',id=videoIdInput,maxResults=10
        )
        response = request.execute()

        # st.write(response)
        VideoData(response,playlistIdI)
        
def comments_api_call(commentsIdInput):
    if commentsIdInput!=0:
        request = youtube.commentThreads().list(
            part="snippet",videoId=commentsIdInput,maxResults=10
        )
        response = request.execute()

        # st.write(response)
        CommentsData(response)