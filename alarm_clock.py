import tkinter as tk
from tkinter import messagebox
import time
import threading
import pygame

# Initialize pygame mixer for alarm sound
pygame.mixer.init()

def play_alarm():
    pygame.mixer.music.load("mixkit-digital-clock-digital-alarm-buzzer-992.wav")  # Ensure you have an alarm sound file
    pygame.mixer.music.play()

def check_alarm():
    while True:
        current_time = time.strftime('%H:%M:%S')
        if current_time == set_alarm_time.get():
            play_alarm()
        time.sleep(1)

def set_alarm():
    alarm_thread = threading.Thread(target=check_alarm, daemon=True)
    alarm_thread.start()

# Create main application window
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("300x200")

# Label for current time
time_label = tk.Label(root, text="Current Time: " + time.strftime('%H:%M:%S'), font=("Arial", 12))
time_label.pack(pady=10)

# Label and Entry for setting alarm
tk.Label(root, text="Set Alarm (HH:MM:SS):").pack()
set_alarm_time = tk.StringVar()
alarm_entry = tk.Entry(root, textvariable=set_alarm_time)
alarm_entry.pack(pady=5)

# Button to set alarm
set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
