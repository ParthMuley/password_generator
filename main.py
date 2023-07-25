import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_button_clicked():
    try:
        password_length=int(length_entry.get())
        if(password_length<8):
            messagebox.showerror("The length of password","Should be greater then 8 charachter")
        else:
            generated_password = generate_password(password_length)
            password_result_label.config(text="Generated Password: " + generated_password)
    except:
        messagebox.showerror("Invalid Input","Enter correct input")

def generate_password(length=12):
    ch=string.ascii_letters+string.digits+string.punctuation
    password = ''.join(random.choice(ch) for _ in range(length))
    return password







root = tk.Tk()
root.title("Password generator")
root.geometry("480x200")
# Code to add widgets will go here...
length_label=tk.Label(root,text="Enter the Length of Password")
length_label.pack(pady=10)

length_entry=tk.Entry(root)
length_entry.pack(pady=5)

generate_button=tk.Button(root,text="generate password",command=generate_button_clicked)
generate_button.pack(pady=5)

password_result_label = tk.Label(root, text="Generated Password: ")
password_result_label.pack(pady=5)

root.mainloop()