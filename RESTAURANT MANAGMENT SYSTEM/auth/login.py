import session
from dashboard.dashboard import open_dashboard
from database.queries import login_user, check_user
from database.queries import update_login_status
import tkinter as tk
from tkinter import messagebox
def open_login():
    window = tk.Tk()
    window.title("Login")
    window.geometry('350x350')
    window.configure(background=("#f0f0f0"))
    window.resizable(False, False)
    title = tk.Label(window, text="LOGIN", font=("Arial", 18, "bold"))
    title.pack(pady=20)
    username = tk.Label(window, text="Enter Contact", font=("Arial", 12))
    username.pack()
    username_entry = tk.Entry(window, width=20, font=("Arial", 13))
    username_entry.pack(pady=10)
    password = tk.Label(window, text="Enter Password", font=("Arial", 13))
    password.pack()
    password_entry = tk.Entry(window, width=20, font=("Arial", 13), show="*")
    password_entry.pack(pady=10)

    # conncetion
    def login():
        contact = username_entry.get()
        password = password_entry.get()

        if contact == "" or password == "":
            messagebox.showwarning("Error","Enter contact and Password")
            return
        if not contact.isdigit():
            messagebox.showerror("Error","Contact must contain only numbers")
            return
        if len(contact) !=10:
            messagebox.showerror("Error","Contact must be exatly 10 digits")
            return
        user = login_user(contact, password)
        user_contact=check_user(contact)
        if user:
            session.current_user=user
            update_login_status(contact,1)
            messagebox.showinfo("Success", "Login Successfully")
            window.destroy()
            open_dashboard()

        elif user_contact and not user:
            messagebox.showerror("Error", "Incorrect Contact or Password")

        elif not user_contact:
            messagebox.showerror("Account Not Found","You don't have an account. Please Signup First")
            window.destroy()
            from auth.singup import open_signup
            open_signup()

    login_btn = tk.Button(window, text="Login", width=10, height=1, bg="blue", fg="white", font=("Arial", 12, "bold"),
                          command=login)
    login_btn.pack(pady=20)
    back_btn = tk.Button(window, text="Back", width=10, height=1, bg="light blue", fg="black",
                         font=("Arial", 12, "bold"))
    back_btn.pack()
    window.mainloop()

