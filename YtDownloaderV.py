from pytube import YouTube, Playlist
from progress.bar import Bar
import os
import  sys

def menu():
    opt = input("[A]-Download single Video:\n[B]-Download Playlist videos:\n[C]-Convert To Audio\n[Q]-Exit\n[#]-Choose One: ").upper()
    
    
    if opt == "Q":
        print("Thank you Use my App")
        sys.exit()

    if opt == "A":
        def url():
            url = input("Enter Your Urls:\n")
            path = os.getcwd()
            with Bar('Processing', max=10) as bar:
                for i in range(10):
                      Yt=YouTube(url).streams.filter(progressive=True, file_extension='mp4').desc().first().download()
                      bar.next() 
                bar.finish()
                print(Yt.title)
                print("Done")
                print(f"path of Download file {path}")
        url()
    
    if opt == "B":
        def playlist():
            plist = input("Enter Your Urls:\n")
            path = os.getcwd()
            with Bar('Processing', max=10)  as bar:
                for i in range(10):
                      p= Playlist(plist)
                      for video in p.videos:
                          video.streams.filter(progressive=True, file_extension='mp4').desc().first().download()
                      bar.next() 
                bar.finish()
                print(f'Downloading: {p.title}') 
                print("Done")
                print(f"path of Download file {path}")
        playlist()
        
        
    if opt == "C":
        def audio():
            url = input("Enter Your Urls:\n")
            path = os.getcwd()
            with Bar('Processing', max=5) as bar:
                for i in range(5):
                      Yt=YouTube(url).streams.filter(only_audio=True).desc().first().download()
                      bar.next()
                bar.finish()
                #For convert WEBN to MP3
                base, ext = os.path.splitext(Yt)
                new_file = base + '.mp3'
                os.rename(Yt, new_file)
                print(new_file)
                print("Done!")            
        audio()
        

menu()
