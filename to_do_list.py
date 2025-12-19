#AUTHOR:-PARMAR HARDIK
#If you like this project, feel free to star the repository!

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


#ADD TASK		
def add_task():
    task=entry.get()
    if task.strip()!="":
        field.insert(tk.END,f"-{task}")
        entry.delete(0,tk.END)
        field.yview(tk.END)
    else:
        messagebox.showwarning("input error","Please Enter a Task")

#DELETE TASK
def delete_task():
	try:
		selecte_index=field.curselection()[0]
		task=field.get(selecte_index)
		confirm=messagebox.askyesno("Delete",f"Delete task{task}")
		if confirm:
			field.delete(selecte_index)
	except IndexError:
				messagebox.showwarning("Select"," Please select task to delete")

#SAVE FILE
def save_file():
    file_path = filedialog.asksaveasfilename(
		defaultextension=".txt",
		filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
	)	
    if file_path:
        with open(file_path,"w") as file:
            for i in range(field.size()):
                item = field.get(i)
                file.write(item+"\n")      
#open file
def open_file():
    opn_file= filedialog.askopenfilename(
        title="SELECT A FILE",
        filetypes=[("Text files","*.txt"),("All files","*.")]
	)					
    if opn_file:
        with open(opn_file,"r") as file :
            content = file.read()
            field.delete(0,tk.END)
            for line in content.splitlines():
                field.insert(tk.END,f"{line}")
    else:
        messagebox.askyesno("select","Please select file")
    
#close file 
def close_file():
    confirm1 = messagebox.askyesno("CLOSE","DO YOU WANT TO CLOSE FILE ?")
    if confirm1:
        field.delete(0,tk.END)

#GUI MAIN WINDOW 	
root = tk.Tk()
root.configure(bg="black")
root.title("TO-DO APP")
#lable
lable=tk.Label(root,text="     ENTER YOUR TASKS      ",bg="black",fg="white",font=("Monospace" ,20, "bold"))
lable.pack(pady=10)

#text  and save field
save_frame=tk.Frame(root,bg="black")
save_frame.pack(padx=0)

entry=tk.Entry(save_frame,font=("Monospace" ,15),width=30)
entry.grid(row=0, column=0,pady=5,padx=5)

save_button=tk.Button(save_frame,text="SAVE FILE" , command=save_file, bg="#F79B12",width=10)
save_button.grid(row=0, column=1, padx=5)


#main fram for list and option field
edit_frame=tk.Frame(root,bg="black")
edit_frame.pack(padx=0)

#task list field
field=tk.Listbox(edit_frame,width=30,bg="#F7F7F7",font=("Monospace" ,15, "bold"))
field.grid(row=0,column=0,pady=0,padx=0)

#scroll
scrollbar=tk.Scrollbar(edit_frame)
scrollbar.grid(row=0, column=1,sticky="ns")

field.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=field.yview)

#buttons
opt_frame=tk.Frame(edit_frame,bg="black")
opt_frame.grid(row=0,column=2,pady=0,padx=0)

#options
label1 = tk.Label(opt_frame,text="OPTIONS",bg="BLACK",fg="GREEN",font=("monospace",15,"bold"))
label1.grid(row=0,column=0,padx=5)

add_button=tk.Button(opt_frame,text="Add Task", command=add_task ,width=10 , fg="black" ,bg="#1EF125")
add_button.grid(row=1, column=0, padx=5)

dlt_button=tk.Button(opt_frame,text="Delete", command=delete_task ,fg="black",width=10, bg="#E40E0E")
dlt_button.grid(row=2, column=0, padx=5)

open_button=tk.Button(opt_frame, text="OPEN FILE", command=open_file, bg="blue",fg="black",width=10)
open_button.grid(row=3, column=0, padx=5)

close_button=tk.Button(opt_frame, text="CLOSE FILE", command=close_file, bg="yellow",fg="black",width=10)
close_button.grid(row=4, column=0, padx=5)

#key binding

#add task
def enter_key(event):
    add_task()
root.bind("<Return>",enter_key)

#save task
def ctr_key(event):
    save_file()    
root.bind("<Control-s>",ctr_key)

#open task
def ctr2_key(event):
    open_file()    
root.bind("<Control-o>",ctr2_key)

#delete task
def delete_key(event):
    delete_task()    
root.bind("<Delete>",delete_key)

root.mainloop()