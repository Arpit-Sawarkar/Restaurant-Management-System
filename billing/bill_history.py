import tkinter as tk
from tkinter import ttk
from database.db_connection import get_connection
def open_bill_history():
    history_window = tk.Toplevel()
    history_window.title("Bill History")
    history_window.geometry("1000x400")
    heading = tk.Label(history_window,text="Billing History",font=("Arial", 20, "bold"),fg="black")
    heading.pack(pady=(0,10))
    history_window.resizable(width=False, height=False)
    scrollbar = tk.Scrollbar(history_window, orient="vertical")
    tree = ttk.Treeview(history_window,yscrollcommand=scrollbar.set)
    style = ttk.Style()
    style.configure("Treeview.Heading",font=("Arial", 10, "bold"))
    scrollbar.config(command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.pack(fill="both", expand=True)
    tree["columns"] = ("Bill No","Customer","Contact","City","Date","Time","Table No","Total")
    tree.column("#0", width=0, stretch=False)
    for col in tree["columns"]:
        tree.column(col, anchor="center", width=120)
        tree.heading(col, text=col)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM BILLS")
    records = cursor.fetchall()
    for row in records:
        tree.insert("", "end", values=row)
    cursor.close()
    conn.close()