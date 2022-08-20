from sys import meta_path
from pytube import YouTube
import moviepy.editor as mp
import re
import os
#import panda as pd
#import win32com.client as win32
def main():
    link = input("Digite o link do video que deseja baixar:\n")
    path = "D:\DOWNLOADs"
    yt = YouTube(link)

    print("Baixando...")
    ys = yt.streams.filter(only_audio=True).first().download(path)

    print("Download completo")
    print("Convertendo arquivo....")

    mp3ormp4 = int(input("Digite\n1 para download mp3\n2 para download mp4\n"))

    if mp3ormp4 != 1 or mp3ormp4 != 2:
        print("\nOpção invalida, tente novamente\n")
        mp3ormp4 = int(input("Digite\n1 para download mp3\n2 para download mp4\n"))
        
    if mp3ormp4 == 1:
        for file in os.listdir(path):
            if re.search('mp4',file):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
    else:
        for file in os.listdir(path):
            if re.search('mp4',file):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp3_path)    
    print("Oks!!!")
main()