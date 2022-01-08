from tkinter import *
import time
import pyautogui
import time
import webbrowser
print("hi I'm the bot for your webex")
r = False
def opn():
    g = 0
    global s
    start = time.time()
    time.sleep(20)
    while g == 0:
        try:
            if pyautogui.pixelMatchesColor(x=1627, y=449, expectedRGBColor=(43, 148, 254)):
                stop = time.time()
                s = stop - start
                g = 1
            else:
                b = 0
                while b == 0:
                    pyautogui.click(112, 81)
                    time.sleep(8)
                    if pyautogui.pixelMatchesColor(x=1627, y=449, expectedRGBColor=(43, 148, 254)):
                        stop = time.time()
                        s = stop - start
                        b = 1
                    else:
                        start1 = time.time()
                        e = start1 - start
                        if e >= 2362:
                            b = 1
                            g = 1
                            s = 2362
        except:
            g = 0

def connect():
    pyautogui.moveTo(992, 690)
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.leftClick()
    pyautogui.moveTo(992, 859)
    time.sleep(1)
    pyautogui.leftClick()
    pyautogui.moveTo(1097, 681)
    time.sleep(1)
    pyautogui.leftClick()
    pyautogui.moveTo(1168, 458)
    time.sleep(1)
    pyautogui.leftClick()
    pyautogui.moveTo(1118, 694)
    time.sleep(1)
    pyautogui.leftClick()
    pyautogui.moveTo(568, 1129)
    time.sleep(5)
    pyautogui.leftClick()
    pyautogui.moveTo(792, 1056)
    pyautogui.leftClick()
def ext():
    pyautogui.moveTo(623, 46)
    time.sleep(1)
    pyautogui.leftClick()
    pyautogui.moveTo(1077, 195)
    time.sleep(1)
    pyautogui.leftClick()
def entry(name, email, password):
    pyautogui.moveTo(623, 341)
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(1601, 390)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.typewrite("st-2001683@e-arsakeio.gr")
    time.sleep(1)
    pyautogui.moveTo(1500, 390)
    pyautogui.leftClick()
    pyautogui.moveTo(1605, 486)
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(20)
    connect()

def m1(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()

def m2(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()

def m3(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()

def m4(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()

def m5(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()

def m6(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()

def m7(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()

def m8(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()

def tu1(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()

def tu2(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def tu3(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def tu4(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def tu5(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def tu6(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def tu7(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2062 - s)
    ext()
def tu8(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()

def w1(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
    time.sleep(300)
def w2(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def w3(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def w4(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def w5(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def w6(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def w7(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def w8(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()

def t1(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def t2(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def t3(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def t4(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def t5(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def t6(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def t7(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def t8(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()

def f1(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def f2(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def f3(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def f4(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def f5(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def f6(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def f7(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()
def f8(link, name, email, password):
    webbrowser.open(link)
    opn()
    entry(name=name, email=email, password=password)
    time.sleep(2362 - s)
    ext()

def runp(name, email, password, m1l, m2l, m3l, m4l, m5l, m6l, m7l, m8l, tu1l, tu2l, tu3l, tu4l, tu5l, tu6l, tu7l, tu8l, w1l, w2l, w3l, w4l, w5l, w6l, w7l, w8l, t1l, t2l, t3l, t4l, t5l, t6l, t7l, t8l, f1l, f2l, f3l, f4l, f5l, f6l, f7l, f8l):
    while 1 != 0:
        a = time.ctime()
        if a[0] == "M" and a[11] == "0" and a[12] == "8" and a[14] == "1" and a[15] == "0":
            m1(link=m1l, name=name, email=email, password=password)
        elif a[0] == "M" and a[11] == "0" and a[12] == "8" and a[14] == "5" and a[15] == "5":
            m2(link=m2l, name=name, email=email, password=password)
        elif a[0] == "M" and a[11] == "0" and a[12] == "9" and a[14] == "5" and a[15] == "0":
            m3(link=m3l, name=name, email=email, password=password)
        elif a[0] == "M" and a[11] == "1" and a[12] == "0" and a[14] == "4" and a[15] == "5":
            m4(link=m4l, name=name, email=email, password=password)
        elif a[0] == "M" and a[11] == "1" and a[12] == "1" and a[14] == "3" and a[15] == "5":
            m5(link=m5l, name=name, email=email, password=password)
        elif a[0] == "M" and a[11] == "1" and a[12] == "2" and a[14] == "3" and a[15] == "0":
            m6(link=m6l, name=name, email=email, password=password)
        elif a[0] == "M" and a[11] == "1" and a[12] == "3" and a[14] == "2" and a[15] == "5":
            m7(link=m7l, name=name, email=email, password=password)
        elif a[0] == "M" and a[11] == "1" and a[12] == "4" and a[14] == "1" and a[15] == "0":
            m8(link=m8l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "u" and a[11] == "0" and a[12] == "8" and a[14] == "1" and a[15] == "0":
            tu1(link=tu1l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "u" and a[11] == "0" and a[12] == "8" and a[14] == "5" and a[15] == "5":
            tu2(link=t2l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "u" and a[11] == "0" and a[12] == "9" and a[14] == "5" and a[15] == "0":
            tu3(link=tu3l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "u" and a[11] == "1" and a[12] == "0" and a[14] == "4" and a[15] == "5":
            tu4(link=tu4l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "u" and a[11] == "1" and a[12] == "1" and a[14] == "3" and a[15] == "5":
            tu5(link=tu5l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "u" and a[11] == "1" and a[12] == "2" and a[14] == "3" and a[15] == "0":
            tu6(link=tu6l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "u" and a[11] == "1" and a[12] == "3" and a[14] == "3" and a[15] == "0":
            tu7(link=tu7l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "u" and a[11] == "1" and a[12] == "4" and a[14] == "1" and a[15] == "0":
            tu8(link=tu8l, name=name, email=email, password=password)
        elif a[0] == "W" and a[11] == "0" and a[12] == "8" and a[14] == "1" and a[15] == "0":
            w1(link=w1l, name=name, email=email, password=password)
        elif a[0] == "W" and a[11] == "0" and a[12] == "8" and a[14] == "5" and a[15] == "5":
            w2(link=w2l, name=name, email=email, password=password)
        elif a[0] == "W" and a[11] == "0" and a[12] == "9" and a[14] == "5" and a[15] == "0":
            w3(link=w3l, name=name, email=email, password=password)
        elif a[0] == "W" and a[11] == "1" and a[12] == "0" and a[14] == "4" and a[15] == "5":
            w4(link=w4l, name=name, email=email, password=password)
        elif a[0] == "W" and a[11] == "1" and a[12] == "1" and a[14] == "3" and a[15] == "5":
            w5(link=w5l, name=name, email=email, password=password)
        elif a[0] == "W" and a[11] == "1" and a[12] == "2" and a[14] == "3" and a[15] == "0":
            w6(link=w6l, name=name, email=email, password=password)
        elif a[0] == "W" and a[11] == "1" and a[12] == "3" and a[14] == "2" and a[15] == "5":
            w7(link=w7l, name=name, email=email, password=password)
        elif a[0] == "W" and a[11] == "1" and a[12] == "4" and a[14] == "1" and a[15] == "0":
            w8(link=w8l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "h" and a[11] == "0" and a[12] == "8" and a[14] == "1" and a[15] == "0":
            t1(link=t1l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "h" and a[11] == "0" and a[12] == "8" and a[14] == "5" and a[15] == "5":
            t2(link=t2l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "h" and a[11] == "0" and a[12] == "9" and a[14] == "5" and a[15] == "0":
            t3(link=t3l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "h" and a[11] == "1" and a[12] == "0" and a[14] == "4" and a[15] == "5":
            t4(link=t4l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "h" and a[11] == "1" and a[12] == "1" and a[14] == "3" and a[15] == "5":
            t5(link=t5l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "h" and a[11] == "1" and a[12] == "2" and a[14] == "3" and a[15] == "0":
            t6(link=t6l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "h" and a[11] == "1" and a[12] == "3" and a[14] == "2" and a[15] == "5":
            t7(link=t7l, name=name, email=email, password=password)
        elif a[0] == "T" and a[1] == "h" and a[11] == "1" and a[12] == "4" and a[14] == "1" and a[15] == "0":
            t8(link=t8l, name=name, email=email, password=password)
        elif a[0] == "F" and a[11] == "0" and a[12] == "8" and a[14] == "1" and a[15] == "0":
            f1(link=f1l, name=name, email=email, password=password)
        elif a[0] == "F" and a[11] == "0" and a[12] == "8" and a[14] == "5" and a[15] == "5":
            f2(link=f2l, name=name, email=email, password=password)
        elif a[0] == "F" and a[11] == "0" and a[12] == "9" and a[14] == "5" and a[15] == "0":
            f3(link=f3l, name=name, email=email, password=password)
        elif a[0] == "F" and a[11] == "1" and a[12] == "0" and a[14] == "4" and a[15] == "5":
            f4(link=f4l, name=name, email=email, password=password)
        elif a[0] == "F" and a[11] == "1" and a[12] == "1" and a[14] == "3" and a[15] == "5":
            f5(link=f5l, name=name, email=email, password=password)
        elif a[0] == "F" and a[11] == "1" and a[12] == "2" and a[14] == "3" and a[15] == "0":
            f6(link=f6l, name=name, email=email, password=password)
        elif a[0] == "F" and a[11] == "1" and a[12] == "3" and a[14] == "2" and a[15] == "5":
            f7(link=f7l, name=name, email=email, password=password)
        elif a[0] == "F" and a[11] == "1" and a[12] == "4" and a[14] == "1" and a[15] == "0":
            f8(link=f8l, name=name, email=email, password=password)
def runt():
    global n, e, p
    s = 0
    scn = Tk()
    mf = Frame(scn)
    tuf = Frame(scn)
    wf = Frame(scn)
    tf = Frame(scn)
    ff = Frame(scn)
    fd = [mf, tuf, wf, tf, ff]
    g = 1
    for frame in fd:
        frame.grid(column=g, row=0, rowspan=16)
        g += 1
    def save():
        global r, n, e, p, m1l, m2l, m3l, m4l, m5l, m6l, m7l, m8l, tu1l, tu2l, tu3l, tu4l, tu5l, tu6l, tu7l, tu8l, w1l, w2l, w3l, w4l, w5l, w6l, w7l, w8l, t1l, t2l, t3l, t4l, t5l, t6l, t7l, t8l, f1l, f2l, f3l, f4l, f5l, f6l, f7l, f8l
        with open("name.txt", 'w') as f:
            f.write(name.get())
        with open("email.txt", 'w') as f:
            f.write(email.get())
        with open("password.txt", 'w') as f:
            f.write(password.get())
        a = 1
        for hour in hours:
            with open("hour" + str(a) + ".txt", 'w') as f:
                f.write(hour.get())
            a += 1
        m1l = m1e.get()
        m2l = m2e.get()
        m3l = m3e.get()
        m4l  =m4e.get()
        m5l = m5e.get()
        m6l = m6e.get()
        m7l = m7e.get()
        m8l = m8e.get()
        tu1l = tu1e.get()
        tu2l = tu2e.get()
        tu3l = tu3e.get()
        tu4l = tu4e.get()
        tu5l = tu5e.get()
        tu6l = tu6e.get()
        tu7l = tu7e.get()
        tu8l = tu8e.get()
        w1l = w1e.get()
        w2l = w1e.get()
        w3l = w3e.get()
        w4l = w4e.get()
        w5l = w5e.get()
        w6l = w6e.get()
        w7l = w7e.get()
        w8l = w8e.get()
        t1l = t1e.get()
        t2l = t2e.get()
        t3l = t3e.get()
        t4l = t4e.get()
        t5l = t5e.get()
        t6l = t6e.get()
        t7l = t7e.get()
        t8l = t8e.get()
        f1l = f1e.get()
        f2l = f2e.get()
        f3l = f3e.get()
        f4l = f4e.get()
        f5l = f5e.get()
        f6l = f6e.get()
        f7l = f7e.get()
        f8l = f8e.get()
        r = True
        run()
        close()
    lbl1 = Label(scn, text="name:")
    name = Entry(scn)
    lbl2 = Label(scn, text="email:")
    email = Entry(scn)
    lbl3 = Label(scn, text="session password:")
    password = Entry(scn)
    m1e = Entry(master=mf)
    m2e = Entry(master=mf)
    m3e = Entry(master=mf)
    m4e = Entry(master=mf)
    m5e = Entry(master=mf)
    m6e = Entry(master=mf)
    m7e = Entry(master=mf)
    m8e = Entry(master=mf)
    tu1e = Entry(master=tuf)
    tu2e = Entry(master=tuf)
    tu3e = Entry(master=tuf)
    tu4e = Entry(master=tuf)
    tu5e = Entry(master=tuf)
    tu6e = Entry(master=tuf)
    tu7e = Entry(master=tuf)
    tu8e = Entry(master=tuf)
    w1e = Entry(master=wf)
    w2e = Entry(master=wf)
    w3e = Entry(master=wf)
    w4e = Entry(master=wf)
    w5e = Entry(master=wf)
    w6e = Entry(master=wf)
    w7e = Entry(master=wf)
    w8e = Entry(master=wf)
    t1e = Entry(master=tf)
    t2e = Entry(master=tf)
    t3e = Entry(master=tf)
    t4e = Entry(master=tf)
    t5e = Entry(master=tf)
    t6e = Entry(master=tf)
    t7e = Entry(master=tf)
    t8e = Entry(master=tf)
    f1e = Entry(master=ff)
    f2e = Entry(master=ff)
    f3e = Entry(master=ff)
    f4e = Entry(master=ff)
    f5e = Entry(master=ff)
    f6e = Entry(master=ff)
    f7e = Entry(master=ff)
    f8e = Entry(master=ff)
    btn = Button(scn, text="run program", command=save)
    lbl1.grid(column=0, row=0)
    name.grid(column=0, row=1)
    lbl2.grid(column=0, row=2)
    email.grid(column=0, row=3)
    lbl3.grid(column=0, row=4)
    password.grid(column=0, row=5)
    hours = [m1e, m2e, m3e, m4e, m5e, m6e, m7e, m8e, tu1e, tu2e, tu3e, tu4e, tu5e, tu6e, tu7e, tu8e, w1e, w2e, w3e, w4e, w5e, w6e, w7e, w8e, t1e, t2e, t3e, t4e, t5e, t6e, t7e, t8e, f1e, f2e, f3e, f4e, f5e, f6e, f7e, f8e]
    monday = [m1e, m2e, m3e, m4e, m5e, m6e, m7e, m8e]
    tuesday = [tu1e, tu2e, tu3e, tu4e, tu5e, tu6e, tu7e, tu8e]
    wednesday = [w1e, w2e, w3e, w4e, w5e, w6e, w7e, w8e]
    thursday = [t1e, t2e, t3e, t4e, t5e, t6e, t7e, t8e]
    friday = [f1e, f2e, f3e, f4e, f5e, f6e, f7e, f8e]
    with open("name.txt", 'r') as f:
        n = f.read()
        name.insert("0", n)
    with open("email.txt", 'r') as f:
        e = f.read()
        email.insert("0", e)
    with open("password.txt", 'r') as f:
        p = f.read()
        password.insert("0", p)
    a = 1
    for hour in monday:
        with open("hour" + str(a) + ".txt", 'r') as f:
            hour.insert("0", f.read())
        Label(master=mf, text="hour" + str(a)).pack()
        hour.pack()
        a += 1
    b = 1
    for hour in tuesday:
        with open("hour" + str(a) + ".txt", 'r') as f:
            hour.insert("0", f.read())
        Label(master=tuf, text="hour" + str(b)).pack()
        hour.pack()
        b += 1
        a += 1
    c = 1
    for hour in wednesday:
        with open("hour" + str(a) + ".txt", 'r') as f:
            hour.insert("0", f.read())
        Label(master=wf, text="hour" + str(c)).pack()
        hour.pack()
        c += 1
        a += 1
    d = 1
    for hour in thursday:
        with open("hour" + str(a) + ".txt", 'r') as f:
            hour.insert("0", f.read())
        Label(master=tf, text="hour" + str(d)).pack()
        hour.pack()
        d += 1
        a += 1
    r = 1

    for hour in friday:
        with open("hour" + str(a) + ".txt", 'r') as f:
            hour.insert("0", f.read())
        Label(master=ff, text="hour" + str(r)).pack()
        hour.pack()
        r += 1
        a += 1
    btn.grid(column=0, row=15)
    def close():
        scn.destroy()
    scn.mainloop()
def run():
    if r == True:
        runp(name=n, email=e, password=p, m1l=m1l, m2l=m2l, m3l=m3l, m4l=m4l, m5l=m5l, m6l=m6l, m7l=m7l, m8l=m8l, tu1l=tu1l, tu2l=tu2l, tu3l=tu3l, tu4l=tu4l, tu5l=tu5l, tu6l=tu6l, tu7l=tu7l, tu8l=tu8l, w1l=w1l, w2l=w2l, w3l=w3l, w4l=w4l, w5l=w5l, w6l=w6l, w7l=w7l, w8l=w8l, t1l=t1l, t2l=t2l, t3l=t3l, t4l=t4l, t5l=t5l, t6l=t6l, t7l=t7l, t8l=t8l, f1l=f1l, f2l=f2l, f3l=f3l, f4l=f4l, f5l=f5l, f6l=f6l, f7l=f7l, f8l=f8l)
    else:
        runt()
run()