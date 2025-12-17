import tkinter as tk
from tkinter import messagebox

def yes_clicked():
    messagebox.showinfo("❤️ Yay!", "Forever starts now 💍💕")

def no_clicked():
    messagebox.showwarning("💔 Oh no", "Still wishing you happiness 🌸")

root = tk.Tk()
root.title("Heart Proposal ❤️")
root.geometry("350x250")

label = tk.Label(root, text="Will you be mine? ❤️", font=("Arial", 16))
label.pack(pady=20)

yes_btn = tk.Button(root, text="Yes ❤️", width=10, command=yes_clicked)
yes_btn.pack(pady=5)

no_btn = tk.Button(root, text="No 💔", width=10, command=no_clicked)
no_btn.pack(pady=5)

root.mainloop()
