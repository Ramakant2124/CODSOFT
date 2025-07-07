import tkinter as tk
from tkinter import messagebox

# GUI setup
root = tk.Tk()
root.title("Simple Calculator || Devloper By Ramakant Chaudhari")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#CCCCFF")

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

# Widgets
tk.Label(root, text="Enter first number:",bg="#CCCCFF",font=(28)).pack(pady=5)
entry1 = tk.Entry(root,width=48,font=(20))
entry1.pack()

tk.Label(root, text="Enter second number:",bg="#CCCCFF",font=(28)).pack(pady=5)
entry2 = tk.Entry(root,width=48,font=(20))
entry2.pack()

tk.Label(root, text="Choose operation (+, -, *, /):",bg="#CCCCFF",font=(28)).pack(pady=5)
operation = tk.StringVar()
operation_entry = tk.Entry(root, textvariable=operation,width=48,font=(20))
operation_entry.pack()

tk.Button(root, text="Calculate", command=calculate,width=30,bg="#F3205F",font=(28)).pack(pady=10)

result_label = tk.Label(root, text="Result: ",bg="#CCCCFF",font=(30))
result_label.pack(pady=10)

# Run the app
root.mainloop()
