from pytube import YouTube
from pytube import Playlist

def completed():
    print("download")

vidorpla=input("this is a video or playlist:")

num=1
if(vidorpla=="video"):
    link=input("enter the video link :")
    name=input("enter the video name :")
    video=YouTube(link)
    video.streams.get_highest_resolution().download(output_path="C:/Users/azer/Videos/downloads",filename=f"{name}.mp4")
    video.register_on_complete_callback(completed())
elif(vidorpla=="playlist"):
    links=input("enter the playlist link :")
    playlistname=input("enter the playlist name :")
    playlist=Playlist(links)
    for video in playlist.videos:
        video.streams.get_highest_resolution().download(output_path="C:/Users/azer/Videos/downloads",filename=f"{playlistname}+{num}.mp4")
        video.register_on_complete_callback(completed())
        num+=1
