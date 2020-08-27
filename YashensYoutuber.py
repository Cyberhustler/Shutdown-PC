#importing tkinter
from tkinter import *
#importing Youtube module
from pytube import YouTube
#initializing tkinter
root = Tk()
#setting the geometry of the GUI
root.geometry('400x350')
#setting the title of the GuI
root.title("Yashen Naidus YouTube Downloader")
#defining download function
def download():
    # using try and except to execute program without errors
    try:
        myVar.set("Downloading...")
        root.update()
        YouTube(link.get()).stream.first().download()y
        link.set("Video downloaded successfully")
    except Exception as e:
        myVar.set("Mistake has been made")
        root.update()
        link.set("Ënter the Correct link")
 
#create the welcome label to welcome the user
Label(root)
