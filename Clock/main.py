from alarm_window import window_clock_alarm
from alarm_window import ALARM
from timer_window import window_clock_timer
from stop_watch_window import window_stop_watch
from tkinter import *
from tkinter import messagebox
import datetime
import pygame


NOW = datetime.datetime.now()
HOUR = NOW.strftime("%I")
MINUTE = NOW.minute
SECOND = NOW.second
MERIDIEM = NOW.strftime("%p")

def window_cancel():

    ask = messagebox.askyesno(title="Quit", message="Do you want to quit?")
    if ask:
        print()
        window.destroy()

def show() :

    global NOW
    NOW = datetime.datetime.now()
    HOUR = NOW.strftime("%I")
    MINUTE = NOW.minute
    # SECOND = NOW.second
    MERIDIEM = NOW.strftime("%p")

    if int(MINUTE) < 10:

        MINUTE = f"0{MINUTE}"

    canvas.itemconfig(time_text, text=f"{HOUR}:{MINUTE}")
    # print(f"{HOUR}:{MINUTE}:{SECOND}")
    canvas.itemconfig(meridiem_text, text=MERIDIEM)
    checking = ALARM[0] == HOUR and ALARM[1] == str(MINUTE) and ALARM[2] == MERIDIEM

    # exact_time = [HOUR, MINUTE, MERIDIEM]
    # print(f"Alarm : {ALARM}")
    # print(f"Time : {exact_time}")
    # print(f"Checking : {checking}")

    if  checking:
        print("\nAlarm is ringing")
        pygame.init()
        pygame.mixer.music.load("ringtone_alarm.mp3")
        pygame.mixer.music.play()
    window.after(1000, show)


window = Tk()
window.title("Clock")
window.iconbitmap("icon.ico")


canvas = Canvas(height=500, width=500)
img = PhotoImage(file="clock.png").subsample(2, 2)
canvas.create_image(250, 250, image=img)
time_text = canvas.create_text(250, 280, text="00:00", fill="white", font=("Arial", 80))
meridiem_text = canvas.create_text(360, 350, text="", fill="white", font=("Arial", 15))
canvas.pack()

frm_button = Frame(master=window)

btn_set_alarm = Button(frm_button, text="Alarm", width=18, height=3, font=("Arial", 10), command=window_clock_alarm)
btn_set_timer = Button(frm_button, text="Timer", width=18, height=3, font=("Arial", 10), command=window_clock_timer)
btn_set_stopwatch = Button(frm_button, text="Stop Watch", width=18, height=3, font=("Arial", 10), command=window_stop_watch)

btn_set_alarm.pack(side=LEFT, padx=20, pady=20, fill=BOTH, expand=True)
btn_set_timer.pack(side=LEFT, padx=20, pady=20, fill=BOTH, expand=True)
btn_set_stopwatch.pack(side=LEFT, padx=20, pady=20, fill=BOTH, expand=True)

frm_button.pack()

show()

window.protocol("WM_DELETE_WINDOW", window_cancel)
window.mainloop()
