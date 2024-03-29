from tkinter import *

MINUTE = 0
SECOND = 0
COUNT = 0
RESET_COUNT = 0
timer = None


def window_stop_watch() :

    def reset() :
        global MINUTE, SECOND, COUNT, RESET_COUNT
        MINUTE = 0
        SECOND = 0
        COUNT = 0
        RESET_COUNT = 0
        label.config(text="00 : 00")
        window.after_cancel(timer)
        btn_start.config(state="normal")


    def stop() :
        global timer, COUNT
        COUNT = RESET_COUNT
        window.after_cancel(timer)
        btn_start.config(state="normal")


    def start():
        count_down(COUNT)
        btn_start.config(state="disabled")


    def count_down(count):

        global MINUTE, SECOND, RESET_COUNT, timer
        RESET_COUNT = count

        SECOND = count%60


        if count>0 and int(count%60) == 0 :
            MINUTE = int(MINUTE)+1
        if int(MINUTE) < 10 :
            MINUTE = ""
            MINUTE = f"0{int(count/60)}"
        elif int(MINUTE) == 10 :
            MINUTE = 10
            
        if int(SECOND) < 10:
            SECOND = f"0{SECOND}"

        # print(f"MINUTE : {MINUTE}   SECOND : {SECOND} COUNT : {count}")
        label.config(text=f"{MINUTE} : {SECOND}")
        timer = window.after(1000, count_down, count+1)


    window = Tk()
    window.title("Stopwatch")
    window.config(padx=20, pady=20)

    label = Label(window, text="00 : 00", font=("Arial", 70, "bold"))
    label.pack()

    frame_button = Frame(window)

    btn_start = Button(frame_button, text="Start", font=("Arial", 10), padx=30, pady=10, command=start)
    btn_start.grid(row=0, column=0, padx=20)

    btn_stop = Button(frame_button, text="Stop", font=("Arial", 10), padx=30, pady=10 , command=stop)
    btn_stop.grid(row=0, column=1, padx=20)

    btn_reset = Button(frame_button, text="Reset", font=("Arial", 10), padx=30, pady=10, command=reset)
    btn_reset.grid(row=0, column=2, padx=20)

    frame_button.pack(pady=20)


    window.mainloop()
    