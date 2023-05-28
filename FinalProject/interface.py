import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
import time

from extract import extract_text, join_text
import threading
import pyttsx3

import settings
settings.init()

engine = pyttsx3.init()

voices = engine.getProperty('voices')

change = False

def play():
    print("Reading: ", settings.reading)
    settings.reading = not settings.reading

def upload_file():
    file_types = [("Files", "*.pdf"), ("Files", "*.docx"), ("Files", "*.txt")]
    file_path = filedialog.askopenfilename(filetypes=file_types)
    print("Uploaded file:", file_path)

    settings.filePath = file_path
    read_document(file_path)

def download_file():
    print("Converting and Downloading file")
    thread = threading.Thread(target=convert_and_download)
    thread.start()


def convert_and_download():
    text = join_text(extract_text(settings.filePath))

    engine = pyttsx3.init()

    engine.save_to_file(text, 'file.wav')

    engine.runAndWait()

def left():
    settings.sentenceIndex -= 1


def right():
    settings.sentenceIndex += 1

def read_document(filePath):
    text = extract_text(filePath)
    settings.reading = True

    settings.sentenceIndex = 0
    readThread = threading.Thread(target=read_text, args=(text))
    readThread.start()

def read_text(*text):
    while(settings.sentenceIndex < len(text)):
        if(settings.appRunning == False):
            settings.reading = False
            return
        
        if(settings.reading):

            engine = pyttsx3.init()

            voices = engine.getProperty('voices')

            if (not change):

                engine.setProperty('voice', voices[0].id)
            
            else:

                engine.setProperty('voice', voices[1].id)
            
            update_text_area(text[settings.sentenceIndex])

            engine.say(text[settings.sentenceIndex])
            engine.runAndWait()
            engine.stop()
            settings.sentenceIndex += 1


        else:
            time.sleep(0.1)

        progress_bar['value'] = (settings.sentenceIndex / len(text)) * 100
        window.update_idletasks()

def update_text_area(text): 
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, text)


def change_voice(is_Female): 
        global change
        change = is_Female

    


# Create the main window
window = tk.Tk()
window.title("Speechify")
window.geometry("800x600")  # Set the window size

# Create a header frame
header_frame = tk.Frame(window, bg="#1DB954", height=80)
header_frame.pack(fill=tk.X)

# Create a logo label
logo_label = tk.Label(header_frame, text="SPEECHIFY", font=("Arial", 24), fg="white", bg="#1DB954")
logo_label.pack(pady=10)


# Criar um frame para o conteúdo
content_frame = tk.Frame(window, bg="white", padx=20, pady=20)
content_frame.pack(fill=tk.BOTH, expand=True)

# Criar a área de texto
text_area = tk.Text(content_frame, height=10, width=50)
text_area.pack(pady=10, padx=(0, 10))

# Load button icons
upload_icon = Image.open("upload_icon.png") 
download_icon = Image.open("download_icon.png")  
play_icon = Image.open("play_icon.jpg")  
left_icon = Image.open("left_icon.jpg") 
right_icon = Image.open("right_icon.jpg") 


# Resize button icons
upload_icon = upload_icon.resize((32, 32), Image.ANTIALIAS)
download_icon = download_icon.resize((32, 32), Image.ANTIALIAS)
play_icon = play_icon.resize((32, 32), Image.ANTIALIAS)
left_icon = left_icon.resize((32, 32), Image.ANTIALIAS)
right_icon = right_icon.resize((32, 32), Image.ANTIALIAS)

# Convert icons to Tkinter-compatible format
upload_image = ImageTk.PhotoImage(upload_icon)
download_image = ImageTk.PhotoImage(download_icon)
play_image = ImageTk.PhotoImage(play_icon)
left_image = ImageTk.PhotoImage(left_icon)
right_image = ImageTk.PhotoImage(right_icon)

# Create a frame for the buttons
buttons_frame = tk.Frame(content_frame)
buttons_frame.pack(side=tk.TOP, padx=10, pady=10)

# Create buttons with icons
download_button = ttk.Button(buttons_frame, image=download_image, command=download_file)
download_button.pack(side=tk.LEFT, padx=5)

left_button = ttk.Button(buttons_frame, image=left_image, command=left)
left_button.pack(side=tk.LEFT, padx=5)

play_button = ttk.Button(buttons_frame, image=play_image, command=play)
play_button.pack(side=tk.LEFT, padx=5)

right_button = ttk.Button(buttons_frame, image=right_image, command=right)
right_button.pack(side=tk.LEFT, padx=5)

upload_button = ttk.Button(buttons_frame, image=upload_image, command=upload_file)
upload_button.pack(side=tk.LEFT, padx=5)

# Create a frame for the progress bar
progress_frame = tk.Frame(content_frame)
progress_frame.pack(side=tk.TOP, padx=10, pady=5)

# Create a progress bar
progress_bar = ttk.Progressbar(progress_frame, orient=tk.HORIZONTAL, length=400, mode='indeterminate')
progress_bar.pack(padx=5)

# Create a frame for the cards
cards_frame = tk.Frame(content_frame)
cards_frame.pack(pady=10)

# Define the card style
card_style = ttk.Style()
card_style.configure("Card.TFrame", background="white", relief=tk.RAISED, borderwidth=1)
card_style.configure("Card.TLabel", font=("Arial", 12))

# Create cards with name and play button
for i in range(len(voices)):
    card_frame = ttk.Frame(cards_frame, style="Card.TFrame")
    card_frame.pack(side=tk.LEFT, padx=10, pady=10)

    card_name_label = ttk.Label(card_frame, text=voices[i].name.split(" ")[1] + "    ", style="Card.TLabel")
    card_name_label.pack(pady=5, side=tk.LEFT)

    if(i == 0):
        card_play_button = ttk.Button(card_frame, image=play_image, command=lambda: change_voice(False))
        card_play_button.pack(pady=5)
    else:
        card_play_button = ttk.Button(card_frame, image=play_image, command=lambda: change_voice(True))
        card_play_button.pack(pady=5)

def close_main_windows():
    settings.appRunning = False
    while(settings.reading):
        time.sleep(0.1)
    window.destroy()

window.protocol('WM_DELETE_WINDOW', close_main_windows)  # root is your root window

# Run the main event loop
settings.appRunning = True
window.mainloop()