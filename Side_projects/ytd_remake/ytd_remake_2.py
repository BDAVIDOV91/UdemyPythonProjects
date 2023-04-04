import os
from pytube import YouTube
from moviepy.editor import *

# Ask the user for the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Ask the user for the destination folder to save the files
destination_folder = input("Enter the destination folder: ")
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Download the YouTube video
youtube_video = YouTube(video_url)
video_stream = youtube_video.streams.filter(only_audio=True).first()
video_file_path = video_stream.download(output_path=destination_folder)

# Convert the downloaded video into an mp3 file
video_file = os.path.basename(video_file_path)
audio_file = os.path.join(destination_folder, os.path.splitext(video_file)[0] + ".mp3")
try:
    video_clip = AudioFileClip(video_file_path)
    video_clip.write_audiofile(audio_file)
    video_clip.close()
except Exception as e:
    print("Error converting file: ", e)

# Remove the downloaded video file
os.remove(video_file_path)

# Print debugging information
print("Downloaded file: ", video_file_path)
print("Converted file: ", audio_file)