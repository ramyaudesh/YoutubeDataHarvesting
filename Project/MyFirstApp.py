import streamlit as st
from streamlit_option_menu import option_menu

# 1. as sidebar
with st.sidebar:
    selectionMenu = option_menu(
        menu_title="Menu",    #required
        menu_icon="list", #optional
        options=["Dashboard","Channels"], #required
        icons=["speedometer2","building-add"], #optional
        # default_index=0, #optional 
    )

if selectionMenu == "Channels":
    st.title("YouTube Channels Harvesting")
    st.text_input("Enter the Channel Id")
    st.button(label='Get channels')
   
else:
    st.title("You have selected")
