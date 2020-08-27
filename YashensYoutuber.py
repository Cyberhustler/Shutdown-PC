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
Label(root, text="Welcome to Yashens Youtube\n Downloader Application", font="Consolas 15 bold").pack()
#declaring StringVar type variables
myVar = StringVar()
#Setting the default text to myVar
myVar.set("Enter the link below")
# created the Entry widget to ask the user to enter the URL
Entry(root, textvariable=myVar, width=40).pack(pady=10)
#declaring StringVar type variable
link = StringVar()
#created the entry widget to gain the link needed
Entry(root, textvariable=link,width=40).pack(pady=10)
#created and called the download functon to download the video
Button(root, text="Download video", command=download).pack()
#running the the mainloop
root.mainloop()
