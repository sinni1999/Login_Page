from tkinter import *
from tkinter import messagebox

from PIL import ImageTk,Image

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'sinnisharma1999@gmail.com' and password == '12345':
        messagebox.showinfo('Login','Login Sucessfully!!!')
    else:
        messagebox.showerror('Error','Login Failed')

root=Tk()
root.title("Login Page")

root.iconbitmap('fevicon.ico')
root.minsize(100,400)
root.maxsize(400,400)

root.geometry('500x500')
root.configure(background='#0096DC')
img = Image.open('logo.png')
resized_img = img.resize((40,40))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root,image=img)
img_label.pack(pady=(10,10))

text_label = Label(root,text='User Login',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',17))


email_label = Label(root,text='Enter Your Email' ,fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',11))

email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))


password_label = Label(root,text='Enter Your Password' ,fg='white',bg='#0096DC')
password_label.pack(pady=(20,3))
password_label.config(font=('verdana',11))

password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

login_btn = Button(root,text='Login' ,bg='white', fg='#0096DC',width=10, height=1,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',11))

root.mainloop()