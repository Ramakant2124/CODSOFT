import tkinter as tk
from tkinter import messagebox
import random
import string

# Tkinter GUI Setup
root = tk.Tk()
root.title(" Password Generator || Devloper By Ramakant Chaudhari")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#fad7a0")

# Title
tk.Label(root, text="Create a Strong Password", font=("Arial", 16, "bold"), bg="#fad7a0").pack(pady=15)

# Subtitle
tk.Label(root, text="Choose length and click generate", font=("Arial", 10), bg="#fad7a0").pack()

# Function to generate the password
def generate_password():
    length = length_slider.get()

    if length < 4:
        messagebox.showwarning("Too Short", "Let's make it at least 4 characters for security.")
        return

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_chars = lowercase + uppercase + digits + symbols

    # Ensure password includes all character types
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    password_var.set(''.join(password))

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied!", "Your password has been copied.")
    else:
        messagebox.showwarning("Nothing to Copy", "Please generate a password first.")

# Length slider
length_slider = tk.Scale(root, from_=4, to=50, orient=tk.HORIZONTAL, length=300,
                         font=("Arial", 10), bg="#fad7a0", highlightthickness=0, troughcolor="#ddd")
length_slider.set(12)
length_slider.pack(pady=10)

# Generate button
tk.Button(root, text=" Generate Password", font=("Arial", 11),
          bg="#5dade2", fg="white", padx=10, pady=5, command=generate_password).pack(pady=10)

# Password display field
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=('Courier', 14), width=30, justify='center').pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", font=("Arial", 10),
          bg="#a569bd", fg="white", padx=10, pady=5, command=copy_to_clipboard).pack(pady=10)

# Optional: generate one on start
generate_password()

# Run the GUI
root.mainloop()
