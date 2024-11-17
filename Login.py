from customtkinter import *
from PIL import Image
from tkinter import messagebox
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif usernameEntry.get()=='Ram' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Wrong credentials')

root = CTk()
set_appearance_mode("light")
root.geometry('1000x667')
root.resizable(0,0)
root.title('Login Page')

image = CTkImage(Image.open('cover.jpg'),size=(1000,667))
imageLabel = CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)

headinglabel = CTkLabel(root,text='Employee Management System',font=('Goudy Old Style',20,'bold'),text_color='dark blue',bg_color='#F1F4FB')
headinglabel.grid(row=0, column=0, padx=370,pady=(300,30))

usernameEntry = CTkEntry(root,placeholder_text='Enter Your Username',width=180)
usernameEntry.grid(row=1, column=0,pady=(0,20))

passwordEntry = CTkEntry(root,placeholder_text='Enter Your Password',width=180,show='*')
passwordEntry.grid(row=2, column=0,pady=(0,20))

loginButton = CTkButton(root,text='Login',cursor='hand2',command=login)
loginButton.grid(row=3, column=0,pady=(0,20))

root.mainloop()