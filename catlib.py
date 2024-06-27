import os
import json
import time
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

# ________  ________  _________  ___       ___  ________     
#|\   ____\|\   __  \|\___   ___\\  \     |\  \|\   __  \    
#\ \  \___|\ \  \|\  \|___ \  \_\ \  \    \ \  \ \  \|\ /_   
# \ \  \    \ \   __  \   \ \  \ \ \  \    \ \  \ \   __  \  
#  \ \  \____\ \  \ \  \   \ \  \ \ \  \____\ \  \ \  \|\  \ 
#   \ \_______\ \__\ \__\   \ \__\ \ \_______\ \__\ \_______\
#    \|_______|\|__|\|__|    \|__|  \|_______|\|__|\|_______|

def print_credits():
    credits = r"""
     ______  __                       __                                         ___                                                          
    /\__  _\/\ \                     /\ \                                      /'___\                                  __                     
    \/_/\ \/\ \ \___      __      ___\ \ \/'\       __  __    ___   __  __    /\ \__/  ___   _ __       __  __    ____/\_\    ___      __     
       \ \ \ \ \  _ `\  /'__`\  /' _ `\ \ , <      /\ \/\ \  / __`\/\ \/\ \   \ \ ,__\/ __`\/\`'__\    /\ \/\ \  /',__\/\ \ /' _ `\  /'_ `\   
        \ \ \ \ \ \ \ \/\ \L\.\_/\ \/\ \ \ \\`\    \ \ \_\ \/\ \L\ \ \ \_\ \   \ \ \_/\ \L\ \ \ \/     \ \ \_\ \/\__, `\ \ \/\ \/\ \/\ \L\ \  
         \ \_\ \ \_\ \_\ \__/.\_\ \_\ \_\ \_\ \_\   \/`____ \ \____/\ \____/    \ \_\\ \____/\ \_\      \ \____/\/\____/\ \_\ \_\ \_\ \____ \ 
          \/_/  \/_/\/_/\/__/\/_/\/_/\/_/\/_/\/_/    `/___/> \/___/  \/___/      \/_/ \/___/  \/_/       \/___/  \/___/  \/_/\/_/\/_/\/___L\ \
                                                        /\___/                                                                         /\____/
                                                        \/__/                                                                          \_/__/

     ________  ________  _________  ___       ___  ________          ___  ___  ___     
    |\   ____\|\   __  \|\___   ___\\  \     |\  \|\   __  \        |\  \|\  \|\  \    
    \ \  \___|\ \  \|\  \|___ \  \_\ \  \    \ \  \ \  \|\ /_       \ \  \\\  \ \  \   
     \ \  \    \ \   __  \   \ \  \ \ \  \    \ \  \ \   __  \       \ \  \\\  \ \  \  
      \ \  \____\ \  \ \  \   \ \  \ \ \  \____\ \  \ \  \|\  \       \ \  \\\  \ \  \ 
       \ \_______\ \__\ \__\   \ \__\ \ \_______\ \__\ \_______\       \ \_______\ \__\
        \|_______|\|__|\|__|    \|__|  \|_______|\|__|\|_______|        \|_______|\|__|

     _____ ______   ________  ________  _______           ________      ___    ___       _____  ________  _______   ___      ___ 
    |\   _ \  _   \|\   __  \|\   ___ \|\  ___ \         |\   __  \    |\  \  /  /|     / __  \|\   ___ \|\  ___ \ |\  \    /  /|
    \ \  \\\__\ \  \ \  \|\  \ \  \_|\ \ \   __/|        \ \  \|\ /_   \ \  \/  / /    |\/_|\  \ \  \_|\ \ \   __/|\ \  \  /  / /
     \ \  \\|__| \  \ \   __  \ \  \ \\ \ \  \_|/__       \ \   __  \   \ \    / /     \|/ \ \  \ \  \ \\ \ \  \_|/_\ \  \/  / / 
      \ \  \    \ \  \ \  \ \  \ \  \_\\ \ \  \_|\ \       \ \  \|\  \   \/  /  /           \ \  \ \  \_\\ \ \  \_|\ \ \    / /  
       \ \__\    \ \__\ \__\ \__\ \_______\ \_______\       \ \_______\__/  / /              \ \__\ \_______\ \_______\ \__/ /   
        \|__|     \|__|\|__|\|__|\|_______|\|_______|        \|_______|\___/ /                \|__|\|_______|\|_______|\|__|/    
                                                                      \|___|/ 

    """
    print(credits)

class BtnConfig(Canvas):
    def __init__(self, parent, text, command, radius=25, color="grey", text_color="white", **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.command = command
        self.radius = radius
        self.color = color
        self.text_color = text_color
        self.width = kwargs.get('width', 150)
        self.height = kwargs.get('height', 50)

        self.catlib_button(text)

    def catlib_button(self, text):
        self.create_oval((0, 0, self.radius, self.radius), fill=self.color, outline=self.color)
        self.create_oval((self.width - self.radius, 0, self.width, self.radius), fill=self.color, outline=self.color)
        self.create_oval((0, self.height - self.radius, self.radius, self.height), fill=self.color, outline=self.color)
        self.create_oval((self.width - self.radius, self.height - self.radius, self.width, self.height), fill=self.color, outline=self.color)
        self.create_rectangle((self.radius / 2, 0, self.width - self.radius / 2, self.height), fill=self.color, outline=self.color)
        self.create_rectangle((0, self.radius / 2, self.width, self.height - self.radius / 2), fill=self.color, outline=self.color)
        self.create_text(self.width / 2, self.height / 2, text=text, fill=self.text_color)

        self.bind("<Button-1>", lambda event: self.command())

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("CatLib UI")

        self.pack(fill=BOTH, expand=1)

        new_button = BtnConfig(self, text="New Button", command=lambda: None, width=150, height=50)
        new_button.place(x=50, y=50)

def main():
    print_credits()
    root = Tk()
    root.geometry("400x400")
    app = Window(root)
    root.mainloop()

if __name__ == '__main__':
    main()
