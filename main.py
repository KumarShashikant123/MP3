from tkinter import *
from tkinter import filedialog
import pygame
import time
from PIL import Image, ImageDraw
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
import audio_metadata
from PIL import Image, ImageTk
from io import BytesIO
from tinytag import TinyTag
import myfunctions
import wave
from tkinter import font
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import pydub.playback
import numpy as np
import sounddevice as sd
import librosa
import librosa.display
import pyaudio

import matplotlib.pyplot as plt
import IPython.display as ipd
from scipy import signal
from scipy.io import wavfile
import math
import pyaudio as pa



pygame.mixer.init()

window = Tk()
window.title("MP3 PLAYER")
window.geometry("1550x810")



def audio_processing():
    # AUDIO PROCESSING
    #global s_rate
    #file1 = wave.open(output_file)
    global output_file
    global mono
    file1 = wave.open(output_file)
    print(type(file1))

    s_rate = file1.getframerate()
    print(s_rate)
    no_of_channels = file1.getnchannels()
    print(no_of_channels)

    no_of_frames = file1.getnframes()
    print(no_of_frames)

    data1 = file1.readframes(-1)
    # print(len(data1))
    # print(type(data1))

    w_data = np.frombuffer(data1, np.int16)
    # print(w_data)
    # print(type(w_data))
    # print(len(w_data))
    # print(w_data)

    mono = []
    print("BEFORE PLAYING SIZE OF MONO")
    print(len(mono))
    if(len(mono)):
        mono.clear()

    m1 = 0
    while m1 <= len(w_data) - 1:
        mono.append(w_data[m1])
        m1 = m1 + 2
    print("AFTER PLAYING MONO SIZE")
    print(len(mono))
    w_data.shape = -1, 2

    global songdur1


    s_rate = file1.getframerate()
    CHUNK = 1024 * 2
    CHANNELS = 1
    FORMAT = pa.paInt16

    RATE = s_rate

    frame = []
    fr = 0


    print("FRAMES")
    print(int(RATE / CHUNK * songdur1))
    #print(type(data1))
    #print(len(data1))
    # print(data1)

    for fr in range(fr, int(RATE / CHUNK)):
        pass

    # for fr in range(fr,)
    play = pa.PyAudio()
    stream_play = play.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            output=True)

    fig, ax = plt.subplots()
    x = np.arange(0, CHUNK, 1)
    line, = ax.plot(x, np.random.rand(CHUNK), 'r')
    ax.set_ylim(-32770, 32770)
    ax.ser_xlim = (0, CHUNK)

    fig.show()

    print("playing")

    isa = 0
    jsa = 0
    ksa = 0
    data_sa = []
    no_of_frames = file1.getnframes()
    print(no_of_frames)
    print(s_rate)
    #mono = []
    print(len(mono))
    print(CHUNK)
    print(int(len(mono) / CHUNK))

    for isa in range(isa, int(len(mono) / CHUNK)):
        ksa = 0
        for ksa in range(ksa, CHUNK):
            data_sa.append(mono[jsa])
            jsa = jsa + 1

        # stream_play.write(data_sa)
        # wav_data = np.frombuffer(data_sa, 'int16')
        # print(wav_data)

        # print(struct.calcsize(str(CHUNK))+'h');

        # dataInt = struct.unpack(str(CHUNK) + 'h',wav_data)
        # print(len(dataInt))
        # print(data_sa)
        # print(len(data_sa))
        line.set_ydata(data_sa)
        fig.canvas.draw()
        fig.canvas.flush_events()

        # print(data_sa)
        data_sa.clear()

    stream_play.stop_stream()
    stream_play.close()
    play.terminate()

def cover_pic():
    pass
    """
    global song
    metadata = audio_metadata.load(song)
    # print(metadata)

    # get the picture data for the first picture in metadata pictures
    pic = metadata.pictures[0].data

    # open stream (similar to file) in binary mode
    stream = BytesIO(pic)

    # display artwork on tkinter
    canvas = Canvas(f2, width=230, height=230)
    canvas.pack(pady=30, side=BOTTOM)
    img1 = ImageTk.PhotoImage(Image.open(stream))

    canvas.create_image(0, 0, image=img1)

    """

# LEFT FRAME ; PLAYLISTS,ARTISTS,ALBUMS
def playlistfun():
    global plist_arti_alb_box
    if plist_arti_alb_box.size() >= 0:
        plist_arti_alb_box.delete(0, END)
    """
    global songbox
    global size_songbox
    n0 = size_songbox
    global l_playlist

    if songbox.size() >= 0:
        songbox.delete(0, END)
    ipl=0
    for song_pl in l_playlist:
        songbox.insert(END, song_pl)

    """










# FOR ARTIST
def artistfun():
    global plist_arti_alb_box
    if plist_arti_alb_box.size() >= 0:
        plist_arti_alb_box.delete(0, END)

    global size_songbox
    n = size_songbox
    l = []
    l1 = []
    i = 0
    for i in range(i, n):
        s = songbox.get(i)
        s = f'C:/Users/shash/PycharmProjects/MP3/audio/{s}.mp3'
        l.append(s)
    # print(len(l))

    i = 0
    for i in range(i, len(l)):
        audio = TinyTag.get(l[i])
        # print(type(audio))

        a = audio.artist
        l1.append(a)
    # print(l1)
    l3 = myfunctions.endcomma_fromlist(l1)
    # print(l3)

    artists = []

    for i in l3:
        artists.append(i.strip())
    artists = list(set(artists))

    artists = (sorted(artists))
    # print(artists)


    for i in artists:
        # print(i)
        i1 = 1
        plist_arti_alb_box.insert(i1, i)
        i1 = i1 + 1


# FOR ALBUM

def albumfun():
    # CLEARING LISTBOX IF EXISTED
    global plist_arti_alb_box
    if plist_arti_alb_box.size() >= 0:
        plist_arti_alb_box.delete(0, END)

    global songbox
    n = songbox.size()
    l = []
    i = 0
    for i in range(i, n):
        s = songbox.get(i)

        s = f'C:/Users/shash/PycharmProjects/MP3/audio/{s}.mp3'
        album1 = TinyTag.get(s)
        print(album1)
        album1 = album1.album
        l.append(album1)
    # print(album1)




# PLAY FUCTION

def play():
    global song
    song = songbox.get(ACTIVE)

    song = f'C:/Users/shash/PycharmProjects/MP3/audio/{song}.mp3'
    pygame.mixer.music.set_volume(0.5)


    # print(song)

    loop = AudioSegment.from_mp3(song)

    global output_file
    output_file = "result.wav"
    loop.export(output_file, format="wav")


    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songstatus()



    metadata = audio_metadata.load(song)
    # print(metadata)

    # get the picture data for the first picture in metadata pictures
    pic = metadata.pictures[0].data

    # open stream (similar to file) in binary mode
    stream = BytesIO(pic)

    # display artwork on tkinter
    canvas = Canvas(f2, width=230, height=230)
    canvas.pack(pady=30, side=BOTTOM)
    img1 = ImageTk.PhotoImage(Image.open(stream))

    canvas.create_image(0, 0, image=img1)

    # META_DATA FOR COVER IMAGE
    """
    metadata = audio_metadata.load(song)
    # print(metadata)

    # get the picture data for the first picture in metadata pictures
    pic = metadata.pictures[0].data

    # open stream (similar to file) in binary mode
    stream = BytesIO(pic)

    # display artwork on tkinter
    canvas = Canvas(f2, width=230, height=230)
    canvas.pack(pady=30,side=BOTTOM)
    img1 = ImageTk.PhotoImage(Image.open(stream))

    canvas.create_image(0, 0, image=img1)
    """
    audio_processing()


    #songstatus()

    # audio_modulation()


# CHECK

def check1():
    c = songbox.get(2)


# print(c)


# SONG STATUS
def songstatus():
    # SONG CURRENT TIME
    global current_time
    current_time = pygame.mixer.music.get_pos() / 1000

    # SHOW SLIDER TIME TEMPORARY
    # temp_slider.config(text=f'Slider:{int(slider.get())} ,Current_time: {int(current_time)}')

    new_currrent_time = time.strftime('%M:%S', time.gmtime(current_time))
    song_status.config(text=new_currrent_time)

    # SONG TOTAL LENGTH
    # current_song=songbox.curselection()
    song = songbox.get(ACTIVE)
    song = f'C:/Users/shash/PycharmProjects/MP3/audio/{song}.mp3'
    song1 = MP3(song)
    global songdur1
    songdur1 = song1.info.length
    song_duration = time.strftime('%M:%S', time.gmtime(songdur1))

    song_status.config(text=f'{new_currrent_time}of{song_duration}')

    # UPDATE SLIDER TO GET CURRENT TIME
    slider.config(value=int(current_time))

    # UPDATE SLIDER LENGTH
    slider_lenght = int(songdur1)
    # current_time +=1
    slider.config(to=slider_lenght, value=int(current_time))

    # CHECK
    # SHOW SLIDER TIME TEMPORARY
    #temp_slider.config(text=f'Slider:{int(slider.get())} ,Current_time: {int(current_time)}')

    current_time = slider.get()
    slider.config(value=int(current_time))

    # UPADTE TIME
    song_status.after(1000, songstatus)



# SLIDER
def song_slider(x):
    # temp_slider.config(text=f'{int(slider.get())}of{int(songdur1)}')
    # print('',songdur1)
    song = songbox.get(ACTIVE)

    song = f'C:/Users/shash/PycharmProjects/MP3/audio/{song}.mp3'
    # check1()

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(slider.get()))


# PAUSE,RESUME

var1 = False


def pause():
    global var1

    if var1 == False:
        pygame.mixer.music.pause()
        global resume_img
        b6l1.config(image=resume_img)
        var1 = TRUE
    else:

        pygame.mixer.music.unpause()
        global pause_img
        b6l1.config(image=pause_img)
        var1 = False


# STOP
def stop():
    pygame.mixer.music.stop()
    songbox.selection_clear(ACTIVE)
    pygame.mixer.music.unload()

    # CLEAR STATUS BAR
    song_status.config(text='')


# NEXT SONG
def nextsong():
    n1 = songbox.curselection()

    # CHECK
    # print(type(songbox))
    # print(songbox.get(n1))

    n1 = n1[0] + 1

    # print(songbox.get(n1))
    song = songbox.get(n1)
    # print(songbox.size())

    song = f'C:/Users/shash/PycharmProjects/MP3/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songbox.selection_clear(0, END)

    songbox.activate(n1)

    songbox.selection_set(n1, last=None)

    # SLIDER HELP
    # slider.config(value=0)


# PREVIOUS SONG
def previousong():
    next_one = songbox.curselection()

    next_one = next_one[0] - 1

    song = songbox.get(next_one)
    song = f'C:/Users/shash/PycharmProjects/MP3/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songbox.selection_clear(0, END)

    songbox.activate(next_one)

    songbox.selection_set(next_one, last=None)

    # SLIDER HELP


# MENUBAR FUNCTION
# ADD ONE SONG
def onesong():
    song = filedialog.askopenfilename(initialdir='audio/', title="chhose a song", filetypes=(("mp3 Files", "*.mp3"),))
    song = song.replace("C:/Users/shash/PycharmProjects/MP3/audio/", "")
    song = song.replace(".mp3", "")
    global l_playlist
    l_playlist=[]
    l_playlist.append(song)

    songbox.insert(END, song)
    global size_songbox
    size_songbox = songbox.size()
    print(size_songbox)
def manysong():

    songs = filedialog.askopenfilenames(initialdir='audio/', title="chhose a song", filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        song = song.replace("C:/Users/shash/PycharmProjects/MP3/audio/", "")
        song = song.replace(".mp3", "")
        global l_playlist

        l_playlist.append(song)

        songbox.insert(END, song)
        global size_songbox
        size_songbox = songbox.size()
        # print(size_songbox)


# DELETE
def onesong1():
    songbox.delete(ANCHOR)
    pygame.mixer.music.stop()
    global size_songbox

    size_songbox = songbox.size()


def manysong1():
    songbox.delete(0, END)
    stop()
    global size_songbox

    size_songbox = songbox.size()


def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())


# MENUBAR
mymenubar = Menu()
menu1 = Menu(mymenubar, tearoff=0)
menu1.add_command(label="ONE SONG", command=onesong)
menu1.add_command(label="MANY SONG", command=manysong)
mymenubar.add_cascade(label="ADD SONG", menu=menu1)

window.config(menu=mymenubar)
menu2 = Menu(mymenubar, tearoff=0)
menu2.add_command(label="ONE SONG", command=onesong1)
menu2.add_command(label="ALL SONG", command=manysong1)
mymenubar.add_cascade(label="REMOVE SONG", menu=menu2)

# PLAYLISTS, ARTISTS, ALBUMS
f1 = Frame(window, bg="grey", width=50)
f1.pack(side=LEFT, fill=Y, pady=128, expand=YES)

b1f1 = Button(f1, text="PLAYLIST", width=30, command=playlistfun)
b1f1.pack()
b2f1 = Button(f1, text="ARTISTS", width=30, command=artistfun)
b2f1.pack()
b3f1 = Button(f1, text="ALBUMS", width=30, command=albumfun)
b3f1.pack()

# PLAYLIST ,ARTISTS, ALBUMS

lab2 = Label(f1, width=30, height=31, bg="skyblue4")
lab2.place(x=2, y=73)
global plist_arti_alb_box
plist_arti_alb_box = Listbox(f1, bg="skyblue4", width=34, height=30)
plist_arti_alb_box.pack()

# MAIN SCREEN
f2 = Frame(window, bg="black", width=100, height=100)
f2.pack(side=LEFT, fill=Y, pady=128, expand=YES)
# l3f2=Label(f2,width=900,height=465)
# l3f2.pack()
global l1f2
l1f2 = Label(f2, bg="blue", width=120, height=2)
l1f2.pack(side=BOTTOM)

specto_img=ImageTk.PhotoImage(Image.open("specto_img.png"))
spect_button=Button(l1f2,width=50,image=specto_img)
spect_button.pack(side=LEFT,padx=20)

previous_img = ImageTk.PhotoImage(Image.open("previous.png"))


# Create a Label Widget to display the text or Image

b1l1 = Button(l1f2, width=80, command=previousong,image=previous_img,height=25)
#b1l1 = Button(l1f2, text="PREVIOUS", width=15, command=previousong)
b1l1.pack(side=LEFT, padx=20)

next_img = ImageTk.PhotoImage(Image.open("next.png"))
b4l1 = Button(l1f2, width=80, height=25,command=nextsong,image=next_img)
b4l1.pack(padx=10, side=LEFT)
play_img = ImageTk.PhotoImage(Image.open("play.ico"))
b2l1 = Button(l1f2, width=80,height=25, fg="green", command=play,image=play_img)
b2l1.pack(padx=10, side=LEFT)
global pause_img
pause_img = ImageTk.PhotoImage(Image.open("pause.png"))
global resume_img
resume_img=ImageTk.PhotoImage(Image.open("resume.png"))

global b6l1
b6l1 = Button(l1f2, width=80,height=25, command=pause,image=pause_img)
b6l1.pack(padx=10, side=LEFT)

stop_img = ImageTk.PhotoImage(Image.open("stop.png"))
b5l1 = Button(l1f2, width=80,height=25, command=stop,image=stop_img)
b5l1.pack(side=LEFT,padx=10)
# VOLUME SLIDER
volume_img = ImageTk.PhotoImage(Image.open("volume.png"))
l2f2 = Label(l1f2, width=70,height=25,image=volume_img)
l2f2.pack(side=LEFT,padx=5)
l3f2 = Label(l1f2, height=2)
l3f2.pack()

volume_slider = ttk.Scale(l3f2, from_=0, to=1, orient=HORIZONTAL, value=0, command=volume, length=100)
volume_slider.pack(padx=10)

# SONG DURATION
song_status = Label(f2, anchor=E)
song_status.pack(side=BOTTOM, fill=X)
# SLIDER
slider = ttk.Scale(song_status, from_=0, to=100, value=0, command=song_slider, length=700)
slider.pack()

# TEMPORARY SLIDER HELP
#temp_slider = Label(song_status)
#temp_slider.pack()

# SONGS LIST
f3 = Frame(window, bg="grey")
f3.pack(side=LEFT, fill=BOTH, pady=128, expand=YES)
l1f3 = Label(f3, text="SONGS", bg="orange", width=90)
l1f3.pack()
songbox = Listbox(f3, bg="skyblue4", width=90, height=100)
songbox.pack()

# fl2=Label(f1,image=photo)
# fl2.pack()



window.mainloop()

