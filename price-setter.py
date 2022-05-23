from tkinter import *
import tkinter.font as font
import math


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Kenar1')
        self.lbl2 = Label(win, text='Kenar2')
        self.lbl3 = Label(win, text='USD/TRY')
        self.lbl_nk = Label(win, text='NetKar(%)')
        self.lbl_separator = Label(win, text='----------------------------------------------------------------------')
        self.t1 = Entry(bd=3)
        self.t1.insert(0, 30)
        self.t2 = Entry()
        self.t2.insert(0, 30)
        self.t3 = Entry()
        self.t3.insert(0, 16)
        self.t_nk = Entry()
        self.t_nk.insert(0, "25, 40, 45")
        # self.btn2 = Button(win, text='Subtract')
        # self.btn3 = Button(win, text="Multilication")
        # self.btn4 = Button(win, text="Division")
        self.lbl1.place(x=20, y=20)
        self.t1.place(x=100, y=20)
        self.lbl2.place(x=20, y=60)
        self.t2.place(x=100, y=60)
        self.lbl3.place(x=20, y=100)
        self.t3.place(x=100, y=100)
        self.lbl_nk.place(x=20, y=140)
        self.t_nk.place(x=100, y=140)
        self.lbl_separator.place(x=80, y=180)
        myFont = font.Font(family='Helvetica', size=20, weight='bold')
        # self.btn1 = Button(win, text='Fiyat Hesapla')
        self.b1 = Button(win, text='Fiyat Hesapla', fg='red', command=self.price_setter, height=5, width=20,
                         font=myFont)
        self.b1.place(x=320, y=30)
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
        # -------------------------------------------------------------------------------------
        self.lbl_nolight = Label(win, text='Işıksız Fiyat')
        self.lbl_light = Label(win, text='Işıklı Fiyat')
        self.lbl_rgb = Label(win, text='RGB Fiyat')
        self.lbl_desi = Label(win, text='Desi')
        self.lbl_kargo = Label(win, text='Kargo Maliyeti')
        self.lbl_etsy = Label(win, text='ETSY Maliyeti')
        self.lbl_maliyet = Label(win, text='Toplam Maliyet')
        self.lbl_kar = Label(win, text='İndirimli Kar')
        self.t_nolight = Entry()
        self.t_light = Entry()
        self.t_rgb = Entry()
        self.t_desi = Entry()
        self.t_kargo = Entry()
        self.t_etsy = Entry()
        self.t_maliyet = Entry()
        self.t_kar = Entry()
        self.lbl_nolight.place(x=20, y=220)
        self.t_nolight.place(x=100, y=220)
        self.lbl_light.place(x=20, y=260)
        self.t_light.place(x=100, y=260)
        self.lbl_rgb.place(x=20, y=300)
        self.t_rgb.place(x=100, y=300)
        self.lbl_desi.place(x=360, y=290)
        self.t_desi.place(x=400, y=290)
        self.lbl_kargo.place(x=250, y=340)
        self.t_kargo.place(x=350, y=340)
        self.lbl_etsy.place(x=250, y=380)
        self.t_etsy.place(x=350, y=380)
        self.lbl_maliyet.place(x=250, y=420)
        self.t_maliyet.place(x=350, y=420)
        self.lbl_kar.place(x=250, y=460)
        self.t_kar.place(x=350, y=460)

    def price_setter(self):
        x = int(self.t1.get()) + 5
        y = int(self.t2.get()) + 5
        usd = int(self.t3.get())
        profit =list(map(float, self.t_nk.get().split(",")))
        profit1 = profit[0] / 100
        profit2 = profit[1] / 100
        profit3 = profit[2] / 100
        z = 6
        desi = x * y * z / 5000
        if desi <= 1:
            kargo = 426.9
        elif desi <= 2:
            kargo = 459.67
        elif desi <= 2.5:
            kargo = 564.2
        elif desi <= 3:
            kargo = 668.73
        elif desi <= 3.5:
            kargo = 773.26
        elif desi <= 4:
            kargo = 877.79
        elif desi <= 4.5:
            kargo = 982.32
        elif desi <= 5:
            kargo = 1086.8
        elif desi <= 5.5:
            kargo = 1191.38
        elif desi <= 6:
            kargo = 1295.91
        elif desi <= 6.5:
            kargo = 1400.44
        elif desi <= 7:
            kargo = 1504.97
        elif desi <= 7.5:
            kargo = 1609.5
        elif desi <= 8:
            kargo = 1714.03
        elif desi <= 8.5:
            kargo = 1818.56
        elif desi <= 9:
            kargo = 1923.09
        elif desi <= 9.5:
            kargo = 2027.62
        elif desi <= 10:
            kargo = 2132.15
        else:
            kargo = 0
        kargo_usd = kargo / usd
        urun_maliyet = 100
        urun_maliyet_usd = 100 / usd
        total_cost = urun_maliyet + kargo
        total_cost_usd = total_cost / usd
        price = total_cost_usd/(0.8 - profit1)
        etsy_cost1 = price * 0.2
        total_cost_plusetsy1 = total_cost_usd + etsy_cost1
        price_light = total_cost_usd / (0.8 - profit2)
        price_rgb = total_cost_usd / (0.8 - profit3)
        if price_rgb*0.8 - price_rgb*0.8*0.2 - total_cost_usd>=50:
            price_rgb = price_rgb*0.93
            price_light = price_light * 0.93
        elif price_rgb*0.8 - price_rgb*0.8*0.2 - total_cost_usd<=45:
            price_rgb = price_rgb * 1.1
            price_light = price_light * 1.1
        etsy_cost2 = price_light * 0.2
        total_cost_plusetsy2 = total_cost_usd + etsy_cost2
        etsy_cost3 = price_rgb * 0.2
        total_cost_plusetsy3 = total_cost_usd + etsy_cost3
        kar1 = price*0.8 - price*0.8*0.2 - total_cost_usd
        kar2 = price_light*0.8 - price_light*0.8*0.2 - total_cost_usd
        kar3 = price_rgb*0.8 - price_rgb*0.8*0.2 - total_cost_usd
        # price_light = price*1.4
        # price_rgb = price*1.55

        self.t_nolight.delete(0, 'end')
        self.t_nolight.insert(END, f"{math.ceil(price)}    ---->%20 indirimle: {math.ceil(price*0.8)} ")
        self.t_light.delete(0, 'end')
        self.t_light.insert(END, f"{math.ceil(price_light)}   ---->%20 indirimle: {math.ceil(price_light*0.8)} ")
        self.t_rgb.delete(0, 'end')
        self.t_rgb.insert(END, f"{math.ceil(price_rgb)}   ---->%20 indirimle: {math.ceil(price_rgb*0.8)} ")
        self.t_desi.delete(0, 'end')
        self.t_desi.insert(END, f"{round(desi, 2)}")
        self.t_kargo.delete(0, 'end')
        self.t_kargo.insert(END, f"{round(kargo_usd, 2)}")
        self.t_etsy.delete(0, 'end')
        self.t_etsy.insert(END, f"{round(etsy_cost1, 2)}, {round(etsy_cost2, 2)}, {round(etsy_cost3, 2)}")
        self.t_maliyet.delete(0, 'end')
        self.t_maliyet.insert(END, f"{round(total_cost_plusetsy1, 2)}, {round(total_cost_plusetsy2, 2)}, {round(total_cost_plusetsy3, 2)}")
        self.t_kar.delete(0, 'end')
        self.t_kar.insert(END,
                              f"{round(kar1, 2)}, {round(kar2, 2)}, {round(kar3, 2)}")
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
