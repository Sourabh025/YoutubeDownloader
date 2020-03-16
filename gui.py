import tkinter
from tkinter import *
from pytube import YouTube
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO

gui = tkinter.Tk()
gui.geometry("500x400")
gui.title("Youtuber")

def high():
    y = YouTube(e1.get())
    title = y.title
    print(title)
    link = y.thumbnail_url
    # print(y.streams)
    # s=y.streams.all
    vd = YouTube(e1.get()).streams.get_highest_resolution().download()

def low():
    y = YouTube(e1.get())
    title = y.title
    print(title)
    link = y.thumbnail_url
    # print(y.streams)
    # s=y.streams.all
    vd=YouTube(e1.get).streams.get_lowest_resolution().dowmload()

def audio():
    y = YouTube(e1.get())
    title = y.title
    print(title)
    link = y.thumbnail_url
    # print(y.streams)
    # s=y.streams.all
    vd=YouTube(e1.get()).streams.get_audio_only().download()


c=tkinter.Label(gui,text="Deus", bg="black", pady=50)
c.pack(fill="x")

d=tkinter.Label(gui, text="Enter Video link")
d.pack(pady=5)

br=tkinter.Label(gui)
br.pack()
e1=tkinter.Entry(gui, borderwidth=6)
e1.pack(pady=10)
link=e1.get()


def down():

    '''info=tk.Toplevel(gui)
    info.geometry("300x100")
    info.title("INFO")
    y =YouTube(e1.get())
    #t = y.title
    print(y.title)
    #m = Message(gui,text=t)
    #m.pack()
    l=Label(info,text=t)
    l.pack(pady=10)
    #print(y.streams.all)
    #s.download();

    m=Message(text=link)
    response = requests.get(link)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    panel = tk.Label(gui, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    '''
    pass


db = Button(gui, text='Download Audio', command=audio,borderwidth=3)
db.pack(pady=10)
b=Button(gui,text='Download Mp4',command=low,borderwidth=3)
b.pack(pady=10)

b2=Button(gui,text='Download HD',command=high,borderwidth=3)
b2.pack(pady=10)


gui.mainloop()
