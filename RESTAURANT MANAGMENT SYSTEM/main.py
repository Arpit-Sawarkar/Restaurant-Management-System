import tkinter as tk
import session
from auth.login import open_login
from auth.singup import open_signup
from dashboard.dashboard import open_dashboard
from database.queries import get_logged_in_user
def open_main():
    window = tk.Tk()
    window.title("RESTAURANT MANAGMENT SYSTEM")
    window.geometry("1000x600")
    window.resizable(False, False)
    label = tk.Label(window, text="RESTAURANT MANAGEMENT SYSTEM", font=("Times new Roman", 20, "bold"))
    label.pack(ipady=60)
    frame = tk.Frame(window, relief="solid", width=500, height=450)
    frame.pack_propagate(False)
    frame.pack(pady=50)
    def login():
        print("Login page open")
        window.destroy()
        open_login()
    loginbtn = tk.Button(frame, text="Login", width=10, height=1, bg="blue", fg="white", font=("Arial", 15, "bold"),command=login)
    loginbtn.pack(pady=(60, 10))
    def signup():
        print("Signup page open")
        window.destroy()
        open_signup()
    singupbtn = tk.Button(frame, text="Sing up", width=10, height=1, bg="blue", fg="white", font=("Arial", 15, "bold"),command=signup)
    singupbtn.pack(pady=(20, 10))
    window.mainloop()
if __name__ == "__main__":
    user = get_logged_in_user()
    if user:
        session.current_user = user
        open_dashboard()
    else:
        open_main()
