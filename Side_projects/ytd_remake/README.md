# YouTube Downloader

This project downloads YouTube videos, converts them to MP3 format, and saves them in the `music` directory. The original video file is deleted after conversion.

## Setup

1. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Ensure `ffmpeg` is installed on your system**:
    ```sh
    sudo apt-get install ffmpeg
    ```

4. **Place your YouTube cookies file in the project root directory and name it `cookies.txt`**.

## Usage

1. **Activate the virtual environment** (if not already activated):
    ```sh
    source venv/bin/activate
    ```

2. **Run the script**:
    ```sh
    python src/ytd.py
    ```

3. **Enter the YouTube video URL when prompted**.

## Project Structure
