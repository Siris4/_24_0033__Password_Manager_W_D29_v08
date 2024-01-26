from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


# Window Setup:
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas Widget:
canvas = Canvas(width=200, height=189, highlightthickness=0)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 95, image=lock_img)
canvas.grid(row=0, column=1)

# Website label:
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

# Website Entry:
website_entry = Entry(width=36)
website_entry.insert(END, string="Enter website URL here! ")
website_entry.grid(row=1, column=1, columnspan=2)    #columnspan=2 is a keyword argument.

#############

# Email/Username label:
email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

# Email/Username Entry:
email_username_entry = Entry(width=36)
email_username_entry.insert(END, string="Enter Email/Username here! ")
email_username_entry.grid(row=2, column=1, columnspan=2)

#############

# Password label:
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Password Entry:
password_entry = Entry(width=17)
password_entry.insert(END, string="Enter Pass here! ")
password_entry.grid(row=3, column=1)

# Generate Password button:
def generate_pass_action():
    print("Generate Password Button was Clicked.")

generate_password_button = Button(text="Generate Password", command=generate_pass_action, width=15)
generate_password_button.grid(row=3, column=2)

# Add button:
def add_password_action():
    print("Add Password Button was Clicked.")

add_button = Button(text="Add", command=add_password_action, width=30)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
