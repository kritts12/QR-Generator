import pyqrcode
import png
from pyqrcode import QRCode
import tkinter as tk
from tkinter import *

window = Tk()
window.geometry('400x450')
window.title('QR Generator')

label = Label(window, text='Let\'s Create QR Code', font=('arial', 15))
label.pack()

def create_qrcode():
    s1 = s.get()

    if s1.strip() == "":
        label2 = Label(window, text='Please enter some text to generate QR Code', fg='red', font=('arial', 10))
        label2.pack()
        return

    qr = pyqrcode.create(s1)

    qr.png('myqr.png', scale=6)

    global icon 
    icon = PhotoImage(file = 'myqr.png')

    label3 = Label(window, text='QR Code is created successfully', fg='green', font=('arial', 10))
    label3.pack()
    imglabel = Label(window, image=icon)
    imglabel.pack()

s = StringVar()

entry = Entry(window, textvariable=s, font=('arial', 15))
entry.pack()

button = Button(window, text='Create', bg='pink', command=create_qrcode)
button.pack()

window.mainloop()