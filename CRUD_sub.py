
import tkinter as tk
from tkinter import messagebox
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hari@123",
    database="myshop_database"
)
cursor = db.cursor()


def add_data():
    name = entry_name.get()
    if name:
        cursor.execute("INSERT INTO subjects (name) VALUES (%s)", (name,))
        db.commit()
        messagebox.showinfo("Success", "Data added successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please provide  name")

def delete_data():
    id = entry_id.get()
    if id:
        cursor.execute("DELETE FROM subjects WHERE id = %s", (id,))
        db.commit()
        messagebox.showinfo("Success", "Data deleted successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please provide an ID")

def modify_data():
    id = entry_id.get()
    name = entry_name.get()
    if id and name:
        cursor.execute("UPDATE subjects SET name = %s WHERE id = %s", (name, id))
        db.commit()
        messagebox.showinfo("Success", "Data updated successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please provide ID, name")

def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)


root = tk.Tk()
root.title("Database GUI")


tk.Label(root, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

tk.Label(root, text="Name").grid(row=1, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)


btn_add = tk.Button(root, text="Add", command=add_data)
btn_add.grid(row=3, column=0)

btn_delete = tk.Button(root, text="Delete", command=delete_data)
btn_delete.grid(row=3, column=1)

btn_modify = tk.Button(root, text="Modify", command=modify_data)
btn_modify.grid(row=3, column=2)

root.mainloop()


db.close()
