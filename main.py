import vid_to_text as v
import streamlit as st
import time
import vid_id_extract
import os
from metrics_eval import meteor , rouge_score_1 , bertScore_basic, bertScore_intmed,bertScore

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

        # if(col1.button('Get Metric scores')):
        c1,c2,c3,c4=st.columns(4)
        # with c1:
        c1.markdown("### Meteor Score : "+ "\n #### " + str(meteor.meteor()))
        # with c2:
        c2.markdown("### Rouge Score : "+ "\n #### " + str(rouge_score_1.rouge()))
        # with c3:
        try:
            c3.markdown("### bertScore Score : "+ "\n #### " + str(bertScore.bertScore_different()))
        except:
            c3.markdown("## bertScore_basic Score : "+ "\n #### " + str(bertScore_basic.bertScore_basic()))
        # with c4:
        c4.markdown("### bertScore_intmed Score : "+ "\n #### " + str(bertScore_intmed.bert_intmed()))

# os.remove('./audiofile.mp3')






