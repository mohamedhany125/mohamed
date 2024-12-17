import tkinter as tk
from tkinter import messagebox
import pyttsx3

# Initialize the s
engine = pyttsx3.init()

def play_text():
    # Get the text from the entry field
    text = text_entry.get()
    
    # Check if the text is not empty
    if text.strip():
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("Error", "الرجاء إدخال النص.")

def set_text():
    # This function can be used for any future features you want to add
    pass

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Text to Speech")

# Create the label
label = tk.Label(root, text="أدخل النص:", font=("Arial", 14))
label.pack(pady=10)

# Create the text entry field
text_entry = tk.Entry(root, font=("Arial", 12), width=30)
text_entry.pack(pady=10)

# Create the button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Play button
play_button = tk.Button(button_frame, text="تشغيل", font=("Arial", 12), bg="lightgreen", command=play_text)
play_button.grid(row=0, column=0, padx=10)

# Set button (currently a placeholder function)
set_button = tk.Button(button_frame, text="تعيين", font=("Arial", 12), bg="lightblue", command=set_text)
set_button.grid(row=0, column=1, padx=11)

# Exit button
exit_button = tk.Button(button_frame, text="خروج", font=("Arial", 12), bg="darkgray", command=exit_app)
exit_button.grid(row=0, column=2, padx=12)

# Run the main event loop
root.mainloop()
