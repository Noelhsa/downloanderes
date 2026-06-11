import os
import yt_dlp

ruta = "videos"
os.makedirs(ruta, exist_ok=True)

url = input("URL: ")

opciones = {
    "outtmpl": os.path.join(ruta, "%(title)s.%(ext)s"),
    "format": "best"
}

with yt_dlp.YoutubeDL(opciones) as ydl:
    ydl.download([url])