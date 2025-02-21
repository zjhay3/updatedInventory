# First Screen
from tkinter import *
from tkinter.ttk import Progressbar
import sys
import os
import time

def resource_path(relative_path):
    """ Get absolute path to resource for development and PyInstaller executable """
    try:
        base_path = sys._MEIPASS  # Temporary folder for PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = Tk()

# Correct image path resolution
image_path = resource_path(os.path.join("images", "first_screen.png"))
image = PhotoImage(file=image_path)

# Window configuration
height = 450
width = 600
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')
root.overrideredirect(1)
root.wm_attributes('-topmost', True)
root.config(background='#ffffff')

# Background image
bg_label = Label(root, image=image)
bg_label.place(x=0, y=0)

# Welcome labels
welcome_label = Label(text='Welcome to MSD Godspeed Exhibits Corp.', bg='white', font=("arial", 15, "bold"), fg='black')
welcome_label.place(x=100, y=20)

created_by_label = Label(text='Founded By Melchor Sacramento Domingo ', bg='white', font=("arial", 11, "bold"), fg='black')
created_by_label.place(x=170, y=50)

# Progress bar
progress_label = Label(root, text="Please Wait...", font=('arial', 13, 'bold'), fg='black', bg='white')
progress_label.place(x=225, y=350)
progress = Progressbar(root, orient=HORIZONTAL, length=550, mode='determinate')
progress.place(x=25, y=390)

# Exit button
exit_btn = Button(text='x', bg='red', command=lambda: exit_window(), bd=0, font=("arial", 16, "bold"),
                  activebackground='#fd6a36', fg='white')
exit_btn.place(x=570, y=0)

def exit_window():
    sys.exit(root.destroy())

import subprocess
import os
import sys

def top():
	root.withdraw()
	startupinfo = None
	if os.name == 'nt':
		startupinfo = subprocess.STARTUPINFO()
		startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW # Hides the console window

	if getattr(sys, 'frozen', False):
		# Running as a bundled executable
		executable = os.path.join(os.path.dirname(sys.executable), 'productManager.exe')
		subprocess.Popen(
			[executable],
			startupinfo=startupinfo # Hides CMD window in Pycharm
		)
	else:
		# Running in development environment(Pycharm)
		executable = os.path.abspath('productManager.py')
		subprocess.Popen(
			[sys.executable, 'productManager.py'],
			startupinfo=startupinfo # Hides CMD window in Pycharm
		)
	os._exit(0) # Terminate StartApp.py immidiately after launching

#def top():
    #root.withdraw()
    #os.system("python productManager.py")
    #root.destroy()

#def top():
    #root.withdraw()
    #if getattr(sys, 'frozen', False):
        #   Running in PyInstaller bundle
        #executable = os.path.join(sys._MEIPASS, 'productManager.exe')
        #os.system(executable)
    #else:
        #   Running in normal Python environment
        #os.system(f'"{sys.executable}" productManager.py')
    #root.destroy()


# Loading system animation
i = 0
def loadsystem():
    global i
    if i <= 100:
        if i == 90:
            time.sleep(2)
        txt = f'Please Wait...  {i}%'
        progress_label.config(text=txt)
        progress_label.after(10, loadsystem)
        progress['value'] = i
        i += 1
    else:
        top()

loadsystem()
root.mainloop()
