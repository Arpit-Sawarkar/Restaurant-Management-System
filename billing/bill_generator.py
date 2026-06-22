from datetime import datetime
from tkinter import messagebox
current_date = datetime.now().strftime("%d - %m - %Y")
current_time = datetime.now().strftime("%I : %M  %p")
bill_items=[]
#Add items
def add_item(purchase_entry, quantity_dropdown, cost_dropdown, bill_text):
    bill_text.config(state="normal")
    item = purchase_entry.get()
    qty = int(quantity_dropdown.get())
    cost = int(cost_dropdown.get())
    total = qty * cost
    bill_items.append([item, qty, cost, total])
    bill_text.insert("end",f"   {item:<12}   {qty:<10}  {cost:<10}    {total}\n")
    purchase_entry.delete(0, "end")
    bill_text.config(state="disabled")
#Generate bill
def generate_bill(bill_entry,name_entry,contact_entry,city_entry,date_entry,time_entry,table_dropdown,bill_text):
    bill_text.config(state="normal")
    bill_text.delete(1.0, "end")
    bill_no = bill_entry.get()
    name = name_entry.get()
    contact = contact_entry.get()
    city = city_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    table = table_dropdown.get()
    bill_text.tag_config("title", font=("Courier New", 13, "bold"), justify="center")  # Title Style
    bill_text.tag_config("address", font=("Courier New", 12))   # Address Style
    bill_text.tag_config("total", font=("Courier New", 12, "bold"))  # Total Style
    bill_text.insert("end", "\n", "title")
    bill_text.insert("end", "Shivshahi Family Restaurant & Bar \n", "title")
    bill_text.insert("end", "               Ring road, Amravati, Maharashtra 444605\n", "address")
    bill_text.insert("end", "        ------------------------------------------------------------\n\n")
    bill_text.insert("end", f"   Bill No   :   {bill_no}\n")
    bill_text.insert("end", f"   Customer  :   {name}\n")
    bill_text.insert("end", f"   Contact   :   {contact}\n")
    bill_text.insert("end", f"   City      :   {city}\n")
    bill_text.insert("end", f"   Date      : {date}\n")
    bill_text.insert("end", f"   Time      : {time}\n")
    bill_text.insert("end", f"   Table No  :   {table}\n\n")
    bill_text.insert("end","   ---------------------------------------------\n")
    bill_text.insert("end", "   Item          Qty         Cost         Total\n")
    bill_text.insert("end","   ---------------------------------------------\n")
    bill_text.config(state="disabled")
#Calculate Total
def calculate_total(bill_text):
    bill_text.config(state="normal")
    subtotal = 0
    for item in bill_items:
        subtotal += item[3]
    gst = subtotal * 0.05
    grand_total = subtotal + gst
    bill_text.insert("end","   ---------------------------------------------\n")
    bill_text.insert("end",f"   GST (5%)                            {gst:.2f}\n","total")
    bill_text.insert("end",f"   Grand Total                         {grand_total:.2f}\n","total")
    bill_text.insert("end",                                    "\nThank You Visit Again!\n","title")
    bill_text.config(state="disabled")
    return grand_total
def get_grand_total():
    subtotal = 0
    for item in bill_items:
        subtotal += item[3]
    gst = subtotal * 0.05
    grand_total = subtotal + gst
    return grand_total
#Clear Bill
def clear_bill(name_entry,contact_entry,city_entry,purchase_entry,quantity_dropdown,cost_dropdown,table_dropdown,bill_text):
    bill_text.config(state="normal")
    bill_items.clear()
    name_entry.delete(0, "end")
    contact_entry.delete(0, "end")
    city_entry.delete(0, "end")
    purchase_entry.delete(0, "end")
    quantity_dropdown.current(0)
    cost_dropdown.current(0)
    table_dropdown.current(0)
    bill_text.delete(1.0, "end")
    bill_text.config(state="disabled")
#Exit button
def exit_app(window):
    result = messagebox.askyesno("Exit","Are you sure you want to exit?")
    if result:
        window.destroy()
