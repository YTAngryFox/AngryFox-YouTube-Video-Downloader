from pytube import YouTube
import sys
import os
from pystyle import Colorate, Colors

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("")

print(Colorate.Horizontal(Colors.purple_to_red, "                           █████╗ ███╗   ██╗ ██████╗ ██████╗ ██╗   ██╗███████╗ ██████╗ ██╗  ██╗"))
print(Colorate.Horizontal(Colors.purple_to_red, "                          ██╔══██╗████╗  ██║██╔════╝ ██╔══██╗╚██╗ ██╔╝██╔════╝██╔═══██╗╚██╗██╔╝"))
print(Colorate.Horizontal(Colors.purple_to_red, "                          ███████║██╔██╗ ██║██║  ███╗██████╔╝ ╚████╔╝ █████╗  ██║   ██║ ╚███╔╝ "))
print(Colorate.Horizontal(Colors.purple_to_red, "                          ██╔══██║██║╚██╗██║██║   ██║██╔══██╗  ╚██╔╝  ██╔══╝  ██║   ██║ ██╔██╗ "))
print(Colorate.Horizontal(Colors.purple_to_red, "                          ██║  ██║██║ ╚████║╚██████╔╝██║  ██║   ██║   ██║     ╚██████╔╝██╔╝ ██╗"))
print(Colorate.Horizontal(Colors.purple_to_red, "                          ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═╝"))

print(Colorate.Diagonal(Colors.purple_to_red, "                                                   Made by AngryFoxYT"))
print(Colorate.Diagonal(Colors.purple_to_red, "                                                YouTube Video Downloader"))

print("")

print(Colorate.Diagonal(Colors.purple_to_red, "Enter the youtube link"))
link = input("")

yt = YouTube(link)

yt.bypass_age_gate()

video = yt.streams.get_highest_resolution()

clear()

print("")

print(Colorate.Horizontal(Colors.purple_to_red, "                           █████╗ ███╗   ██╗ ██████╗ ██████╗ ██╗   ██╗███████╗ ██████╗ ██╗  ██╗"))
print(Colorate.Horizontal(Colors.purple_to_red, "                          ██╔══██╗████╗  ██║██╔════╝ ██╔══██╗╚██╗ ██╔╝██╔════╝██╔═══██╗╚██╗██╔╝"))
print(Colorate.Horizontal(Colors.purple_to_red, "                          ███████║██╔██╗ ██║██║  ███╗██████╔╝ ╚████╔╝ █████╗  ██║   ██║ ╚███╔╝ "))
print(Colorate.Horizontal(Colors.purple_to_red, "                          ██╔══██║██║╚██╗██║██║   ██║██╔══██╗  ╚██╔╝  ██╔══╝  ██║   ██║ ██╔██╗ "))
print(Colorate.Horizontal(Colors.purple_to_red, "                          ██║  ██║██║ ╚████║╚██████╔╝██║  ██║   ██║   ██║     ╚██████╔╝██╔╝ ██╗"))
print(Colorate.Horizontal(Colors.purple_to_red, "                          ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═╝"))

print(Colorate.Diagonal(Colors.purple_to_red, "                                                   Made by AngryFoxYT"))
print(Colorate.Diagonal(Colors.purple_to_red, "                                                YouTube Video Downloader"))

print("")

print(Colorate.Diagonal(Colors.purple_to_red, "Title: " + yt.title))
print(Colorate.Diagonal(Colors.purple_to_red, "Author: " + yt.author))

print("")

print(Colorate.Diagonal(Colors.purple_to_red, "Is this the video you want to install? (y/n)"))
yn = input("")

print("")

if yn == "y":
   os.chdir(".")
   print(Colorate.Diagonal(Colors.purple_to_red, "Done!"))
   video.download()
   sys.exit()
elif yn == "n":
   sys.exit()
else:
   print(Colorate.Diagonal(Colors.purple_to_red, "Invalid Option."))
