from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
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


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web_entry = website_entry.get()
    em_entry = email_entry.get()
    pas_entry = password_entry.get()

    if len(web_entry) == 0 or len(pas_entry) == 0:
        messagebox.showinfo(title="website", message="Make sure you have not left any empty fields.")
    else:
        is_ok = messagebox.askokcancel(title="website", message=f"This are the details entered by you:\n "
                                                                f"Website: {web_entry}"f"\n Pass: {pas_entry}")
        if is_ok:
            with open("dataa.txt", "a") as data_file:
                data_file.write(f"{web_entry} |{em_entry}| {pas_entry}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


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
generate_pass_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", highlightthickness=0, width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ankkitmahadik14@gmail.com")

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

window.mainloop()
