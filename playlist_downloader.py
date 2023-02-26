import os
from pytube import Playlist
from tqdm import tqdm

link = input("Enter YouTube Playlist URL: ")

yt_playlist = Playlist(link)
count = 1
try:
    os.mkdir("Downloaded")
except:
    pass
total = len(yt_playlist.videos)
for video in tqdm(yt_playlist.videos):
    # print("Video downloading: ", video.title, count, "/", total)
    val = '0'+str(count) if count < 10 else count
    video.streams.get_highest_resolution().download("./Downloaded/", filename_prefix = str(val)+"_" ,
                    max_retries=3)
    count += 1

print("\nAll videos are downloaded.")
