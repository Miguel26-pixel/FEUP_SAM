import tkinter as tk
from tkinter import ttk

# Create a custom tkinter theme
custom_theme = ttk.Style()
custom_theme.configure('Custom.TButton', font=('Helvetica', 16), foreground='#ffffff', background='#4b0082')

# Create a main window
root = tk.Tk()
root.geometry('600x400')
root.title('Amazing UI')

# Create a label
label = ttk.Label(root, text='Welcome to my amazing UI!', font=('Helvetica', 24))
label.pack(pady=20)

# Create a button
button = ttk.Button(root, text='Click me!', style='Custom.TButton')
button.pack()

# Run the application
root.mainloop()