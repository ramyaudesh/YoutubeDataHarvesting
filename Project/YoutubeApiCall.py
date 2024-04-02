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


    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
def channel_api_call(channelId):    
        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",id=channelId
        )
        channelResponse = request.execute()
        st.write(channelResponse)
        ChannelData(channelResponse)
         
def videos_api_call(videoId):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",id=videoId
        )
        response = request.execute()

        st.write(response)
        ChannelData(response)
        
def playlist_api_call(playlistId):
        request = youtube.playlists().list(
            part="snippet,contentDetails,statistics",id=playlistId
        )
        response = request.execute()

        st.write(response)
        ChannelData(response)
        
def comments_api_call(commentsId):
        request = youtube.comments().list(
            part="snippet,contentDetails,statistics",id=commentsId
        )
        response = request.execute()

        st.write(response)
        ChannelData(response)