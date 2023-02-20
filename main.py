from tkinter import INSERT, Tk, Label, Entry, Button, Text, END
import math
from searchClass import Saerch1

"""The function get_probability accepts some probability percent then
   calculates and shows all probabilities above the probability that
   accepted and prints the probability-price context accordingly. It's mean all
   prices that 'stay out of the money"""


def get_probability():
    exp = int(ent1.get())
    range1 = int(ent2.get())
    search = Saerch1(exp, range1)
    price = search.get_price()
    iv = search.get_iv() * 100
    sumf = 3.9998584534793378
    sum_in = 3.9993720275712055
    result_long = {}
    result_short = {}
    var = -3.75
    vl = []
    for i in range(31):
        var += 0.25
        vl.append(var)
        sum_in -= math.exp(-1 / 2 * (vl[i] ** 2)) / (math.sqrt(2 * math.pi))
        p = round(price + iv * exp * vl[i], 2)
        prob = round((1 - sum_in / sumf) * 100, 2)
        if 100 - prob > range1:
            result_short.update({p: 100 - prob})
        if prob > range1:
            result_long.update({p: prob})

    txt1.insert(INSERT, "expire {0} days:\n".format(exp))
    txt1.insert(INSERT, "price:{1} --- iv:{2} --- short (OUT THE MONEY):\n".format(exp, price, round(iv, 2)))
    txt1.insert(INSERT, result_short.items())
    txt1.insert(INSERT, "\n \n")
    txt1.insert(INSERT, "price:{1} --- iv:{2} --- long (OUT THE MONEY):\n".format(exp, price, round(iv, 2)))
    txt1.insert(INSERT, result_long.items())
    txt1.insert(INSERT, "\n ______________________________________________________________________\n")
    txt1.insert(INSERT, "\n\n >>> another expire:\n")


window = Tk()
window.title('IV Price')
window.geometry('1200x600')
window.resizable(False, False)
window.iconbitmap('hamster.ico')

lbl1 = Label(window, text="Enter days for expire: ")
lbl1.place(x=2, y=5)
ent1 = Entry(window, width=5)
ent1.place(x=130, y=10)

lbl2 = Label(window, text="Enter minimum percent (For example:95,90,87):")
lbl2.place(x=2, y=35)
ent2 = Entry(window, width=5)
ent2.place(x=260, y=37)
lbl2ps = Label(window, text="%")
lbl2ps.place(x=300, y=37)

btn1 = Button(window, text="calculate", command=get_probability)
btn1.place(x=370, y=8)
btn2 = Button(window, text='Delete', command=lambda: txt1.delete(0.0, END))
btn2.place(x=370, y=40)

txt1 = Text(window, width=150)
txt1.place(x=5, y=100)

window.mainloop()
