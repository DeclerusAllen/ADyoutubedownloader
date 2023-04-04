from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import shutil


#Fonction
def select_video_path():
    #selectionner une direction
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_video():
    #avoir user path
    get_link = link_field.get()
    # if the link isn't correct
    if 'youtube.com' not in get_link:
        link_field.delete(0, END) #delete the link
        link_field.insert(0, "the link is invalid, please retype the link") # print the error
        return
    


    #avoir selected path
    user_path = path_label.cget("text")
    screen.title('video is Downloading...')
    #get selected resolution
    resolution = resolution_var.get()
    #Download Video
    yt = YouTube(get_link)
    video = yt.streams.filter(res=resolution).first()
    mp4_video = video.download()
    
    #put the video in the file
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another Video...')

screen = Tk()
title = screen.title('A_YT Downloader')
canvas = Canvas(screen, width=500, height=800)
canvas.pack()

#image logo
logo_img = PhotoImage(file='A.png')
#resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)

#enter the link bouton
link_field = Entry(screen, width=40, font=('Arial', 15) )
link_label = Label(screen, text="Enter Video Link Below: ", font=('Arial', 15))


#Select Path for saving the file
path_label = Label(screen, text="Select where you want to add your video", font=('Arial', 15))
select_btn =  Button(screen, text="Select Path", bg='crimson', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=select_video_path)
#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Add widgets to window 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#Resolution dropdown menu
resolutions = ['360p', '480p', '720p', '1080p']
resolution_var = StringVar()
resolution_var.set(resolutions[0])
resolution_dropdown = OptionMenu(screen, resolution_var, *resolutions)
resolution_label = Label(screen, text="Select Resolution: ", font=('Arial', 15))
#Add to window
canvas.create_window(250, 370, window=resolution_label)
canvas.create_window(250, 420, window=resolution_dropdown)

#Download btns
download_btn = Button(screen, text="Download Video",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_video)
#add to canvas
canvas.create_window(250, 490, window=download_btn)


screen.mainloop()
