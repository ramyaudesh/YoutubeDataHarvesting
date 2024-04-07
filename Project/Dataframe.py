import pandas as pd
import streamlit as st
from sqlalchemy import *
from mysql import *

engine = create_engine('mysql://ramya:root123@localhost/youtubeharvesting')

def UploadDataToTable(data,table):
    data.to_sql(table, con=engine, if_exists='append', index=False)    

def querySqlTables(query):
    result = pd.read_sql_query(query,engine)
    return result
  
def ChannelData(FullChannelDetails):
    if FullChannelDetails!=0:

        requiredChannelDetails = ({
            "CHANNELID" : [FullChannelDetails["items"][0]["id"]],
            "CHANNELNAME" : [FullChannelDetails["items"][0]["snippet"]["title"]],
            "CHANNELTYPE" : [FullChannelDetails["items"][0]["kind"]],
            "CHANNELVIEWS" : [FullChannelDetails["items"][0]["statistics"]["viewCount"]],
            "CHANNELDESCRIPTION" : [FullChannelDetails["items"][0]["snippet"]["description"]],
            "CHANNELSTATUS" : [FullChannelDetails["items"][0]["snippet"]["title"]],      
            })

        Uploads=  FullChannelDetails["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
        StoredChannelData = pd.DataFrame(requiredChannelDetails)
        UploadDataToTable(StoredChannelData,"channel")
        
        # st.write("Extracted Uploads Url is------------>"+ Uploads)
        st.toast('Hooray!! Channel data extracted and uploaded to database!!', icon='🎉')
        return Uploads

def PlaylistData(FullPlaylistDetails):
    if FullPlaylistDetails!=0:

        requiredPlaylistDetails = ({
            "PlaylistID":[FullPlaylistDetails["items"][0]["snippet"]["playlistId"]],
            "ChannelID":[FullPlaylistDetails["items"][0]["snippet"]["channelId"]],
            "PlaylistName":[FullPlaylistDetails["items"][0]["snippet"]["title"]]
            })
        StoredPlaylistData = pd.DataFrame(requiredPlaylistDetails)
        UploadDataToTable(StoredPlaylistData,"playlist")
        # st.write(requiredPlaylistDetails)
        
        requiredVideoIdList = []
        for item in FullPlaylistDetails["items"]:
            videoIds = dict(
                videoId = item["snippet"]["resourceId"]["videoId"]
                )
            requiredVideoIdList.append(videoIds)
            
        # st.write(requiredVideoIdList)
        return requiredVideoIdList
        
def VideoData(FullVideoDetails,playlistIdI):
    if FullVideoDetails!=0:

        videosList =  []
        for item in FullVideoDetails["items"]:
            requiredVideoDetails = dict(
                VideoID = item["id"],
                ChannelID = item["snippet"]["channelId"],
                PlaylistID = playlistIdI,
                VideoName = item["snippet"]["title"],
                VideoDescription = item["snippet"]["description"],
                PublishedDate =item["snippet"]["publishedAt"],
                ViewCount =item["statistics"]["viewCount"],
                LikeCount =item["statistics"]["likeCount"],
                DisLikeCount =item["statistics"]["favoriteCount"],
                FavoriteCount = item["statistics"]["favoriteCount"],
                CommentCount =item["statistics"]["commentCount"],
                Duration =item["contentDetails"]["duration"],
                thumbnail = item ["snippet"]["thumbnails"],
                CaptionStatus =item["contentDetails"]["caption"],
                )
            videosList.append(requiredVideoDetails)
            
        StoredVideoData = pd.DataFrame(videosList)
        UploadDataToTable(StoredVideoData,"video")
        # st.write(StoredVideoData)

def CommentsData(FullCommentsDetails):
    if FullCommentsDetails!=0:

        commentsList =  []
        for item in FullCommentsDetails["items"]:
            requiredCommentsDetails = dict(
            CommentID = item["snippet"]["topLevelComment"]["id"],
            VideoID = item["snippet"]["videoId"],
            CommentText = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"],
            CommentAuthor = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
            Commentpublisheddate = item["snippet"]["topLevelComment"]["snippet"]["publishedAt"])
            
            commentsList.append(requiredCommentsDetails)
        StoredCommentsData = pd.DataFrame(commentsList)
        UploadDataToTable(StoredCommentsData,"comment")
        # st.write(StoredCommentsData)