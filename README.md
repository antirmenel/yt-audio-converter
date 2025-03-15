# YouTube Audio Downloader

This Python script allows you to download audio from YouTube videos and convert them to your preferred format (e.g., MP3, WAV).  
 It uses `yt_dlp` for downloading the video and `FFmpeg` for audio extraction and conversion.

## Features

- Download audio from YouTube videos.
- Convert audio to various formats (default: MP3).
- Save audio to a specified directory with a custom filename.
- Display download progress in real-time.
- Support for Windows and other platforms.

## Requirements

- Python 3.x
- `yt_dlp` (YouTube downloader)
- `FFmpeg` (for audio extraction and conversion)

### Install Dependencies

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install `yt_dlp` via pip:
   ```
   pip install yt-dlp
   ```
3. Install FFmpeg:
Windows: Download FFmpeg from FFmpeg official site : 
https://ffmpeg.org/download.html  
macOS/Linux: Install via package manager, e.g.:
```
brew install ffmpeg
   ```

## Usage  
1. Clone this repository:  
```git clone https://github.com/antirmenel/yt-audio-converter.git```    

```cd yt-audio-converter```

2. Run the script:

```
python downloader.py

```
3. Follow the prompts:

Enter the YouTube video URL.  
Choose the output directory (optional).  
Set a filename (optional).  
Choose the audio format (default is MP3).  


## License
This project is licensed under the MIT License.

### Made with ❤️ by Menel



