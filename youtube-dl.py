from __future__ import unicode_literals
import youtube_dl
import shutil
from pathlib import Path
import os
import platform

def get_download_folder ():
    os = platform.system()

    if os == 'Linux' :
        return str(Path.home() / "Downloads")
    else :
        return f'C:\\Users\\{os.getlogin()}\\Downloads\\'

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def select_format(url) :
    format = input("Select a format: ")
    download_mp4(url, format)

def download_mp4(url, format = False) :

    ydl_opts = {
        'format': 'bestaudio/best' if not format else format,
        'outtmpl': '{}/%(title)s.%(ext)s'.format(get_download_folder()),
        'listformats': True if not format else False,
        'progress_hooks': [my_hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        if format :
            ydl.download([url])
            start_system()
        else :
            ydl.download([url])
            select_format(url)

def download_mp3(url) :

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '{}/%(title)s.%(ext)s'.format(get_download_folder()),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'progress_hooks': [my_hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        start_system()

def start_system() :
    print("""
1) Audio
2) Video """)
    option = input("Select an option: ")

    if option != "1" and option != "2" :
        print("Invalid option")
        start_system()

    url = input("Enter the url of the video: ")

    if option == "1" : 
        download_mp3(url)
    else :
        download_mp4(url)

print("YouTube Downloader by MetaRiaqer - V1.0")
start_system()
