from pytube import YouTube

def audio_to_text(link):
    # print("checkk ekckekdkeijfiuhsiuty")
    yt_video = YouTube(link)
    yt_video.set_filename('xx')
    audio = yt_video.streams.filter(only_audio=True, file_extension='mp4')[0]
    audio.download()

    # text = open("transcript.txt",'w')
    # text.write(clean_data)
    # text.close()

    return("hiiiiiiiiii")