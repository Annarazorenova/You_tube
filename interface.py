import tkinter
from tkinter import *
import pytube 
from  PIL import  ImageTk

def load():
    video_link = Entry.clipboard_get(enter_link)
    yt = pytube.YouTube(video_link)
    streams = yt.streams
    video_best = streams.order_by('resolution').desc().first()
    audio_best = streams.filter(only_audio=True).desc().first()
    print(audio_best)
    print(video_best)
    path = 'C:\Downloads'
    video_best.download(path)
    audio_best.download(path)

def start():
    global enter_link
    global enter_save

    window = Tk()
    window.title('Downloader YouTube 1.0')
    window.geometry('380x380')
    window.columnconfigure(index=0, weight=50)
    window.columnconfigure(index=1, weight=250)

    canvas = tkinter.Canvas(window, height=225, width=225)
    image = Image.open('C:\Python_bot\youtube\py.jpg')
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw',image=photo)
    canvas.grid(row=0,columnspan=2)

    link = Label(window, text='Введите ссылку для скачивания')
    link.grid(row = 1, column = 0, sticky = 'e')
    # link1 = Label(window, text='Сохраненные файлы C:\Downloads')
    # link1.grid(row=2, columnspan=2, sticky = 'ew')
    enter_link = Entry(window) 
    enter_link.grid(row = 1, column = 1, sticky = 'w',pady=10)
    btn = Button(window, text = 'скачать',command = load)
    btn.grid(row = 3, columnspan = 2, pady = 10)
    window.mainloop()


