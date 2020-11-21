from pytube import YouTube
from pytube.cli import on_progress
from colorama import Fore, Back, Style
import os
import time

BOLD = '\033[1m'


def downloader():
    try:
        title = "Youtube Downloader"
        title_new = title.center(158, '-')
        print(Fore.RED + BOLD + title_new + Fore.RED)
        url = input(Fore.CYAN + "Paste Youtube Link: " + Fore.CYAN)
        format = input(Style.RESET_ALL + "\nChoose File Format(video or audio): ")
        if format == "video":
            print(Fore.GREEN + BOLD + "Selected Format => video" + Fore.GREEN)
            yt = YouTube(url, on_progress_callback=on_progress)
            yt.streams\
                .filter(progressive=True, file_extension="mp4")\
                .get_highest_resolution()\
                .download(os.path.curdir + "/Downloads/Video", filename_prefix="video_")
            print("DONE...")
        elif format == "audio":
            print(Fore.GREEN + "Selected Format => audio" + Fore.GREEN)
            vt = YouTube(url, on_progress_callback=on_progress)
            vt.streams.get_by_itag(140)\
                .download(os.path.curdir + "/Downloads/Audio", filename_prefix="audio_")
            print("DONE...")
        else:
            print(Fore.RED + BOLD + "Unknown or Invalid Format!!!" + Fore.RED)
            time.sleep(3)
            exit
    except Exception as err:
        print(err)


downloader()
