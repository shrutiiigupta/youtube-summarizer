import logging
from youtube_transcript_api import YouTubeTranscriptApi as yta
import streamlit as st
import audio_to_text


def vid_to_text(link):

    # harman singh - manual script - https://youtu.be/Wn9iALMyS7c?si=q0LYZBrR9mSbj2b7
    # netflix death note dhruv rathee - no script allowed - https://www.youtube.com/watch?v=H3nzTmNlS4I&t=32s
    # power couple - auto-generated only - https://www.youtube.com/watch?v=6dpF_G3yMMQ

    id = link.split('/')
    vid_id = id[-1]
    # print(vid_id)

    try:
        data = yta.get_transcript(vid_id, languages=['en-IN', 'en'])
        return(clean_text(data))
    except:
        data = audio_to_text(link)

    # print(data)

def clean_text(data):
    final_data = ''
    for val in data:
        for key,value in val.items():
            if key == 'text':
                final_data += ' ' + value

    # print(final_data)
    process_data = final_data.splitlines()
    clean_data = ''.join(process_data)
    # print(clean_data)
    text = open("transcript.txt",'w')
    text.write(clean_data)
    text.close()

    return(clean_data)