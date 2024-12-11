import tkinter as tk
import csv
from replit import clear


root = tk.Tk()
root.geometry("250x250")
frame1=tk.Frame(root,width=200,height=200)
frame1.grid(row=0,column=0)
def write1(k,n):
    with open("BEGINNER_PROJECTS/TO_DO_LIST_tkinter/storage.csv","a",newline='') as f:
        c = csv.writer(f)
        c.writerow([k,n])
    

root.title('TO DO LIST')

def input_task():
    for widgets in frame1.winfo_children():
        widgets.destroy()
    
     
    tk.Label(frame1,text="input the task").grid(row=0,column=0)
    e1=tk.Entry(frame1)
    e1.grid(row=0,column=1)
    tk.Label(frame1,text="input  the deadline").grid(row=1,column=0)
    e2=tk.Entry(frame1)
    e2.grid(row=1,column=1)
    button = tk.Button(frame1,text="confirm",command= lambda: write1(e1.get(),e2.get()))
    button.grid(row=2,column=1)
    button = tk.Button(frame1,text="go back to menu",command=clearall)
    button.grid(row=3,column=1)
    tk.Button(frame1,text="clear ",command=clearall).grid(row=4,column=1)
    
        

def see_task():
    
    #for widget in root.grid_slaves():
    #    if isinstance(widget, tk.Label) and widget.grid_info()['row'] >= 4:
    #        widget.destroy()
            
    try:
        with open("BEGINNER_PROJECTS/TO_DO_LIST_tkinter/storage.csv", "r") as f:
            c = csv.reader(f)
            tk.Label(frame1, text="Task", font=('Arial', 10, 'bold')).grid(row=4, column=0)
            tk.Label(frame1, text="Deadline", font=('Arial', 10, 'bold')).grid(row=4, column=1)
            
            for row_num, row in enumerate(c, start=5):
                if len(row) >= 2:  
                    tk.Label(frame1, text=row[0]).grid(row=row_num, column=0)  # Task
                    tk.Label(frame1, text=row[1]).grid(row=row_num, column=1)  # Deadline
                    
        
        tk.Button(frame1, text="Back to Menu", command=clearall).grid(row=3, column=0)
        tk.Button(frame1,text="clear ",command=clearall).grid(row=4,column=0)
                    
    except FileNotFoundError:
        tk.Label(frame1, text="No tasks found!").grid(row=4, column=0)


def clearall():
    for widgets in frame1.winfo_children():
        widgets.destroy()
    menu()


def menu():
    
    button = tk.Button(frame1,text="input",command=input_task)
    button.grid(row=0,column=0)
    button1 = tk.Button(frame1,text="show",command=see_task)
    button1.grid(column=0,row=1)

menu()

root.mainloop()

