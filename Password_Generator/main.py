from tkinter import *
from tkinter import messagebox
import pyperclip
from password import function_generate_password

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

def add_data_button() :

    website = ent_website.get()
    username = ent_username.get()
    password = ent_password.get()

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the detailed entered:\nEmain: {username}\nPassword: {password}" )

        if is_ok :
            with open("data.txt" , mode="a") as file:
                file.write(f"{website} | {username} | {password}\n")

        ent_website.delete(0, END)
        ent_username.delete(0, END)
        ent_password.delete(0, END)

def generate_password_button():
    ent_password.delete(0, END)
    temp = function_generate_password()
    ent_password.insert(0, temp)
    pyperclip.copy(temp)

frame = Frame(window)

canvas = Canvas(frame, width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

lbl_website = Label(frame, text="Website:", font=("Arial", 10))
lbl_website.grid(row=1, column=0)

lbl_username = Label(frame, text="Username:", font=("Arial", 10))
lbl_username.grid(row=2, column=0)

lbl_password = Label(frame, text="Password:", font=("Arial", 10))
lbl_password.grid(row=3, column=0)

ent_website = Entry(frame, width=54)
ent_website.grid(row=1, column=1, columnspan=2)
ent_website.focus()

ent_username = Entry(frame, width=54)
ent_username.grid(row=2, column=1, columnspan=2)


ent_password = Entry(frame, width=35)
ent_password.grid(row=3, column=1, padx=4)

btn_generate = Button(frame, text="Generate Password", command=generate_password_button)
btn_generate.grid(row=3, column=2)

btn_add = Button(frame, text="Add", width=46, command=add_data_button)
btn_add.grid(row=4, column=1, columnspan=2)

frame.pack()

window.mainloop()

