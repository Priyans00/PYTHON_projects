from tkinter import *
from tkinter import messagebox 
import sqlite3

conn = sqlite3.connect("app_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS data(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               key TEXT,
               value TEXT)
""")
conn.commit()

root = Tk()

root.title('TO DO LIST')
root.geometry("420x500")
root.configure(bg = "lightgrey")


a=root.winfo_width()
b=root.winfo_height()


f1 = Frame(root,bg='black',height=400,width=400)
f1.place(anchor="center",relx=0.5,rely=0.65)

f2 = Frame(root,bg='black',width=300,height=70)
f2.place(anchor='center',relx=0.5,rely=0.15)

l2=Label(f2,text="TO DO LIST",bg='black',fg='yellow')
l2.place(anchor='center',relx=0.5,rely=0.5)



def insert1():
    insert = Tk()
    insert.title("Add Task")
    insert.geometry("300x200")

    fi1 = Frame(insert)
    fi1.place(anchor='center',relx=0.5,rely=0.5)

    Label(fi1, text="Enter the task:").pack()
    ei1 = Entry(fi1)
    ei1.pack()
    
    Label(fi1, text="Enter the deadline:").pack()
    ei2 = Entry(fi1)
    ei2.pack()

    def add():
        key = ei1.get()
        value = ei2.get()

        if key and value:
            try:
                cursor.execute("insert into data (key,value) values (?,?)",(key,value))
                conn.commit()
                messagebox.showinfo("Success","Data saved successfully!")
                insert.destroy()
            except Exception as e:
                messagebox.showerror("Error",f"An error occurred: {str(e)}")
        else:
            messagebox.showwarning("Warning","Please fill in both fields")

    bi1 = Button(fi1, text="Submit", command=add)
    bi1.pack(pady=10)

    insert.mainloop()

def show():
    show = Toplevel(root)

    fs1 = Frame(show)
    fs1.place(anchor = 'center',relx=0.5,rely=0.5)

    cursor.execute('select * from data')
    result = cursor.fetchall()
    conn.commit()

    k=len(result)
    newh = max(100,k*20)
    show.geometry(f"500x{newh}")
    for i in range(len(result)):
        label = Label(fs1, text=f"s.no = {result[i][0]}, task = {result[i][1]}, deadline = {result[i][2]}")
        label.grid(row=i, column=0)

    def dest():
        show.destroy()

    b1 = Button(fs1, text="return to main menu", command=dest)
    b1.grid(row=5, column=10)
    show.mainloop()

def delit():
    delit = Toplevel(root)
    delit.title("Delete Task")
    delit.geometry("400x400")
    
    fd = Frame(delit)
    fd.pack(pady=20)
    
    cursor.execute('select * from data')
    result = cursor.fetchall()
    
    Label(fd, text="Current Tasks:", font=('Arial', 10, 'bold')).pack(pady=5)
    for row in result:
        Label(fd, text=f"S.No {row[0]}: {row[1]} (Deadline: {row[2]})").pack()
    
    Label(fd, text="\nEnter the S.No of the task to delete:", font=('Arial', 10)).pack(pady=5)
    ed1 = Entry(fd)
    ed1.pack(pady=5)

    def dell():
        sno = ed1.get()
        if sno:
            try:
                cursor.execute("delete from data where id = ?", (sno,))
                conn.commit()
                messagebox.showinfo("Success", "Removed successfully")
                delit.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showerror("Error", "Please enter a valid S.No")

    bd1 = Button(fd, text="Delete", command=dell)
    bd1.pack(pady=10)

b1 = Button(f1,text = "enter a task",height=2,width=15,bg="blue",fg="yellow",padx=5,borderwidth=0.5,command=insert1)
b1.place(anchor='w',relx=0,rely=0.25)

b2 = Button(f1,text="see the tasks",height=2,width=15,bg="blue",fg="yellow",padx=5,borderwidth=5,command=show)
b2.place(anchor='w',relx=0,rely=0.5)    

b3 = Button(f1,text="delete task",height=2,width=15,bg="blue",fg="yellow",padx=5,borderwidth=5,command=delit)
b3.place(anchor='center',relx=0.5,rely=0.5)   


root.mainloop()