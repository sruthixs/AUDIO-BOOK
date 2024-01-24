from gtts import gTTS
from io import BytesIO
from pygame import mixer
import pygame
import time
import PyPDF2
from PyPDF2 import PdfReader
import tkinter as tk

def speak(text):
    
    mp3_fp = BytesIO()
    tts = gTTS(text, lang='en')
    tts.write_to_fp(mp3_fp)
    mixer.init()
    sound   = mp3_fp
    sound.seek(0)
    mixer.music.load(sound, "mp3")
    mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def read(book):
    root1=tk.Tk()
    root1.geometry("700x500")
    root1.configure(bg="light green")
    tk.Label(root1, text='Page no:', anchor="center",bg="light green",font=("arial",40),fg="blue").place(x=20,y=170)
    entry=tk.Entry(root1,bg="blue",fg="red")
    entry.place(x=200,y=190)
    def click():
        a=repr(entry.get())
        root1.destroy()
        print(a[1:len(a)-1])
        a=int(a[1:len(a)-1])
        READ(a-1)
    button2 = tk.Button(root1, text='SUBMIT',highlightbackground="blue",width=20,height=2,command=click)
    button2.place(x=280,y=250)
    
    def READ(i):
        pdfFileObj = open(book, 'rb')
        pdfReader = PdfReader(pdfFileObj)
        pageObj = pdfReader.pages[i]
        a=pageObj.extract_text()
        speak(a)
