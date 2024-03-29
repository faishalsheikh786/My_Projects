from tkinter import *
from tkinter import ttk
import datetime

NOW = datetime.datetime.now()
HOUR = NOW.strftime("%I")
MINUTE = NOW.minute
SECOND = NOW.second
MERIDIEM = NOW.strftime("%p")
ALARM = ["", "", ""]



def window_clock_alarm():

    def finalizing_alarm():
        global ALARM
        x = Combo_hour.get()
        y = Combo_minute.get()
        z = Combo_meridiem.get()
        ALARM[0] = x
        ALARM[1] = y
        ALARM[2] = z
        print(f"\nHour:{x}  Minute:{y}  Meridiem:{z}\n")
        alarm_window.destroy()

    alarm_window = Tk()
    alarm_window.geometry("320x150")
    alarm_window.title("Alarm")
    frame = Frame(alarm_window)

    hrslist = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    minlist = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']
    meridiemlist = ["AM", "PM"]

    Combo_hour = ttk.Combobox(frame, values = hrslist, width=10)
    Combo_hour.set("Hour")
    Combo_hour.grid(row=0, column=0, padx = 10, pady = 20)

    Combo_minute = ttk.Combobox(frame, values = minlist, width=10)
    Combo_minute.set("Minute")
    Combo_minute.grid(row=0, column=1, padx = 10, pady = 20)

    Combo_meridiem = ttk.Combobox(frame, values = meridiemlist, width=10)
    Combo_meridiem.set("AM")
    Combo_meridiem.grid(row=0, column=2, padx = 10, pady = 20)

    frame.pack()

    btn_set = Button(alarm_window, text="Set", width=12, height=2, command=finalizing_alarm)
    btn_set.pack(padx=20)

    alarm_window.mainloop()
