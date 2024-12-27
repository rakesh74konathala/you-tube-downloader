import os
import yt_dlp

cur_dir = os.getcwd()


def download_video(link, id):
    youtube_dl_options = {
        "format": "b",
        "outtmpl": os.path.join(cur_dir, f"{id}.mp4")
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])
        
        
download_video('https://www.youtube.com/watch?v=ERZR-tPASto','video_filename')        