from tkinter import *

HOUR = "00"
MINUTE = "00"
SECOND = "00"
timer = None



def window_clock_timer():

    def focus_in_hour(e):
        entry_hour.delete(0, END)

    def focus_out_hour(e):
        global HOUR
        HOUR = entry_hour.get()
        if HOUR == "":
            entry_hour.insert(0, "00")

    def focus_in_minute(e):
        entry_minute.delete(0, END)

    def focus_out_minute(e):
        global MINUTE
        MINUTE = entry_minute.get()
        if MINUTE == "":
            entry_minute.insert(0, "00")

    def focus_in_second(e):
        entry_second.delete(0, END)

    def focus_out_second(e):
        global SECOND
        SECOND = entry_second.get()
        if SECOND == "":
            entry_second.insert(0, "00")



    def function_reset_timer():

        btn_start.config(state="normal")

        if HOUR != "00" or MINUTE != "00" or SECOND != "00":
            entry_hour.config(state='normal')
            entry_minute.config(state='normal')
            entry_second.config(state='normal')

            window.after_cancel(timer)

            entry_hour.delete(0, END)
            entry_minute.delete(0, END)
            entry_second.delete(0, END)


            entry_hour.insert(0, "00")
            entry_minute.insert(0, "00")
            entry_second.insert(0, "00")
        

    def function_start_timer():

        if entry_hour.get()=="00" and entry_minute.get()=="00" and entry_second.get()=="00" :
            pass

        else :

            btn_start.config(state="disabled")

            global HOUR, MINUTE, SECOND
            HOUR = int(entry_hour.get())
            MINUTE = int(entry_minute.get())
            SECOND = int(entry_second.get())
            count = HOUR*60*60 + MINUTE*60 + SECOND

            if HOUR > 0 or MINUTE > 0 or SECOND > 0:
                count_down(count)
        

    def count_down(count):
        hour = int((count/60)/60)
        minute = int(count/60)
        second = count%60

        if int(second) < 10:
            second = f"0{second}"
        if int(minute) < 10 :
            minute = f"0{minute}"
        if int(hour) < 10:
            hour = f"0{hour}"

        entry_hour.config(state='normal')
        entry_minute.config(state='normal')
        entry_second.config(state='normal')

        entry_hour.delete(0, END)
        entry_minute.delete(0, END)
        entry_second.delete(0, END)

        entry_hour.insert(0, hour)
        entry_minute.insert(0, minute)
        entry_second.insert(0, second)

        entry_hour.config(state='disabled')
        entry_minute.config(state='disabled')
        entry_second.config(state='disabled')

        if count>0 :
            global timer
            timer = window.after(1000, count_down, count-1)
        else:
            function_reset_timer()



    window = Tk()
    window.title("TIMER")
    window.config(padx=100, pady=50)


    frame_timer_entry = Frame(window)

    entry_hour = Entry(frame_timer_entry, width=2, font=("Arial", 60, "bold"), bg="#f8f7f6", highlightthickness=0, relief="flat")
    entry_hour.insert(0, "00")
    entry_hour.bind('<FocusIn>', focus_in_hour)
    entry_hour.bind('<FocusOut>', focus_out_hour)
    entry_hour.grid(row=0, column=0)

    label_colon_1 = Label(frame_timer_entry, text=":", font=("Arial", 60, "bold"))
    label_colon_1.grid(row=0, column=1)

    entry_minute = Entry(frame_timer_entry, width=2, font=("Arial", 60, "bold"), bg="#f8f7f6", highlightthickness=0, relief="flat")
    entry_minute.insert(0, "00")
    entry_minute.grid(row=0, column=2,)
    entry_minute.bind('<FocusIn>', focus_in_minute)
    entry_minute.bind('<FocusOut>', focus_out_minute)

    label_colon_2 = Label(frame_timer_entry, text=":", font=("Arial", 60, "bold"))
    label_colon_2.grid(row=0, column=3)

    entry_second = Entry(frame_timer_entry, width=2, font=("Arial", 60, "bold"), bg="#f8f7f6", highlightthickness=0, relief="flat")
    entry_second.insert(0, "00")
    entry_second.grid(row=0, column=4)
    entry_second.bind('<FocusIn>', focus_in_second)
    entry_second.bind('<FocusOut>', focus_out_second)

    frame_timer_button = Frame(window)

    btn_start = Button(frame_timer_button, text="Start", command=function_start_timer, padx=40, pady=15)
    btn_start.grid(row=0, column=0, padx=30)

    btn_reset = Button(frame_timer_button, text="Reset", command=function_reset_timer, padx=40, pady=15)
    btn_reset.grid(row=0, column=1, padx=30)

    frame_timer_entry.pack()
    frame_timer_button.pack(pady=30)


    window.mainloop()
