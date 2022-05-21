from tkinter import *
import tkinter.font as font


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Kenar1')
        self.lbl2 = Label(win, text='Kenar2')
        self.lbl3 = Label(win, text='USD/TRY')
        self.lbl_nk = Label(win, text='NetKar(%)')
        self.lbl_nolight = Label(win, text='Işıksız Fiyat')
        self.lbl_light = Label(win, text='Işıklı Fiyat')
        self.lbl_rgb = Label(win, text='RGB Fiyat')
        self.t1 = Entry(bd=3)
        self.t2 = Entry()
        self.t3 = Entry()
        self.t_nk = Entry()
        self.t_nk.insert(0,20)
        # print(int(self.t1.get()))
        self.t4 = Entry()
        self.btn1 = Button(win, text='Fiyat Hesapla')
        self.btn2 = Button(win, text='Subtract')
        self.btn3 = Button(win, text="Multilication")
        self.btn4 = Button(win, text="Division")
        self.lbl1.place(x=20, y=20)
        self.t1.place(x=100, y=20)
        self.lbl2.place(x=20, y=60)
        self.t2.place(x=100, y=60)
        self.lbl3.place(x=20, y=100)
        self.t3.place(x=100, y=100)
        self.lbl_nk.place(x=20, y=140)
        self.t_nk.place(x=100, y=140)
        myFont = font.Font(family='Helvetica', size=20, weight='bold')
        self.b1 = Button(win, text='Fiyat Hesapla', fg='red', command=self.price_setter, height=5, width=20, font= myFont)
        self.b1.place(x=320, y=20)
        # self.b1.grid(column=1, row=0, columnspan=10, rowspan=10, sticky=W + E + N + S, padx=5, pady=5)
        # self.b1.bind('<Button-1>', self.price_setter)
        # self.b2 = Button(win, text='Subtract')
        # self.b2.bind('<Button-1>', self.sub)
        # self.b3 = Button(win, text="Multiplication")
        # self.b3.bind('<Button-1>', self.mul)
        # self.b4 = Button(win, text="Divisin")
        # self.b4.bind('<Button-1>', self.div)
        # self.b2.place(x=200, y=150)
        # self.b3.place(x=300, y=150)
        # self.b4.place(x=400, y=150)
        self.lbl1 = Label(win, text='Kenar1')
        self.lbl_nolight.place(x=100, y=200)
        self.t4.place(x=200, y=200)

    def price_setter(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def sub(self, event):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

    def mul(self, event):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def div(self, event):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 / num2
        self.t3.insert(END, str(result))


window = Tk()
mywin = MyWindow(window)
window.title('Etsy Fiyat Algoritması')
window.geometry("700x500+10+10")
window.mainloop()
