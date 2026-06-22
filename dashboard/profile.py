import tkinter as  tk
from database.queries import update_login_status
import session
def open_profile(dashboard_window):
    window = tk.Tk()
    window.title("My Profile")
    window.geometry("350x440")
    window.geometry("+1000+80")
    window.resizable(0, 0)
    window.configure(bg="#f0f0f0")
    user=session.current_user
    title = tk.Label(window, text="My Profile", font=("Arial", 15, "bold"), bg="#f0f0f0")
    title.pack(pady=(15,0))
    icon = tk.Label(window, text="👤", font=("Arial", 100), bg="#f0f0f0")
    icon.pack()
    name=tk.Label(window,text=f"Name : {user[0]}",font=("Arial",15))
    name.pack(pady=5)
    email=tk.Label(window,text=f"Email : {user[1]}",font=("Arial",15))
    email.pack(pady=5)
    contact=tk.Label(window,text=f"Contact : {user[2]}",font=("Arial",15))
    contact.pack(pady=5)
    city=tk.Label(window,text=f"City : {user[3]}",font=("Arial",15))
    city.pack(pady=5)

    def back():
        window.destroy()

    def logout():
        update_login_status(session.current_user[2],0)
        session.current_user=None
        dashboard_window.destroy()
        window.destroy()
        from main import open_main
        open_main()

    btn_frame = tk.Frame(window, bg="#f0f0f0")
    btn_frame.pack(pady=20)
    back_btn = tk.Button(btn_frame,text="Back",font=("Arial", 12, "bold"),width=10,bg="light blue",command=back)
    back_btn.grid(row=0, column=0, padx=10)
    logout_btn = tk.Button(btn_frame,text="Logout",font=("Arial", 12, "bold"),width=10,bg="orange",command=logout)
    logout_btn.grid(row=0, column=1, padx=10)

    window.mainloop()
