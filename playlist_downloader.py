from pytube import Playlist
from tqdm import tqdm

link = input("Enter YouTube Playlist URL: ")

yt_playlist = Playlist(link)
count = 1
for video in tqdm(yt_playlist.videos, desc="Video downloading: "+ str(count)+"/"+str(len(yt_playlist.videos))):
    video.streams.get_highest_resolution().download("C:\\Users\\vishnu\\Downloads\\bharatanatyam",max_retries=3)
    count += 1
    # print("Video downloading: ", video.title, count, "/", len(yt_playlist.videos))

print("\nAll videos are downloaded.")