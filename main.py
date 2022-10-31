from pytube import YouTube
import sys
import colorama
import os

colorama.init()

print("")

print(colorama.Fore.LIGHTCYAN_EX + """
\ \   /__ __|      __ \                           |                    |
 \   /    |        |   |  _ \  \ \  \   /  __ \   |   _ \    _` |   _` |   _ \   __|
    |     |        |   | (   |  \ \  \ /   |   |  |  (   |  (   |  (   |   __/  |
   _|    _|       ____/ \___/    \_/\_/   _|  _| _| \___/  \__._| \__._| \___| _|

""")

print(colorama.Fore.RED + "Made by AngryFoxYT")

print(colorama.Fore.WHITE + "")

link = input("Enter the youtube video link: ")

yt = YouTube(link)

yt.bypass_age_gate()

video = yt.streams.get_highest_resolution()

print("")

print("Title: " + yt.title)
print("Author: " + yt.author)

print("")

yn = input("Is this the video you want to install? (y/n): ")

print("")

if yn == "y":
   os.chdir(".")
   print("Done...")
   video.download()
elif yn == "n":
   sys.exit()
else:
   print("Invalid option.")
