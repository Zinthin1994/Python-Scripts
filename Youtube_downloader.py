import os
#Update Packages to the newest version
os.system("pip install --upgrade yt-dlp")

#Print Download Directory
print("\033[91m" + "Downloading to the following directory:" + "\033[0m" + " " + os.getcwd())

#Ask for Playlist or Video you would like to download
PlaylistOrVideo = input("\033[91m" + "Enter video or Playlist: " + "\033[0m")
VideoOrAudioInput = input("\033[91m" + "v for Video(mp4) or a for audio(mp3): " + "\033[0m")

if VideoOrAudioInput == 'v':
    VideoOrAudio = "--remux-video mp4"
elif VideoOrAudioInput == 'a':
    VideoOrAudio = "-x --audio-format mp3"
else:
    print("You didn't select a or v --Programing is going to error out")

#Run download process
os.system("yt-dlp" + " " + VideoOrAudio + " " + PlaylistOrVideo)

#Example Video
#https://www.youtube.com/watch?v=-MFx1DLLWo4https://www.youtube.com/watch?v=eFBYfZ9FEC0