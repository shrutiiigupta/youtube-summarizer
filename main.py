import vid_to_text
import streamlit as st
# import pegasus_summarizer
import nlp_summarizer

st.set_page_config(layout="wide")

st.markdown("# Youtube Summarizer ")

col1, col2 = st.columns(2)
col1.subheader("Youtube video")
col2.subheader("Summarized text")

video_link = col1.text_input("Enter Youtube video link")

if(col1.button('Submit')):
    col1.video(video_link)
    if(vid_to_text(video_link)):
        # col2.markdown(pegasus_summarizer())
        col2.markdown(nlp_summarizer())
    else:
        col2.markdown("Processing...")





