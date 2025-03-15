import yt_dlp
import os
import re
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def validate_youtube_url(url):
    youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu)\.(com|be)/.+')
    return bool(youtube_regex.match(url))

def get_ffmpeg_path():
    if os.name == 'nt':
        return r"C:\Users\antir\Downloads\ffmpeg-7.1.1-full_build\ffmpeg-7.1.1-full_build\bin\ffmpeg.exe"
    else:
        return "ffmpeg"

def download_audio(video_url, output_dir, output_filename, preferred_format='mp3'):
    ffmpeg_path = get_ffmpeg_path()
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, f"{output_filename}.%(ext)s"),
        'ffmpeg_location': ffmpeg_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': preferred_format,
            'preferredquality': '192',
        }],
        'progress_hooks': [lambda d: logging.info(f"Download progress: {d.get('_percent_str', 'N/A')}")],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        logging.info(f"Audio downloaded and converted to {preferred_format.upper()} successfully!")
        return True
    except yt_dlp.utils.DownloadError as e:
        logging.error(f"Download error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    return False

def main():
    video_url = input("Enter the YouTube video URL: ").strip()
    if not validate_youtube_url(video_url):
        print("Invalid YouTube URL. Please try again.")
        return

    output_dir = input("Enter the output directory (leave blank for current directory): ").strip() or "."
    output_filename = input("Enter the output filename (without extension): ").strip() or "downloaded_audio"
    preferred_format = input("Enter the preferred audio format (mp3, wav, etc.): ").strip().lower() or "mp3"

    if download_audio(video_url, output_dir, output_filename, preferred_format):
        print("Download completed successfully!")
    else:
        print("Download failed. Please check the logs for more details.")

if __name__ == "__main__":
    main()