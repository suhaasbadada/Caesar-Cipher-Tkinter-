import tkinter as tk

class MyWindow:
    def __init__(self, win):
        self.lbl1=tk.Label(win, text='String',background="white",font=('calibre',7,'normal'))
        self.lbl2=tk.Label(win, text='Shift',background="white",font=('calibre',7,'normal'))
        self.lbl3=tk.Label(win, text='Result',background="white",font=('calibre',7,'normal'))
        self.t1=tk.Entry(bd=3)
        self.t2=tk.Entry()
        self.t3=tk.Entry()
        self.btn1 =tk.Button(win, text='Encrypt')
        self.btn2=tk.Button(win, text='Subtract')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1=tk.Button(win, text='Encrypt', background='#28b463',command=self.encrypt)
        self.b2=tk.Button(win, text='Decrypt',background='#e74c3c')
        self.b2.bind('<Button-1>', self.decrypt)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
   
    def encrypt(self):
        self.t3.delete(0, 'end')
        s=(self.t1.get())
        k=int(self.t2.get())
        z=''
        for i in s:
            if i.isupper():
                z+=chr((ord(i)+k-65)%26+65)                
            else:
                z+=chr((ord(i)+k-97)%26+97)    
        result=z
        self.t3.insert(tk.END, str(result))
    def decrypt(self, event):
        self.t3.delete(0, 'end')
        s=(self.t1.get())
        k=int(self.t2.get())
        z=''
        for i in s:
            if i.isupper():
                z+=chr((ord(i)-k-65)%26+65)                
            else:
                z+=chr((ord(i)-k-97)%26+97)     
        result=z
        self.t3.insert(tk.END, str(result))

window=tk.Tk()
mywin=MyWindow(window)
window.title('Caesar Cipher')
window.geometry("400x300+10+10")
#ima=ImageTk.PhotoImage(Image.open("/home/vyper/Desktop/Caesar Cipher/ccimage.jpeg"))
#canvas=tk.Canvas(window,width=400,height=300)
#canvas.create_image(0,0,image=ima,anchor="nw")
#canvas.pack()
window.configure(background="black")

window.mainloop()