import vid_to_text as v
import streamlit as st
import time
import vid_id_extract
import os
from metrics_eval import meteor , rouge

# print(st.__file__)

st.set_page_config(layout="wide")

st.markdown("# Youtube Summarizer ")

col1, col2 = st.columns(2)
col1.subheader("Youtube video")
col2.subheader("Summarized text")

video_link = col1.text_input("Enter Youtube video link")

if(col1.button('Submit')):
    with st.spinner('Loading...'):
        time.sleep(2)

    vid_id=vid_id_extract.video_id(video_link)
    # print(vid_id)
    if vid_id==None:
        col1.error("Invalid URL")
        col1.info("Please Enter valid URL")
    else:
        col1.video(video_link)
        col2.markdown(v.vid_to_text(video_link ,vid_id))
    
        c1,c2,c3,c4=st.columns(4)
        with c1:
            c1.markdown("## Meteor Score : "+ "\n #### " + str(meteor.meteor()))
        with c2:
            c2.markdown("## Rouge Score : "+ "\n #### " + str(rouge.rouge()))

# os.remove('./audiofile.mp3')






