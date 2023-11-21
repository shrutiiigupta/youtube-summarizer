from pytube import YouTube

def audio_to_text(link):
    # print("checkk ekckekdkeijfiuhsiuty")
    yt_video = YouTube(link)
    audio = yt_video.streams.filter(only_audio=True, file_extension='mp4')[0]
    audio.download()

    return("hiiiiiiiiii")