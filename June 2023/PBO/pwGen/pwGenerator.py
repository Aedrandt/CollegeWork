import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = random.choices(characters, k=length)
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)):
            break
    return ''.join(password)

def generate_button_clicked():
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        password_label.configure(text=f"Password baru Anda:\n{password}")
        copy_button.configure(state="normal")
    except ValueError:
        messagebox.showerror("Error", "Mohon masukkan panjang password yang valid.")

def copy_button_clicked():
    password = password_label.cget("text")
    password = password.replace("Password baru Anda:\n", "")
    window.clipboard_clear()
    window.clipboard_append(password)
    messagebox.showinfo("Password Generator", "Password berhasil disalin ke clipboard.")

# Membuat jendela utama
window = tk.Tk()
window.title("Password Generator")

# Mengatur ukuran jendela
window.geometry("300x175")

# Mengatur warna latar belakang jendela
window.configure(bg="#f0f0f0")

# Mengatur gaya ttk
style = ttk.Style()
style.configure("TLabel", background="#f0f0f0")
style.configure("TButton", font=("Arial", 10))
style.configure("TEntry", font=("Arial", 10))

# Membuat frame utama
main_frame = ttk.Frame(window, padding=20)
main_frame.pack()

# Membuat label dan entry untuk panjang password
length_label = ttk.Label(main_frame, text="Panjang Password:")
length_label.grid(row=0, column=0, sticky="w")
length_entry = ttk.Entry(main_frame, width=10)
length_entry.grid(row=0, column=1, sticky="w")

# Membuat tombol "Generate Password"
generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_button_clicked)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Membuat label untuk menampilkan password baru
password_label = ttk.Label(main_frame, text="", wraplength=300)
password_label.grid(row=2, column=0, columnspan=2)

# Membuat tombol "Copy"
copy_button = ttk.Button(main_frame, text="Copy", state="disabled", command=copy_button_clicked)
copy_button.grid(row=3, column=0, columnspan=2, pady=10)

# Menjalankan loop utama jendela
window.mainloop()