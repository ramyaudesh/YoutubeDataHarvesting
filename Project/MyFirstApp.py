import requests
import streamlit as st
from streamlit_option_menu import option_menu
from YoutubeApiCall import*
import googleapiclient.errors
from Dataframe import *
# 1. as sidebar
with st.sidebar:
    selectionMenu = option_menu(
        menu_title="Menu",    #required
        menu_icon="list", #optional
        options=["Dashboard","Channels"], #required
        icons=["speedometer2","building-add"], #optional
        default_index=0, #optional 
    )


if selectionMenu == "Channels":
    st.title("YouTube Channels Harvesting")
    channelId= st.text_input("Enter Data")
    st.button(label='Extract Data', on_click=channel_api_call(channelId))
    # st.button(label='Extract Data', on_click=videos_api_call(IdInput))
    # st.button(label='Extract Data', on_click=playlist_api_call(IdInput))
    # st.button(label='Extract Data', on_click=comments_api_call(IdInput))

    # st.button(label='Upload to MySql',on_click=UploadChannelData(requiredChannelDetails))
    

else:
    st.title("Welcome to the Dashboard !!")
    st.selectbox(label= 'Choose the options', options=[
            'What are the names of all the videos and their corresponding channels?',
            'Which channels have the most number of videos, and how many videos do they have?',
            'What are the top 10 most viewed videos and their respective channels?',
            'How many comments were made on each video, and what are their corresponding video names?',
            'Which videos have the highest number of likes, and what are their corresponding channel names?',
            'What is the total number of likes and dislikes for each video, and what are their corresponding video names?',
            'What is the total number of views for each channel, and what are their corresponding channel names?',
            'What are the names of all the channels that have published videos in the yea 2022?',
            'What is the average duration of all videos in each channel, and what are their corresponding channel names?',
            'Which videos have the highest number of comments, and what are their corresponding channel names?'])


