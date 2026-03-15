import tkinter as tk
from tkinter import messagebox
import requests


def process_login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter both username and password.")
        return

    try:
        response = requests.post(
            "http://127.0.0.1:8000/login",
            json={"username": username, "password": password}
        )

        if response.status_code == 200:
            messagebox.showinfo("Success", "Login successful!")
        else:
            error_msg = response.json().get("detail", "Login failed")
            messagebox.showerror("Auth Failed", error_msg)

    except requests.exceptions.ConnectionError:
        messagebox.showerror("Connection Error", "Could not connect to the server. Is FastAPI running on port 8000?")



def show_login_fields():
    initial_login_btn.pack_forget()
    frame.pack(expand=True)

root = tk.Tk()
root.title("Login App")
root.geometry("300x250")

initial_login_btn = tk.Button(root, text="Login", width=15, height=2, command=show_login_fields)
initial_login_btn.pack(expand=True)

frame = tk.Frame(root)

tk.Label(frame, text="Username:").pack(pady=(10, 0))
username_entry = tk.Entry(frame)
username_entry.pack(pady=5)

tk.Label(frame, text="Password:").pack(pady=(10, 0))
password_entry = tk.Entry(frame, show="*")
password_entry.pack(pady=5)

submit_btn = tk.Button(frame, text="Submit", width=10, command=process_login)
submit_btn.pack(pady=15)

root.mainloop()