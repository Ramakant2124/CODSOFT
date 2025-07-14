import tkinter as tk
from tkinter import messagebox, simpledialog

# --- GUI Setup ---
root = tk.Tk()
root.title("Contact Book || Devloper By Ramakant Chaudhari")
root.geometry("600x450")
root.resizable(False, False)
root.configure(bg="lightblue")

# Left Frame - Contact List and Search
left_frame = tk.Frame(root)
left_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

tk.Label(left_frame, text="Contacts", font=("Arial", 14, "bold")).pack()

# Store contacts in a dictionary: {name: {phone, email, address}}
contacts = {}

# --- Functions ---

def refresh_contact_list():
    contact_listbox.delete(0, tk.END)
    for name, info in contacts.items():
        display = f"{name} - {info['phone']}"
        contact_listbox.insert(tk.END, display)

def add_contact():
    name = name_var.get().strip()
    phone = phone_var.get().strip()
    email = email_var.get().strip()
    address = address_text.get("1.0", tk.END).strip()

    if not name or not phone:
        messagebox.showwarning("Missing Info", "Name and Phone are required.")
        return

    if name in contacts:
        messagebox.showwarning("Duplicate", "Contact name already exists.")
        return

    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    messagebox.showinfo("Success", f"Contact '{name}' added.")
    clear_form()
    refresh_contact_list()

def clear_form():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_text.delete("1.0", tk.END)

def on_contact_select(event):
    if not contact_listbox.curselection():
        return
    index = contact_listbox.curselection()[0]
    selected = contact_listbox.get(index)
    name = selected.split(" - ")[0]
    contact = contacts.get(name, {})
    if contact:
        name_var.set(name)
        phone_var.set(contact['phone'])
        email_var.set(contact['email'])
        address_text.delete("1.0", tk.END)
        address_text.insert(tk.END, contact['address'])

def update_contact():
    selected_indices = contact_listbox.curselection()
    if not selected_indices:
        messagebox.showwarning("Select Contact", "Please select a contact to update.")
        return

    old_index = selected_indices[0]
    old_entry = contact_listbox.get(old_index)
    old_name = old_entry.split(" - ")[0]

    new_name = name_var.get().strip()
    new_phone = phone_var.get().strip()
    new_email = email_var.get().strip()
    new_address = address_text.get("1.0", tk.END).strip()

    if not new_name or not new_phone:
        messagebox.showwarning("Missing Info", "Name and Phone are required.")
        return

    # Check if new name conflicts with existing contact (other than the current one)
    if new_name != old_name and new_name in contacts:
        messagebox.showwarning("Duplicate", "Another contact with this name exists.")
        return

    # Remove old contact if name changed
    if new_name != old_name:
        del contacts[old_name]

    contacts[new_name] = {'phone': new_phone, 'email': new_email, 'address': new_address}
    messagebox.showinfo("Success", f"Contact '{new_name}' updated.")
    clear_form()
    refresh_contact_list()

def delete_contact():
    selected_indices = contact_listbox.curselection()
    if not selected_indices:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")
        return

    index = selected_indices[0]
    selected = contact_listbox.get(index)
    name = selected.split(" - ")[0]

    confirm = messagebox.askyesno("Confirm Delete", f"Delete contact '{name}'?")
    if confirm:
        del contacts[name]
        messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")
        clear_form()
        refresh_contact_list()

def search_contact():
    query = simpledialog.askstring("Search", "Enter name or phone number:")
    if not query:
        return

    results = []
    query_lower = query.lower()
    for name, info in contacts.items():
        if query_lower in name.lower() or query_lower in info['phone']:
            results.append(f"{name} - {info['phone']}")

    contact_listbox.delete(0, tk.END)
    if results:
        for res in results:
            contact_listbox.insert(tk.END, res)
    else:
        messagebox.showinfo("No Results", "No contacts found matching your search.")

def show_all_contacts():
    refresh_contact_list()

contact_listbox = tk.Listbox(left_frame, width=30, height=20,bg="lightblue")
contact_listbox.pack(pady=5)
contact_listbox.bind('<<ListboxSelect>>', on_contact_select)

btn_frame = tk.Frame(left_frame)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Search", width=12, command=search_contact,bg="#f4d03f", fg="black").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Show All", width=12, command=show_all_contacts,bg="#ed26ff", fg="black").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=12, command=delete_contact,bg="#ff0000", fg="black").grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Update", width=12, command=update_contact,bg="#0da200", fg="black").grid(row=1, column=1, padx=5, pady=5)

# Right Frame - Contact Form
right_frame = tk.Frame(root,bg="lightblue")
right_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

tk.Label(right_frame, text="Contact Details", font=("Arial", 14, "bold"),bg="lightblue").pack()

form_frame = tk.Frame(right_frame,bg="lightblue")
form_frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Name
tk.Label(form_frame, text="Name *=",bg="lightblue").grid(row=0, column=0, sticky=tk.W, pady=2)
name_var = tk.StringVar()
tk.Entry(form_frame, textvariable=name_var, width=40,font=(18)).grid(row=0, column=1, pady=2)

# Phone
tk.Label(form_frame, text="Phone *=",bg="lightblue").grid(row=1, column=0, sticky=tk.W, pady=2)
phone_var = tk.StringVar()
tk.Entry(form_frame, textvariable=phone_var, width=40,font=(18)).grid(row=1, column=1, pady=2)

# Email
tk.Label(form_frame, text="Email =",bg="lightblue").grid(row=2, column=0, sticky=tk.W, pady=2)
email_var = tk.StringVar()
tk.Entry(form_frame, textvariable=email_var, width=40,font=(18)).grid(row=2, column=1, pady=2)

# Address
tk.Label(form_frame, text="Address =",bg="lightblue").grid(row=3, column=0, sticky=tk.NW, pady=2)
address_text = tk.Text(form_frame, width=40, height=5,font=(18))
address_text.grid(row=3, column=1, pady=2)

# Add Contact button
tk.Button(right_frame, text="Add Contact", bg="#00DDFF", fg="white", width=20, command=add_contact).pack(pady=10)

# Start with empty list
refresh_contact_list()

root.mainloop()
