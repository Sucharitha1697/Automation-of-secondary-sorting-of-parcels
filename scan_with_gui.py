from pymongo import MongoClient
import scan_modified as sm
import password_gui as pw
import serial
import time
client= MongoClient('localhost:27017')
db= client.data
from Tkinter import *

def insert():
     global root1
     global barcode
     global weight
     global height
     global length
     global breadth
     global pin
     global payment
     global price
     root1 = Tk()
     root1.attributes('-fullscreen',True)
     root1.title("") 
     root1.configure(background = 'navy blue')
     label = Label(root1, text="Welcome to Parcel Sorting Main Menu", font=("Arial Bold", 32), fg = 'Red', bg= 'navy blue')
     label.pack()
     Button1 = Button(root1, text = 'Insert   ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = insert)
     Button1.place(x=50, y = 90)
     Button2 = Button(root1, text = 'Update ',font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = update)
     Button2.place(x=50, y = 190)
     Button3 = Button(root1, text = '  Read  ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = read)
     Button3.place(x=50, y = 290)
     Button4 = Button(root1, text = ' Delete ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = delete)
     Button4.place(x=50, y = 390)
     Button6 = Button(root1, text = '    Quit  ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = quite)
     Button6.place(x=50, y = 490) 
 
     barcode = Label(root1, text='Barcode: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue') 
     weight = Label(root1, text='Weight: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue') 
     height = Label(root1, text='Height: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue') 
     length = Label(root1, text='Length: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue')
     breadth = Label(root1, text='Breadth: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue') 
     pin = Label(root1, text='Pin: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue')
     payment = Label(root1, text='Payment: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue')
     price = Label(root1, text='Price: ', font=("Arial Bold", 22), fg = 'black', bg ='sky blue')
     barcode.place(x=400 , y=90)   
     weight.place(x=900 , y=90)
     height.place(x=400 , y=250)   
     length.place(x=900 , y=250)
     breadth.place(x= 400, y=410)   
     pin.place(x= 900, y=410)
     payment.place(x=400 , y=570)
     price.place(x=900 , y=570) 
     barcode = Entry(root1, bg='white')
     weight = Entry(root1,bg='white')
     height = Entry(root1, bg='white') 
     length = Entry(root1, bg='white')
     breadth = Entry(root1, bg='white') 
     pin = Entry(root1, bg='white')
     payment = Entry(root1, bg='white')
     price = Entry(root1, bg='white')
     barcode.place(x=600, y=90) 
     weight.place(x=1100, y=90)
     height.place(x=600, y=270) 
     length.place(x=1100, y=270)
     breadth.place(x=600, y=420) 
     pin.place(x=1100, y=420)
     payment.place(x=600, y=580)
     price.place(x=1100, y=580)
     button = Button(root1, text = 'Submit', font = ("Arial Bold", 24), bg = 'bisque', fg = 'Blue',command = quete)
     button.place(x = 700, y = 650)
     root1.mainloop()

def quete():
     print(barcode.get())
     db.data.insert_one(
     {
     "barcode":barcode.get(),
     "weight":weight.get(),
     "height":height.get(),
     "length":length.get(),
     "breadth":breadth.get(),
     "pincode":pin.get(),
     "payment": payment.get(),
     "price" : price.get()
     })
     root1.destroy()

def disp():
     try:
          itemdata= db.data.find()
          for i in itemdata:
               print(i)
     except Exception,e:
          print str(e)

def read():
     bar = sm. _return_barcode(directory)
     itemdata = db.data.find({"barcode":bar})
     pincode  =  db.data.find({"barcode":bar},{"pincode":1})
     for j in pincode:
     	pin = j['pincode']
     print(pin)
     send_data(pin)

     for i in itemdata:
     	breadth_ans["text"] = i['breadth']
        weight_ans["text"] = i['weight']
        price_ans["text"] = i['price']
        barcode_ans["text"] = i['barcode']
        pin_ans["text"] = i['pincode']
        height_ans["text"] = i['height']
        length_ans["text"] = i['length']
        payment_ans["text"] = i['payment']
          

def quete1():
     root_read.destroy()
     
def delete():
     try:
          criteria = input('\n Enter item barcode to delete\n')
          db.data.delete_many({"barcode":criteria})
          print ('\nDeletion successful\n')
     except Exception,e:
          print str(e)

def quite():
     root.destroy()

def update():
     try:
          criteria = input('\nenter barcode to update\n')
          wt= input('\n Enter weight to update\n')
          db.data.update_one(
               {
               "barcode":criteria},
               {
               "$set":{
               "weight":wt
               }
               }
               )
          print ("\n REcords updated succesfully\n")
     except Exception,e:
          print str(e)
   
def send_data(pincode):	
     if pincode == "110035" :
          ser.write('a'.encode())
          print('A')
     if pincode == "600002" :
          ser.write('b'.encode())
          print('B')
     if pincode == "400099" :
          ser.write('c'.encode())
          print('C')
     if pincode == "382110" :
          ser.write('d'.encode())
          print('D')  

def main():
     global root
     global barcode_ans
     global weight_ans
     global height_ans
     global length_ans
     global breadth_ans
     global pin_ans
     global payment_ans
     global price_ans
     root = Tk()
     #root.attributes('-fullscreen',True)
     root.title("") 
     root.configure(background = 'navy blue')
     label = Label(root, text="Welcome to Parcel Sorting Main Menu", font=("Arial Bold", 32), fg = 'Red', bg= 'navy blue')
     label.pack()
     Button1 = Button(root, text = 'Insert   ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = insert)
     Button1.place(x=50, y = 90)
     Button2 = Button(root, text = 'Update ',font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = update)
     Button2.place(x=50, y = 190)
     Button3 = Button(root, text = '  Read  ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = read)
     Button3.place(x=50, y = 290)
     Button4 = Button(root, text = ' Delete ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = delete)
     Button4.place(x=50, y = 390)
     
     Button6 = Button(root, text = '    Quit  ', font = ("Arial Bold", 26), bg = 'orange', fg = 'Blue', command = quite)
     Button6.place(x=50, y = 490)

     barcode = Label(root, text='Barcode: ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     weight = Label(root, text='Weight: ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     height = Label(root, text='Height: ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     length = Label(root, text='Length: ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     breadth = Label(root, text='Breadth: ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     pin = Label(root, text='   Pin:    ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     payment = Label(root, text='Payment: ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     price = Label(root, text='  Price:   ', font=("Arial Bold", 26), fg = 'black', bg ='sky blue')
     barcode.place(x = 400, y= 90)
     weight.place(x = 900, y= 90)
     height.place(x = 400, y= 290)
     length.place(x = 900, y= 290)
     breadth.place(x = 400, y= 490)
     pin.place(x = 900, y= 490)
     payment.place(x = 400, y= 690)
     price.place(x = 900, y= 690)
     answers = ['barcode_ans', 'weight_ans', 'height_ans', 'length_ans', 'breadth_ans', 'pin_ans', 'payment_ans' , 'price_ans']
     barcode_ans = Label(root, text= '               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     weight_ans = Label(root, text= '               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     height_ans = Label(root, text='               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     length_ans = Label(root, text='               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     breadth_ans = Label(root, text='               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     pin_ans = Label(root, text='               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     payment_ans = Label(root, text='               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     price_ans = Label(root, text='               ', font=("Arial Bold", 26), fg = 'dark slate gray', bg ='white')
     barcode_ans.place(x = 600, y= 90)
     weight_ans.place(x = 1100, y= 90)
     height_ans.place(x = 600, y= 290)
     length_ans.place(x = 1100, y= 290)
     breadth_ans.place(x = 600, y= 490)
     pin_ans.place(x = 1100, y= 490)
     payment_ans.place(x = 600, y= 690)
     price_ans.place(x = 1100, y= 690)
     answers = [barcode_ans, weight_ans, height_ans, length_ans, breadth_ans, pin_ans, payment_ans , price_ans]
     root.mainloop()
ser = serial.Serial('COM14',9600)
directory = "C://Program Files (x86)//ZBar//bin//zbarcam.exe"

main()

