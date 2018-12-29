from Tkinter import *
import os
from PIL import ImageTk,Image
import time

creds = 'tempfile.temp' 

def Signup(): 
    global pwordE 
    global nameE
    global roots
 
    roots = Tk()
    roots.title('Signup')
    roots.configure(background = 'RoyalBlue4')
    roots.geometry('450x200')
    intruction = Label(roots, text='Please Enter New Credidentials\n', font=("Arial Bold", 21), fg = 'IndianRed1', bg ='RoyalBlue4')
    intruction.grid(row=0, column=0, sticky=E) 
 
    nameL = Label(roots, text='New Username: ', font=("Arial Bold", 14), fg = 'black', bg ='RoyalBlue4') 
    pwordL = Label(roots, text='New Password: ', font=("Arial Bold", 14), fg = 'black', bg ='RoyalBlue4') 
    nameL.grid(row=1, column=0, sticky=W) 
    pwordL.grid(row=2, column=0, sticky=W) 
 
    nameE = Entry(roots, bg='white') 
    pwordE = Entry(roots, show='*')
    nameE.grid(row=1, column=0) 
    pwordE.grid(row=2, column=0) 
 
    signupButton = Button(roots, text = 'Signup', font = ("Arial Bold", 14), bg = 'gray', fg = 'black', command = FSSignup)
    signupButton.place(x= 180, y = 150)
    roots.mainloop()
 
def FSSignup():
    with open(creds, 'w') as f: 
        f.write(nameE.get()) 
        f.write('\n') 
        f.write(pwordE.get())
        f.close() 
 
    roots.destroy()
    Login() 
 
def Login():
    global nameEL
    global pwordEL 
    global rootA
 
    rootA = Tk() 
    rootA.title('Login')
    rootA.configure(background = 'RoyalBlue4')
    rootA.geometry('430x250')
    intruction = Label(rootA, text='User Login\n', font = ("Arial Bold", 18), bg = 'RoyalBlue4', fg = 'IndianRed1') 
    intruction.grid(row = 0, column = 1, sticky=E) 
 
    nameL = Label(rootA, text='Username: ', font = ("Arial Bold", 14), bg = 'RoyalBlue4', fg = 'white') 
    pwordL = Label(rootA, text='Password: ', font = ("Arial Bold", 14), bg = 'RoyalBlue4', fg = 'white') 
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) 
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='     Login      ', font = ("Arial Bold", 14), bg = 'gray', fg = 'black',command=CheckLogin) 
    loginB.place(x = 113, y = 140)
 
    rmuser = Button(rootA, text='Delete User',font = ("Arial Bold", 14), bg = 'gray', fg='red', command=DelUser) 
    rmuser.place(x = 113, y = 190)
    rootA.mainloop()
 
def CheckLogin():
    with open(creds) as f:
        data = f.readlines() 
        uname = data[0].rstrip() 
        pword = data[1].rstrip()
 
    if nameEL.get() == uname and pwordEL.get() == pword:
        rootA.destroy()
    else:
        rootA.destroy()
        r = Tk()
        r.title('D:')
        r.configure(background = 'Khaki')
        r.geometry('250x100')
        rlbl = Label(r, text='\n!!!Invalid Login !!!', font = ("Arial Bold", 20), bg = 'Khaki', fg='red')
        rlbl.pack()
        r.destroy()
        Login()
 
def DelUser():
    os.remove(creds) 
    rootA.destroy() 
    Signup() 
 
if os.path.isfile(creds):
    Login()
else: 
    Signup()
