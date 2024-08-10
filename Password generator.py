import tkinter as tk
from tkinter import messagebox
import string
import secrets
window = tk.Tk()
window.title("Password Generator")
window.resizable(False,False)
window.geometry("400x200")
window.config(bg="#5480F7")
def generate_password():
    password_length = int(length_entry.get())
    
    if password_length < 4:
        messagebox.showerror("Error", "Password length must be at least 4 characters")
        return
    
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(password_length))
    
    result_label.config(text="Generated Password: " + password)
                        
length_label = tk.Label(window, text="Password Length:",font=("arial 10 bold"))
length_label.pack(pady=10)
length_entry = tk.Entry(window, width=20)
length_entry.pack()
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)
result_label = tk.Label(window, text="",font=("bold 10 bold"))
result_label.pack()
window.mainloop()
