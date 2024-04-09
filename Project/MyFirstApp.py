import streamlit as st
from streamlit_option_menu import option_menu
from YoutubeApiCall import*
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
    channelId= st.text_input("Enter Channel ID Below")
    
    def click_button():
        st.session_state.clicked = true
        extractData(channelId)
        
    if 'clicked' not in st.session_state:
        st.session_state.clicked = false
    
    if st.session_state.clicked:           
     st.button(label='Extract Data', on_click=click_button)
     
else:
    st.title("Welcome to the Dashboard !!")
    question = st.selectbox(label= 'Choose the options', options=[
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

    if question == 'What are the names of all the videos and their corresponding channels?':
        query = "SELECT video.VideoName, channel.ChannelName FROM video INNER JOIN channel ON video.ChannelID =channel.ChannelID;"
        result = querySqlTables(query) 
    elif question == 'Which channels have the most number of videos, and how many videos do they have?':
        query = "select count(VideoID) as VideoCount, channel.ChannelName from video INNER JOIN channel ON video.ChannelID=channel.ChannelID group by ChannelName;"
        result = querySqlTables(query) 
    elif question == 'What are the top 10 most viewed videos and their respective channels?':
        query = "select video.VideoName, video.ViewCount , channel.ChannelName from video INNER JOIN channel ON video.ChannelID =channel.ChannelID Order By ViewCount DESC limit 10;"
        result = querySqlTables(query) 
    elif question == 'How many comments were made on each video, and what are their corresponding video names?':
        query = "SELECT VideoName, COUNT(CommentID) AS comment_count FROM video JOIN comment ON video.VideoID = comment.VideoID GROUP BY VideoName ORDER BY comment_count DESC"
        result = querySqlTables(query) 
    elif question == 'Which videos have the highest number of likes, and what are their corresponding channel names?':
        query = "SELECT video.VideoName, channel.ChannelName FROM channel JOIN playlist ON channel.ChannelID= playlist.ChannelID JOIN video ON playlist.PlaylistID = video.PlaylistID where LikeCount = (select max(LikeCount) from video);"
        result = querySqlTables(query) 
    elif question == 'What is the total number of likes and dislikes for each video, and what are their corresponding video names?':
        query = "SELECT VideoName, LikeCount, DisLikeCount FROM video ORDER BY LikeCount DESC, DisLikeCount DESC;"
        result = querySqlTables(query) 
    elif question == 'What is the total number of views for each channel, and what are their corresponding channel names?':
        query = "SELECT ChannelName,ChannelViews FROM channel ORDER BY ChannelViews DESC;"
        result = querySqlTables(query) 
    elif question == 'What are the names of all the channels that have published videos in the yea 2022?':
        query = "SELECT DISTINCT(ChannelName) FROM channel JOIN playlist ON channel.ChannelID= playlist.ChannelID JOIN video ON playlist.PlaylistID = video.PlaylistID WHERE EXTRACT(YEAR FROM video.PublishedDate) = 2022;"
        result = querySqlTables(query) 
    elif question == 'What is the average duration of all videos in each channel, and what are their corresponding channel names?':
        query = "SELECT ChannelName, AVG(Duration) as AverageDuration FROM channel JOIN playlist ON channel.ChannelID= playlist.ChannelID JOIN video ON playlist.PlaylistID = video.PlaylistID GROUP BY ChannelName order BY AVG(Duration) DESC;"
        result = querySqlTables(query) 
    elif question == 'Which videos have the highest number of comments, and what are their corresponding channel names?':
        query = "SELECT VideoName, ChannelName  FROM channel JOIN playlist ON channel.ChannelID = playlist.ChannelID JOIN video ON playlist.PlaylistID = video.PlaylistID where CommentCount = (select max(CommentCount) from video);"
        result = querySqlTables(query) 
    else:
        result="No query selected !"

    tab1, tab2 = st.tabs(['Data', 'Charts'])
    with tab1:
        st.header("DataTable")
        st.write(result)

    with tab2:
        st.header("DataAnalysisChart")
        chart_data = pd.DataFrame(result)
        if question == 'What are the names of all the videos and their corresponding channels?':
            st.bar_chart(chart_data,x="ChannelName",y="VideoName")
        elif question == 'Which channels have the most number of videos, and how many videos do they have?':
            st.bar_chart(chart_data,x="VideoCount",y="ChannelName")
        elif question == 'What are the top 10 most viewed videos and their respective channels?':
            st.bar_chart(chart_data,x="ChannelName",y="VideoName")
        elif question == 'How many comments were made on each video, and what are their corresponding video names?':
            st.bar_chart(chart_data,x="VideoName",y="comment_count")
        elif question == 'Which videos have the highest number of likes, and what are their corresponding channel names?':
            st.bar_chart(chart_data,x="ChannelName",y="VideoName")
        elif question == 'What is the total number of likes and dislikes for each video, and what are their corresponding video names?':
            st.bar_chart(chart_data,x="VideoName",y=["LikeCount","DisLikeCount"])
        elif question == 'What is the total number of views for each channel, and what are their corresponding channel names?':
            st.bar_chart(chart_data,x="ChannelName",y="ChannelViews")
        elif question == 'What are the names of all the channels that have published videos in the yea 2022?':
            st.bar_chart(chart_data)
        elif question == 'What is the average duration of all videos in each channel, and what are their corresponding channel names?':
            st.bar_chart(chart_data,x="ChannelName",y="AverageDuration")
        elif question == 'Which videos have the highest number of comments, and what are their corresponding channel names?':
            st.bar_chart(chart_data,x="ChannelName",y="VideoName")
        else:
            st.write("No data")
