from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_my_password():
    a=random.randint(8,10)
    b=random.randint(1,3)
    c=random.randint(1,2)
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    number=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','@','#','$','%','^','&','*','(',')','+']
    l=[alphabet,number,symbols]

    password_list=[]
    for char in range(1,a+1):
        password_list.append(random.choice(alphabet))
    for char in range(1,b+1):
        password_list.append(random.choice(number))
    for char in range(1,c+1):
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    password="".join(password_list)
    Password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_text():
    w=website_input.get()
    e=Email_input.get()
    p=Password_input.get()

    if w=="" or e=="" or p=="":
        messagebox.showinfo(message="Please don't leave any field empty")
    else:
        isok=messagebox.askokcancel(title=w,message=f"There are the details entered:\nEmail:{e}\nPassword:{p}\nIs it ok to save?")
        if isok:
            f=open("data.txt","a")
            f.write(f"{w} | {e} | {p}\n")
            f.close()
            website_input.delete(0,END)
            Password_input.delete(0,END)
            Email_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# window.minsize(height=240,width=240)
window.config(padx=20,pady=20)

canvas=Canvas(width=200,height=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=0,row=0,columnspan=3)


website=Label(text="Website:")
website.grid(column=0,row=1)

website_input=Entry(width=41)
website_input.grid(column=1,row=1,columnspan=2)
website.focus()

Email = Label(text="Email/Username:")
Email.grid(column=0, row=2)

Email_input = Entry(width=41)
Email_input.grid(column=1, row=2, columnspan=2)
# Email_input.insert()


Password = Label(text="Password:")
Password.grid(column=0, row=3)

Password_input = Entry(width=20)
Password_input.grid(column=1, row=3)

generate_password=Button(text="Generate Password", width=16, command=generate_my_password)
generate_password.grid(column=2, row=3)

Add=Button(text="Add", width=34, command=write_text)
Add.grid(column=1, row=4, columnspan=2)

window.mainloop()
