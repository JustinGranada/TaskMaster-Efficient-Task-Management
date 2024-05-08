from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Task.db")
root = Tk()
root.title("TaskMaster-Efficient-Task-Management")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

title = StringVar()
description = StringVar()
deadline = StringVar()
priority = StringVar()
completed = StringVar()


# Entries Frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
titles = Label(entries_frame, text="TaskMaster-Efficient-Task-Management", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
titles.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

lbltitle = Label(entries_frame, text="Title", font=("Calibri", 16), bg="#535c68", fg="white")
lbltitle.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txttitle = Entry(entries_frame, textvariable=title, font=("Calibri", 16), width=30)
txttitle.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lbldescription = Label(entries_frame, text="Description", font=("Calibri", 16), bg="#535c68", fg="white")
lbldescription.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtdescription = Entry(entries_frame, textvariable=description, font=("Calibri", 16), width=30)
txtdescription.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lbldeadline = Label(entries_frame, text="Deadline", font=("Calibri", 16), bg="#535c68", fg="white")
lbldeadline.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtdeadline = Entry(entries_frame, textvariable=deadline, font=("Calibri", 16), width=30)
txtdeadline.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblpriority = Label(entries_frame, text="Priority", font=("Calibri", 16), bg="#535c68", fg="white")
lblpriority.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtpriority = Entry(entries_frame, textvariable=priority, font=("Calibri", 16), width=30)
txtpriority.grid(row=2, column=3, padx=10, pady=10, sticky="w")



lblcompleted = Label(entries_frame, text="Completed", font=("Calibri", 16), bg="#535c68", fg="white")
lblcompleted.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtcompleted = Entry(entries_frame, textvariable=completed, font=("Calibri", 16), width=30)
txtcompleted.grid(row=3, column=3, padx=10, sticky="w")


def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    title.set(row[1])
    description.set(row[2])
    deadline.set(row[3])
    priority.set(row[4])
    completed.set(row[5])


def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_employee():
    if txttitle.get() == "" or txtdescription.get() == "" or txtdeadline.get() == "" or txtpriority.get() == "" or txtcompleted.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(txttitle.get(),txtdescription.get(), txtdeadline.get() , txtpriority.get() ,txtcompleted.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()



def update_employee():
    if txttitle.get() == "" or txtdescription.get() == "" or txtdeadline.get() == "" or txtpriority.get() == ""or txtcompleted.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txttitle.get(), txtdescription.get(), txtdeadline.get(), txtpriority.get(), txtcompleted.get())
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_employee():
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    txttitle.delete(0, END)
    txtdescription.delete(0, END)
    txtdeadline.delete(0, END)
    txtpriority.delete(0, END)
    txtcompleted.delete(0, END)

btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Title")
tv.heading("3", text="Description")
tv.column("3", width=5)
tv.heading("4", text="Deadline")
tv.column("4", width=10)
tv.heading("5", text="Priority")
tv.heading("6", text="Completed")
tv.column("6", width=10)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)


dispalyAll()
root.mainloop()