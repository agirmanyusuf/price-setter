from tkinter import *
import tkinter.font as font
import math
import numpy as np


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
        self.b1 = Button(win, text='Fiyat Hesapla', fg='red', command=self.price_automator, height=5, width=20,
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

        # self.lbl_nolight = Label(win, text='Işıksız Fiyat')
        # self.lbl_light = Label(win, text='Işıklı Fiyat')
        # self.lbl_rgb = Label(win, text='RGB Fiyat')
        # self.lbl_desi = Label(win, text='Desi')
        # self.lbl_kargo = Label(win, text='Kargo Maliyeti')
        # self.lbl_etsy = Label(win, text='ETSY Maliyeti')
        # self.lbl_maliyet = Label(win, text='Toplam Maliyet')
        # self.lbl_kar = Label(win, text='İndirimli Kar')
        # self.t_nolight = Entry()
        # self.t_light = Entry()
        # self.t_rgb = Entry()
        # self.t_desi = Entry()
        # self.t_kargo = Entry()
        # self.t_etsy = Entry()
        # self.t_maliyet = Entry()
        # self.t_kar = Entry()
        # self.lbl_nolight.place(x=20, y=220)
        # self.t_nolight.place(x=100, y=220)
        # self.lbl_light.place(x=20, y=260)
        # self.t_light.place(x=100, y=260)
        # self.lbl_rgb.place(x=20, y=300)
        # self.t_rgb.place(x=100, y=300)
        # self.lbl_desi.place(x=360, y=290)
        # self.t_desi.place(x=400, y=290)
        # self.lbl_kargo.place(x=250, y=340)
        # self.t_kargo.place(x=350, y=340)
        # self.lbl_etsy.place(x=250, y=380)
        # self.t_etsy.place(x=350, y=380)
        # self.lbl_maliyet.place(x=250, y=420)
        # self.t_maliyet.place(x=350, y=420)
        # self.lbl_kar.place(x=250, y=460)
        # self.t_kar.place(x=350, y=460)

    def price_automator(self):
        x = int(self.t1.get())
        y = int(self.t2.get())
        usd = int(self.t3.get())
        profit = list(map(float, self.t_nk.get().split(",")))
        profit1 = profit[0] / 100
        profit2 = profit[1] / 100
        profit3 = profit[2] / 100
        z = 6
        desis = [1.47, 1.96, 2.43, 3, 3.63, 4.32, 5.07]
        r = x / y
        table_list = [['Boyut(cm)', 'Boyut(inch)', 'Desi', 'Işıksız', 'Işıklı', 'RGB', 'KargoCost', 'ETSYCost',
                       'ToplamCost', 'İndirimliKar']]
        for desi in desis:
            desicm = desi * 5000
            coeff = [r, 5 * r + 5, 25 - desicm / 6]
            y_new = max(np.roots(coeff))
            x_new = y_new * r
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
            price = total_cost_usd / (0.8 - profit1)
            etsy_cost1 = price * 0.2
            total_cost_plusetsy1 = total_cost_usd + etsy_cost1
            price_light = total_cost_usd / (0.8 - profit2)
            price_rgb = total_cost_usd / (0.8 - profit3)
            if price_rgb * 0.8 - price_rgb * 0.8 * 0.2 - total_cost_usd >= 50:
                price_rgb = price_rgb * 0.93
                price_light = price_light * 0.93
            elif price_rgb * 0.8 - price_rgb * 0.8 * 0.2 - total_cost_usd <= 45:
                price_rgb = price_rgb * 1.1
                price_light = price_light * 1.1
            etsy_cost2 = price_light * 0.2
            total_cost_plusetsy2 = total_cost_usd + etsy_cost2
            etsy_cost3 = price_rgb * 0.2
            total_cost_plusetsy3 = total_cost_usd + etsy_cost3
            kar1 = price * 0.8 - price * 0.8 * 0.2 - total_cost_usd
            kar2 = price_light * 0.8 - price_light * 0.8 * 0.2 - total_cost_usd
            kar3 = price_rgb * 0.8 - price_rgb * 0.8 * 0.2 - total_cost_usd
            table_list.append([f"{round(x_new)}x{round(y_new)}",
                               f"{round(x_new / 2.54)}x{round(y_new / 2.54)}",
                               desi,
                               f"{math.ceil(price)} (%20: {math.ceil(price * 0.8)})",
                               f"{math.ceil(price_light)} (%20: {math.ceil(price_light * 0.8)})",
                               f"{math.ceil(price_rgb)} (%20: {math.ceil(price_rgb * 0.8)})",
                               f"{round(kargo_usd, 1)}",
                               f"{round(etsy_cost1, 1)}, {round(etsy_cost2, 1)}, {round(etsy_cost3, 1)}",
                               f"{round(total_cost_plusetsy1, 1)}, {round(total_cost_plusetsy2, 1)}, {round(total_cost_plusetsy3, 1)}",
                               f"{round(kar1, 1)}, {round(kar2, 1)}, {round(kar3, 1)}"
                               ])

        table_list[2][3] = math.ceil((int(table_list[3][3][:3])+int(table_list[1][3][:3]))/2)
        table_list[2][4] = math.ceil((int(table_list[3][4][:3]) + int(table_list[1][4][:3])) / 2)
        table_list[2][5] = math.ceil((int(table_list[3][5][:3]) + int(table_list[1][5][:3])) / 2)

        total_rows = len(table_list)
        print(table_list)
        print(total_rows)
        total_columns = len(table_list[0])
        print(total_columns)
        x=20
        y=180
        for i in range(total_rows):
            y += 25
            x=20
            for j in range(total_columns):
                if i == 0:
                    if j in (0,1,6):
                        self.entry = Entry(width=8, bg='LightSteelBlue', fg='Black')#, font=('Arial', 16, 'bold'))
                    elif j == 2:
                        self.entry = Entry(width=5, bg='LightSteelBlue', fg='Black')  # , font=('Arial', 16, 'bold'))
                    else:
                        self.entry = Entry(width=15, bg='LightSteelBlue',fg='Black')  # , font=('Arial', 16, 'bold'))
                else:
                    if j in (0,1,6):
                        self.entry = Entry(width=8, fg='blue')
                    elif j == 2 :
                        self.entry = Entry(width=5, fg='blue')
                    else:
                        self.entry = Entry(width=15, fg='blue')
                if j == 1:
                    x+=80
                elif j == 2:
                    x+=80
                elif j == 3:
                    x+=50
                elif j == 4:
                    x+=150
                elif j == 5:
                    x+=150
                elif j == 6:
                    x+=150
                elif j == 7:
                    x+=80
                elif j == 8:
                    x+=150
                elif j == 9:
                    x+=150
                elif j == 10:
                    x+=150

                self.entry.grid(row=i, column=j)
                self.entry.place(x=x,y=y)
                self.entry.insert(END, table_list[i][j])

window = Tk()
mywin = MyWindow(window)
window.title('Etsy Fiyat Algoritması')
window.geometry("1400x500+10+10")
window.mainloop()
