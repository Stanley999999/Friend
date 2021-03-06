import lib
import tkinter as tk
from tkinter import messagebox

friends_db = 'friends_db'

def check():
    index = friends_list.curselection()[0]
    name = friends_list.get(index)
    print(name)
    messagebox.showinfo(title='friend info', message='%s: phone: %s, age: %s' % (name, friends_info[name]['phone'], friends_info[name]['age']))

def remove():
    # How to manage the GUI actions
    index = friends_list.curselection()[0]
    name = friends_list.get(index)

    friends_list.delete(index)
    # How to manage the DB
    lib.delete_friend(friends_info, name)
    lib.process_write(friends_db, friends_info)

def add():
    # Create the window (TopLevel)
    add_box = Toplevel()
    add_box.title('Adding friends...')
    add_box.geometry('300x300+300+300')
    
    row_name = Frame(add_box)
    row_name.pack(fill='x')
    Label(row_name, text='Name: ', width=8).pack(side=LEFT)
    f_name = StringVar()
    Entry(row_name, textvariable=f_name, width=20).pack(side=LEFT)

    row_phone = Frame(add_box)
    row_phone.pack(fill='x')
    Label(row_phone, text='Phone: ', width=8).pack(side=LEFT)
    f_phone = StringVar()
    Entry(row_phone, textvariable=f_phone, width=20).pack(side=LEFT)
    
    row_age = Frame(add_box)
    row_age.pack(fill='x')
    Label(row_age, text='Age: ', width=8).pack(side=LEFT)
    f_age = StringVar()
    Entry(row_age, textvariable=f_age, width=20).pack(side=LEFT)
    
    row_btn = Frame(add_box)
    row_btn.pack(fill='x')
    Button(add_box, text='Add', command=lambda: add_confirm(add_box, f_name.get(), f_phone.get(), f_age.get())).pack(side=LEFT)
    Button(add_box, text='Cancel', command=lambda: cancel(add_box)).pack(side=LEFT)
    # Manage the DB

def cancel(box):
    box.destroy()

def add_confirm(box, name, phone, age):
    lib.add(friends_info, name, phone, age)
    lib.process_write(friends_db, friends_info)
    # Refresh the listbox
    name_list = lib.list_friends(friends_info)
    print(name_list)
    friends_list.delete(0, END)
    for item in name_list:
        friends_list.insert(END, item)
    # Close the window
    box.destroy()

def edit():
    # Create a toplevel window
    pass
    # manage the DB

window = Tk()
window.title('Friends Management System')

label = Label(window, text='Friends are here')
friends_list = Listbox(window)
add_button = Button(window, text='Add', command=add)
remove_button = Button(window, text='Remove', command=remove)
edit_button = Button(window, text='Edit')
check_button = Button(window, text='Check', command=check)

label.pack()
friends_list.pack()
add_button.pack(side=LEFT)
remove_button.pack(side=LEFT)
edit_button.pack(side=LEFT)
check_button.pack(side=LEFT)


# Func1: Display friends in listbox
friends_info = lib.process_read(friends_db)
name_list = lib.list_friends(friends_info)
print(name_list)
for item in name_list:
    friends_list.insert(END, item)
# Func2: for every button 
# Check function
# How to get the info of selected friend
print(friends_list.curselection())

window.mainloop()
