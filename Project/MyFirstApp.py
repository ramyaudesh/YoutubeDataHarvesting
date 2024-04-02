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


