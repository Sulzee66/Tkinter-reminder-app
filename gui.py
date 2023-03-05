import tkinter as tk
from base import Reminder
from countdown import count
import threading


def set_alarm():
    hour = hour_entry.get()
    minute = minute_entry.get()

    # modify hour and minute
    try:
        if int(hour) < 10:
            hour = "0" + hour
        if int(minute) < 10:
            minute = "0" + minute
    except:
        print("Error")

    message = message_entry.get()
    reminder = Reminder(hour, minute, message)
    count()

def start_set_alarm_thread(event):
    global alarm_thread
    alarm_thread = threading.Thread(target=set_alarm)
    alarm_thread.daemon = True
    alarm_thread.start()

# create a window
window = tk.Tk()

# set the size of window
window.geometry("400x400")

# add a title
window.title("Reminder App")

# set background color
window.configure(bg="#252525")

window.resizable(False, False)

# add header text
label = tk.Label(window, text="Set Reminder", font=('Fantasy', 18))
label.configure(fg="white", bg="#252525")
label.pack(padx=20, pady=20)

# creating input field for hours
hour_label = tk.Label(window, text="Hour: ", font=('Fantasy', 18))
hour_label.configure(fg="white", bg="#252525")
hour_label.place(x=50, y = 100)

hour_entry = tk.Entry(window, font=('Arial 12'))
hour_entry.place(x=180, y = 105)

# creating input field minutes
minute_label = tk.Label(window, text="Minute: ", font=('Fantasy', 18))
minute_label.configure(fg="white", bg="#252525")
minute_label.place(x=50, y = 150)

minute_entry = tk.Entry(window, font=('Arial 12'))
minute_entry.place(x=180, y = 155)

# creating input field for message
message_label = tk.Label(window, text="Message: ", font=('Fantasy', 18))
message_label.configure(fg="white", bg="#252525")
message_label.place(x=50, y = 200)

message_entry = tk.Entry(window, font=('Arial 12'))
message_entry.place(x=180, y = 205)

btn = tk.Button(window, text="Confirm", height=1, width=22, borderwidth=0, font=("Fantasy", 18), command=lambda:start_set_alarm_thread(None))
btn.configure(fg="white", bg="green")
btn.place(x=50, y=300)

window.mainloop()