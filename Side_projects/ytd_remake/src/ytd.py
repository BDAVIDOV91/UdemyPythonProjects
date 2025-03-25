import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment


def download_video(url, destination_folder):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(destination_folder, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "cookiefile": "cookies.txt",  # Path to your cookies file
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict.get("title", None)
        video_file_path = os.path.join(destination_folder, f"{video_title}.mp3")
    return video_file_path


def main():
    url = input("Enter the YouTube video URL: ")
    destination_folder = os.path.join(os.path.dirname(__file__), "..", "music")

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    print("Downloading video and converting to MP3...")
    try:
        mp3_file_path = download_video(url, destination_folder)
        print(f"Downloaded and converted to MP3: {mp3_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
