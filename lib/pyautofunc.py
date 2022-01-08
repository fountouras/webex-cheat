import pyautogui
import time
import webbrowser



s = 0
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

def run(name, email, password, m1l, m2l, m3l, m4l, m5l, m6l, m7l, m8l, tu1l, tu2l, tu3l, tu4l, tu5l, tu6l, tu7l, tu8l, w1l, w2l, w3l, w4l, w5l, w6l, w7l, w8l, t1l, t2l, t3l, t4l, t5l, t6l, t7l, t8l, f1l, f2l, f3l, f4l, f5l, f6l, f7l, f8l):
    print("hi I'm the bot for your webex")
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

