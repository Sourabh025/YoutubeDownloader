from pytube import YouTube
import speedtest
import time
from tkinter import *
import tkinter
import sys
import threading

videoList = [] #"https://www.youtube.com/watch?v=9X71T4RNfaU"]

n = 0
def download(video):
    global error_counter
    try:
        print(video)
        print("Downloading video")
        vd = YouTube(video).streams.get_highest_resolution().download()  # .download();
        time.sleep(2)
        raise Exception
        print("video downloaded hello")
    except Exception as e:
        global error_counter
        error_counter += 1
        print('Error counter', error_counter)
        if error_counter > 4:
            print("max reties exceed for video", video)
            return

        download(video)


tim1 = time.time()

try:
    counter = 1
    error_count = 0;
    for video in videoList:
        # download( video)
        t1 = threading.Thread(target=download, args=(video,))
        t1.start()
        print("counter = ", counter)
        counter += 1

except Exception as error:
    print("Done")
tim2 = time.time()

print("total time", tim2 - tim1)
