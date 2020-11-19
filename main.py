from pytube import YouTube
from pytube.cli import on_progress
from colorama import Fore, Back, Style
import os
import time

BOLD = '\033[1m'


def on_entry():
    try:
        title = "Youtube Downloader"
        title_new = title.center(158, '-')
        print(Fore.RED + BOLD + title_new + Fore.RED)
        url = input(Fore.GREEN + "Paste Youtube Link: " + Fore.GREEN)
        format = input(Style.RESET_ALL + "\nChoose File Format(video or audio): ")
        if format == "video":
            print("Selected Format => video")
            yt = YouTube(url, on_progress_callback=on_progress)
            yt.streams\
            .filter(progressive=True, file_extension="mp4")\
            .get_highest_resolution()\
            .download(os.path.curdir + "/Downloads/Video", filename_prefix="video_")
            print("DONE...")
        elif format == "audio":
            print("Selected Format => audio")
            vt = YouTube(url, on_progress_callback=on_progress)
            vt.streams.get_by_itag(140)\
            .download(os.path.curdir + "/Downloads/Audio" , filename_prefix="audio_")
            print("DONE...")
        else:
            print(Fore.RED + BOLD + "Unknown or Invalid Format!!!" + Fore.RED)
            time.sleep(3)
            exit
    except Exception as err:
        print(err)


on_entry()
