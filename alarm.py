import time
from playsound import playsound

def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}. Waiting...")
    
    while True:
        current_time = time.strftime("%H:%M:%S")  # Get the current time in HH:MM:SS format
        if current_time == alarm_time:
            print("Wake up! Alarm is ringing...")
            playsound('/path/to/your/soundfile.mp3')  # Replace with your MP3 file path
            break
        time.sleep(1)  # Check every second for the alarm

# Example: Set alarm for 2 minutes from now
if __name__ == "__main__":
    current_time = time.strftime("%H:%M:%S")
    print(f"Current time: {current_time}")
    
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    set_alarm(alarm_time)
