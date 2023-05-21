import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk

def play():
    file_path = filedialog.askopenfilename()
    # TODO: Implement file upload functionality
    print("Uploaded file:", file_path)

def upload_file():
    file_path = filedialog.askopenfilename()
    # TODO: Implement file upload functionality
    print("Uploaded file:", file_path)

def download_file():
    # TODO: Implement file download functionality
    print("Downloading file")

def left():
    print(' # TODO: Implement file upload functionality')


def right():
    print(' # TODO: Implement file upload functionality')


# Create the main window
window = tk.Tk()
window.title("My Music App")
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


# Create a frame for the search bar and responses
search_frame = tk.Frame(content_frame)
search_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

# Create a search bar
search_entry = ttk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=5)

search_button = ttk.Button(search_frame, text="Search")
search_button.pack(side=tk.LEFT, padx=5)

# Create a frame for the responses
responses_frame = tk.Frame(content_frame)
responses_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

response_label = tk.Label(responses_frame)
response_label.pack(anchor=tk.W)

response_text = tk.Text(responses_frame, height=5, width=50)
response_text.pack(pady=5)

# Run the main event loop
window.mainloop()