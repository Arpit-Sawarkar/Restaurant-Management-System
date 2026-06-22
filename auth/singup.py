from dashboard.dashboard import open_dashboard
from database.queries import check_user
from database.queries import insert_user
from tkinter import messagebox
import tkinter as tk
def open_signup():
    window = tk.Tk()
    window.geometry("400x600")
    window.title("Sign Up")
    window.configure(background="#f0f0f0")
    window.resizable(False, False)
    tk.Label(window, text="Sign Up", font=("Times new roman", 18, "bold")).pack(pady=30)
    name = tk.Label(window, text="Enter Full Name", font=("Arial", 12))
    name.pack()
    name_entry = tk.Entry(window, font=("Arial", 12), )
    name_entry.pack(pady=10)
    email = tk.Label(window, text="Enter Email", font=("Arial", 12))
    email.pack()
    email_entry = tk.Entry(window, font=(" Arial", 12))
    email_entry.pack(pady=10)
    contact = tk.Label(window, text="Enter Contact", font=("Arial", 12))
    contact.pack()
    contact_entry = tk.Entry(window, font=("Arial", 12))
    contact_entry.pack(pady=10)
    city = tk.Label(window, text="Enter City", font=("Arial", 12))
    city.pack()
    city_entry = tk.Entry(window, font=("Arial", 12))
    city_entry.pack(pady=10)
    password = tk.Label(window, text="Enter Password", font=("Arial", 12), )
    password.pack()
    password_entry = tk.Entry(window, font=("Arial", 12), show="*")
    password_entry.pack(pady=10)
    conformpass = tk.Label(window, text="Conform Password", font=("Arial", 12))
    conformpass.pack()
    conformpass_entry = tk.Entry(window, font=("Arial", 12), show="*")
    conformpass_entry.pack(pady=10)

    # Signup connection
    def signup():
        name = name_entry.get()
        email = email_entry.get()
        contact = contact_entry.get()
        city = city_entry.get()
        password = password_entry.get()
        conform = conformpass_entry.get()

        existing_user = check_user(contact)
        if existing_user:
            messagebox.showwarning("Already Registered", "You are Already Registered. Please Login")
            window.destroy()
            from auth.login import open_login
            open_login()
            return

        if (name == "" or
                email == "" or
                contact == "" or
                city == "" or
                password == "" or
                conform == ""):
            messagebox.showerror("Error", "All Fields Requried")
            return
        if password != conform:
            messagebox.showerror("Error", "Password not match")
            return
        if not contact.isdigit():
            messagebox.showerror("Error","Contact must cantain only number")
            return
        if len(contact) !=10:
            messagebox.showerror("error","Contact must be exactly 10 digits")
            return
        insert_user(name, email, contact, city, password)
        messagebox.showinfo("Success", "Signup Successfully")
        window.destroy()
        open_dashboard()

    # Button
    signup_btn = tk.Button(window, text="Sign Up", font=("Arial", 12, "bold"), bg="blue", fg="white", width=10,
                           height=1, command=signup)
    signup_btn.pack(pady=10)
    back_btn = tk.Button(window, text="Back", font=("Arial", 12, "bold"), bg="light blue", fg="black", width=10,
                         height=1)
    back_btn.pack(pady=10)
    window.mainloop()

