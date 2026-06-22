def button_click(value,entry):
    current=entry.get()
    entry.delete(0,"end")
    entry.insert(0,current  +  str(value))

def calculate(entry):
    try:
        expression=entry.get()
        result = eval(entry.get())
        entry.delete(0,"end")
        entry.insert(0,f"{expression} = {result}")
    except:
        entry.delete(0,"end")
        entry.insert(0,"Error")
def clear(entry):
    entry.delete(0,"end")