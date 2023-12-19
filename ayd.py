from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import os
import requests
from tkinter import ttk

def select_video_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def update_progress(downloaded, total_size):
    percentage = int((downloaded / total_size) * 100)
    progress_text.set(f"{percentage}% téléchargé")
    progress_bar['value'] = downloaded

def download_video():
    get_link = link_field.get()
    
    if not ('youtube.com' in get_link or 'youtu.be' in get_link):
        link_field.delete(0, END)
        link_field.insert(0, "Le lien n'est pas valide. Veuillez saisir un lien YouTube correct.")
        return
    
    user_path = path_label.cget("text")
    screen.title('Téléchargement en cours...')
    
    resolution = resolution_var.get()
    yt = YouTube(get_link)
    video = yt.streams.filter(res=resolution).first()
    
    if video:
        response = requests.get(video.url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        
        progress_text.set("0% téléchargé")
        progress_bar['maximum'] = total_size
        
        downloaded = 0
        with open(os.path.join(user_path, os.path.basename(yt.title) + '.mp4'), 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    update_progress(downloaded, total_size)
                    screen.update_idletasks()
        
        screen.title('Téléchargement terminé ! Télécharger une autre vidéo...')
    else:
        screen.title('La résolution sélectionnée n\'est pas disponible pour cette vidéo.')

screen = Tk()
title = screen.title('AY Downloader')
canvas = Canvas(screen, width=500, height=800)
canvas.pack()

file_path = os.path.join(os.path.dirname(__file__), 'Aj.png')
logo_img = PhotoImage(file=file_path)
logo_img = logo_img.subsample(2, 2)
background = canvas.create_image(250, 400, anchor=CENTER, image=logo_img)

link_field = Entry(screen, width=40, font=('Arial', 15))
link_label = Label(screen, text="Entrez le lien de la vidéo ci-dessous : ", font=('Arial', 15))

path_label = Label(screen, text="Sélectionnez où vous souhaitez enregistrer votre vidéo", font=('Arial', 15))
select_btn = Button(screen, text="Sélectionner le chemin", bg='crimson', padx='22', pady='5', font=('Arial', 15), fg='#fff', command=select_video_path)

canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

resolutions = ['360p', '480p', '720p', '1080p']
resolution_var = StringVar()
resolution_var.set(resolutions[0])
resolution_dropdown = OptionMenu(screen, resolution_var, *resolutions)
resolution_label = Label(screen, text="Sélectionnez la résolution : ", pady='10', font=('Arial', 15))

canvas.create_window(250, 390, window=resolution_label)
canvas.create_window(250, 440, window=resolution_dropdown)

progress_text = StringVar()
progress_text.set("0% téléchargé")
progress_bar = ttk.Progressbar(screen, orient=HORIZONTAL, length=300, mode='determinate')
canvas.create_window(250, 600, window=progress_bar)

download_btn = Button(screen, text="Télécharger la vidéo", bg='red', padx='22', pady='5', font=('Arial', 15), fg='#fff', command=download_video)
canvas.create_window(250, 490, window=download_btn)

screen.mainloop()
