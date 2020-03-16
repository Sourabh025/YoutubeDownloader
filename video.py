from pytube import YouTube
import speedtest
import time
from tkinter import *
import tkinter
import sys
import threading

videoList = ["https://www.youtube.com/watch?v=9X71T4RNfaU", 'https://www.youtube.com/watch?v=9X71T4RNfaU'
             ,'https://www.youtube.com/watch?v=9X71T4RNfaU','https://www.youtube.com/watch?v=9X71T4RNfaU'
             ,'https://www.youtube.com/watch?v=9X71T4RNfaU','https://www.youtube.com/watch?v=9X71T4RNfaU',
             "https://www.youtube.com/watch?v=9X71T4RNfaU"]

n = 0



def download(video):
    global error_counter
    try:
        print(video)
        print("Downloading video")
        # vd = YouTube(video).streams.get_highest_resolution().download()  # .download();
        time.sleep(2)
        # raise Exception
        print("video downloaded ")
    except Exception as e:
        global error_counter
        error_counter += 1
        print('Error counter', error_counter)
        if error_counter > 4:
            print("max reties exceed for video", video)
            return

        download(video)


tim1 = time.time()
listlength = len(videoList)
try:
    counter = 1
    error_count = 0;
    for i in range(0, listlength, 3):
        # download( video)
        t1 = threading.Thread(target=download, args=(videoList[i],))
        t1.start()
        try:
            t2 = threading.Thread(target=download, args=(videoList[i + 1],))
            t2.start()
        except Exception as e:
            print("pass")
        try:
            t3 = threading.Thread(target=download, args=(videoList[i + 2],))
            t3.start()
        except IndexError as E:
            print("pass")

        t1.join()
        try:
            t2.join()
            t3.join()
        except:
            pass


        print("counter = ", counter)
        counter += 1

except Exception as error:
    print("Error Caught",error)
tim2 = time.time()
