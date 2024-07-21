from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.title("Currency Converter")
root.iconbitmap("C:/Users/hp/Desktop/gui projects/7037893.ico")

def clear():
    converted_amount_Entry.delete(0,END)
    amount_entry.delete(0,END)

def lock():
    if not currency_entry.get() or not home_entry.get() or not rate_entry.get():
        messagebox.showwarning("Warning!", "Please enter all fields.")
    else:
        currency_entry.config(state="disabled")
        home_entry.config(state="disabled")
        rate_entry.config(state="disabled")
        my_notebook.tab(1,state="normal")

def unlock():
    currency_entry.config(state="normal")
    home_entry.config(state="normal")
    rate_entry.config(state="normal")
    my_notebook.tab(1, state="disabled")

def converter():
    sum = float(rate_entry.get())*float(amount_entry.get())
    converted_amount_Entry.insert(0,sum)


#Create Notebook
my_notebook = ttk.Notebook(root)
my_notebook.pack()


#Create Frames
currency_frame = Frame(my_notebook, width=480, height=480)
converter_frame = Frame(my_notebook, width=480, height=480)

currency_frame.pack()
converter_frame.pack()

#Create Tabs
my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(converter_frame, text="Converter")

#Notebook Disabled
my_notebook.tab(1, state="disabled")

# Currency Stuff

home=LabelFrame(currency_frame, text="Insert Currency Name")
home.config(font=("Helvetica", 14, "bold"))
home.pack(pady=10)

home_entry=Entry(home,font=("Helvetica", 24, "bold"))
home_entry.pack(padx=10, pady=10)

currency_convert = LabelFrame(currency_frame, text="Currency Name & Rate")
currency_convert.config(font=("Helvetica", 14, "bold"))
currency_convert.pack(pady=10)

currency_name = Label(currency_convert, text="Currency Name")
currency_name.config(font=("Helvetica", 14, "bold"))
currency_name.pack(pady=10)

currency_entry = Entry(currency_convert, font=('Helvetica', 24, "bold"))
currency_entry.pack(padx=10, pady=10)

rate_name = Label(currency_convert, text="Market Rate")
rate_name.config(font=("Helvetica", 14, "bold"))
rate_name.pack(pady=10)

rate_entry = Entry(currency_convert, font=('Helvetica', 24, "bold"))
rate_entry.pack(padx=10, pady=10)

my_button = Frame(currency_frame)
my_button.pack(pady=10)

#Create Buttons

lock_button = Button(my_button, text="Lock", command=lock)
lock_button.config(font=("Helvetica", 14, "bold"))
lock_button.grid(row=0,column=0)

unlock_button = Button(my_button, text="Unlock", command=unlock)
unlock_button.config(font=("Helvetica", 14, "bold"))
unlock_button.grid(row=0,column=1)

# Converter Stuff

amount=LabelFrame(converter_frame, text="Amount")
amount.config(font=("Helvetica", 14, "bold"))
amount.pack(pady=10)

amount_entry=Entry(amount,font=("Helvetica", 24, "bold"))
amount_entry.pack(padx=10, pady=10)

convert_button = Button(amount, text="Convert", command=converter)
convert_button.config(font=("Helvetica", 14, "bold"))
convert_button.pack()

converted_amount = LabelFrame(converter_frame, text="Total Amount")
converted_amount.config(font=("Helvetica",14,"bold"))
converted_amount.pack(pady=10)

converted_amount_Entry=Entry(converted_amount,font=("Helvetica",24,"bold"),bd=0,bg="systembuttonface")
converted_amount_Entry.pack(padx=10,pady=10)

clear_button = Button(converter_frame,text="Clear", command=clear)
clear_button.config(font=("Helvetica",14,"bold"))
clear_button.pack()

root.mainloop()

