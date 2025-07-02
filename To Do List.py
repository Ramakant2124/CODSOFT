import tkinter as tk
from tkinter import messagebox

# === GUI Setup ===
root = tk.Tk()
root.title("To-Do List || Devloper By Ramakant Chaudhari")
root.geometry("700x700")
root.resizable(False, False)
root.configure(bg="#daa6ef")

TASKS_FILE = "tasks.txt"

# === Functions ===
def add_task(event=None):
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Select Task", "Please select a task to delete.")

def clear_all_tasks():
    if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
        task_listbox.delete(0, tk.END)

def save_tasks():
    with open(TASKS_FILE, "w") as f:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            for line in f:
                task = line.strip()
                if task:
                    task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

def update_task():
    try:
        index = task_listbox.curselection()[0]
        updated_text = task_entry.get().strip()
        if updated_text:
            task_listbox.delete(index)
            task_listbox.insert(index, updated_text)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Updated task cannot be empty.")
    except IndexError:
        messagebox.showwarning("Select Task", "Please select a task to update.")

def fill_entry_from_list(event):
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)
        task_entry.delete(0, tk.END)
        task_entry.insert(0, task)
    except IndexError:
        pass

# Entry Frame
entry_frame = tk.Frame(root, bg="red")
entry_frame.pack(pady=10)

task_entry = tk.Entry(entry_frame, width=48, font=('Arial', 14))
task_entry.pack(side=tk.LEFT, padx=5)
task_entry.bind("<Return>", add_task)

add_button = tk.Button(entry_frame, text="Add", width=15, command=add_task ,bg="#00C36B", fg="black")
add_button.pack(side=tk.LEFT)

# Listbox Frame with Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(
    list_frame,
    width=70,
    height=26,
    font=('Arial', 12),
    bg="#f9e79f",
    fg="black",
    yscrollcommand=scrollbar.set
)
task_listbox.pack()
scrollbar.config(command=task_listbox.yview)
task_listbox.bind('<<ListboxSelect>>', fill_entry_from_list)

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

delete_button = tk.Button(button_frame, text="Delete", width=43, command=delete_task,bg="#F30000", fg="black")
delete_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", width=43, command=clear_all_tasks,bg="#50D6FF", fg="black")
clear_button.grid(row=0, column=1, padx=5)

update_button = tk.Button(button_frame, text="Update", width=43, command=update_task,bg="#B7FF00", fg="black")
update_button.grid(row=1, column=0, padx=5, pady=5)

save_button = tk.Button(button_frame, text="Save", width=43, command=save_tasks,bg="#00C36B", fg="black")
save_button.grid(row=1, column=1, padx=5, pady=5)

load_button = tk.Button(button_frame, text="Load", width=90, command=load_tasks,bg="#2196F3", fg="black")
load_button.grid(row=2, column=0, columnspan=2, pady=5)

# Load tasks on startup
load_tasks()

# Run app
root.mainloop()
