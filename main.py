from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    char_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    num_list = [choice(numbers) for _ in range(randint(2, 4))]

    password = char_list + symbol_list + num_list

    shuffle(password)

    x = "".join(password)
    password_entry.insert(0, x)
    pyperclip.copy(x)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web_entry = website_entry.get()
    em_entry = email_entry.get()
    pas_entry = password_entry.get()
    data_dict = {web_entry:
                     {"email": em_entry
                         , "pass1": pas_entry}
                 }

    if len(web_entry) == 0 or len(pas_entry) == 0:
        messagebox.showinfo(title="website", message="Make sure you have not left any empty fields.")
    else:
        try:
            with open("dataa.json", "r") as data_file:
                # reading the data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("dataa.json", "w") as data_file:
                json.dump(data_dict, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(data_dict)
            with open("dataa.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    web_entry = website_entry.get()
    try:
        with open("dataa.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="alert", message="No data file found")
    else:
        if web_entry in data:
            password = data[web_entry]["pass1"]
            email = data[web_entry]["email"]
            messagebox.showinfo(title=web_entry, message=f"email: {email}\npassword: {password}")
        else:
            messagebox.showinfo(title=web_entry, message=f"No details for the {web_entry} exists")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", foreground="black")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ", foreground="black")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ", foreground="black")
password_label.grid(row=3, column=0)

# Buttons
generate_pass_button = Button(text="Generate Password", width=20, highlightthickness=0, command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", highlightthickness=0, width=57, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", highlightthickness=0, width=20, command=find_password)
search_button.grid(row=1, column=2)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=57)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ankkitmahadik14@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

window.mainloop()
