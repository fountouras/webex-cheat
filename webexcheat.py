import pyautogui
import time
import webbrowser

print("hi I'm the bot for your webex")

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
                            s = 2362
        finally:
            global a
            a = 0

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
def entry():
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

def m1():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t7eedc3b216f32ece865d9b5ffb9d0cdc")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()

def m2():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t6e1e003d136145bc979c29f16c90ee71")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()

def m3():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t13e1157248318f645cd06c1773f04752")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()

def m4():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t31515fa59f17c267683523bf8a50d150")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()

def m5():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t8d90c298ddef67cc0e8386382191ec0e")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()

def m6():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t7505a83919be05f6a1102455f242b886")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()

def m7():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=tf829294e61b1245802cf4e9fb2189d84")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()

def m8():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=tce8306516fcf5a81c0b74a81a817d039")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()

def tu1():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=td78afc41666b700b1a62a92d722e1b97")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()

def tu2():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t924bf9a74fafcb5b6e51faf8df2713d8")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def tu3():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t4ff09ad9281777b5aa6b6d94fc97b2eb")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def tu4():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t170a14d74ae0106734fe745e394875e1")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def tu5():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t34e32def4caedca0f6dda89e67698a38")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def tu6():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=ta01f4ae809ce0e0b50d668cc07b6e955")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def tu7():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t31f903500d786d43de3d5cf5cc58fd19")
    opn()
    entry()
    time.sleep(2062 - s)
    ext()
def tu8():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=ta24ecc163fc4b6cadbe6620e1dfa24fb")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()

def w1():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t34c3c251fb29aa6627ef114943c8a084")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
    time.sleep(300)
def w2():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=ta5d5e06f18316ccb0898b269f669a83f")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def w3():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=td1592ded54c0ec9cd9ec9085c1cd9297")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def w4():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=tc6e480aadd3995a46bf30c5adca80eb5")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def w5():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=te290f3278aeb89c54f40ee161d366083")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def w6():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t33d09e6d830a014dfd21c367cb5e67b6")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def w7():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t8fd85c37c879c2a0e8fa20dfa38a66d4")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def w8():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t88edd55e383768c21b1304680d9e31ad")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()

def t1():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t30a9cf8ed5e60a87a5a3eea69aafdefe")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def t2():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t03d029b85c26654383f65a01d5573d82")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def t3():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t1ddeb3378c6a4f985c0ae909f5f66fc9")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def t4():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=td9b2ff27a6c8986ae6ce14fcf752df34")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def t5():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=td5f70caa87bab31b5b303688551cda5f")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def t6():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=ta52d066fe0e81a3b5cade76ac7d9e71c")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def t7():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t6e65481521da1b043d498cff90a1352b")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def t8():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t4acf7db71e425fc28e62de0a8f5aeaf5")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()

def f1():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t6ec1340c78d4e7dcff9f9f5b140f506a")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def f2():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=tbdd151bbadc8d10d3d2d125019508f88")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def f3():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=tfab4571dcc0cc16158d2948f644ffff5")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def f4():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t79336810699abe3e2b6dc4d83b66c64e")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def f5():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t512bbc1d0196212ba219cb6108bfe6ed")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def f6():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t2b6a998a0b5acebb3134ec5f259fd56c")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def f7():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t71c9c1e454f0fc88c3e650cebe15d91d")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()
def f8():
    webbrowser.open("https://arsakeio.webex.com/arsakeio/k2/j.php?MTID=t0f9f698bac67a1dd109930e91f25586f")
    opn()
    entry()
    time.sleep(2362 - s)
    ext()


while 1 != 0:
    a = time.ctime()
    if a[0] == "M" and a[11] == "0" and a[12] == "8" and a[14] == "1" and a[15] == "0":
        m1()
    elif a[0] == "M" and a[11] == "0" and a[12] == "8" and a[14] == "5" and a[15] == "5":
        m2()
    elif a[0] == "M" and a[11] == "0" and a[12] == "9" and a[14] == "5" and a[15] == "0":
        m3()
    elif a[0] == "M" and a[11] == "1" and a[12] == "0" and a[14] == "4" and a[15] == "5":
        m4()
    elif a[0] == "M" and a[11] == "1" and a[12] == "1" and a[14] == "3" and a[15] == "5":
        m5()
    elif a[0] == "M" and a[11] == "1" and a[12] == "2" and a[14] == "3" and a[15] == "0":
        m6()
    elif a[0] == "M" and a[11] == "1" and a[12] == "3" and a[14] == "2" and a[15] == "5":
        m7()
    elif a[0] == "M" and a[11] == "1" and a[12] == "4" and a[14] == "1" and a[15] == "0":
        m8()

    if a[0] == "T" and a[1] == "u" and a[11] == "0" and a[12] == "8" and a[14] == "1" and a[15] == "0":
        tu1()
    elif a[0] == "T" and a[1] == "u" and a[11] == "0" and a[12] == "8" and a[14] == "5" and a[15] == "5":
        tu2()
    elif a[0] == "T" and a[1] == "u" and a[11] == "0" and a[12] == "9" and a[14] == "5" and a[15] == "0":
        tu3()
    elif a[0] == "T" and a[1] == "u" and a[11] == "1" and a[12] == "0" and a[14] == "4" and a[15] == "5":
        tu4()
    elif a[0] == "T" and a[1] == "u" and a[11] == "1" and a[12] == "1" and a[14] == "3" and a[15] == "5":
        tu5()
    elif a[0] == "T" and a[1] == "u" and a[11] == "1" and a[12] == "2" and a[14] == "3" and a[15] == "0":
        tu6()
    elif a[0] == "T" and a[1] == "u" and a[11] == "1" and a[12] == "3" and a[14] == "3" and a[15] == "0":
        tu7()
    elif a[0] == "T" and a[1] == "u" and a[11] == "1" and a[12] == "4" and a[14] == "1" and a[15] == "0":
        tu8()

    if a[0] == "W" and a[11] == "0" and a[12] == "8" and a[14] == "1" and a[15] == "0":
        w1()
    elif a[0] == "W" and a[11] == "0" and a[12] == "8" and a[14] == "5" and a[15] == "5":
        w2()
    elif a[0] == "W" and a[11] == "0" and a[12] == "9" and a[14] == "5" and a[15] == "0":
        w3()
    elif a[0] == "W" and a[11] == "1" and a[12] == "0" and a[14] == "4" and a[15] == "5":
        w4()
    elif a[0] == "W" and a[11] == "1" and a[12] == "1" and a[14] == "3" and a[15] == "5":
        w5()
    elif a[0] == "W" and a[11] == "1" and a[12] == "2" and a[14] == "3" and a[15] == "0":
        w6()
    elif a[0] == "W" and a[11] == "1" and a[12] == "3" and a[14] == "2" and a[15] == "5":
        w7()
    elif a[0] == "W" and a[11] == "1" and a[12] == "4" and a[14] == "1" and a[15] == "0":
        w8()

    if a[0] == "T" and a[1] == "h" and a[11] == "0" and a[12] == "8" and a[14] == "1" and a[15] == "0":
        t1()
    elif a[0] == "T" and a[1] == "h" and a[11] == "0" and a[12] == "8" and a[14] == "5" and a[15] == "5":
        t2()
    elif a[0] == "T" and a[1] == "h" and a[11] == "0" and a[12] == "9" and a[14] == "5" and a[15] == "0":
        t3()
    elif a[0] == "T" and a[1] == "h" and a[11] == "1" and a[12] == "0" and a[14] == "4" and a[15] == "5":
        t4()
    elif a[0] == "T" and a[1] == "h" and a[11] == "1" and a[12] == "1" and a[14] == "3" and a[15] == "5":
        t5()
    elif a[0] == "T" and a[1] == "h" and a[11] == "1" and a[12] == "2" and a[14] == "3" and a[15] == "0":
        t6()
    elif a[0] == "T" and a[1] == "h" and a[11] == "1" and a[12] == "3" and a[14] == "2" and a[15] == "5":
        t7()
    elif a[0] == "T" and a[1] == "h" and a[11] == "1" and a[12] == "4" and a[14] == "1" and a[15] == "0":
        t8()

    if a[0] == "F" and a[11] == "0" and a[12] == "8" and a[14] == "1" and a[15] == "0":
        f1()
    elif a[0] == "F" and a[11] == "0" and a[12] == "8" and a[14] == "5" and a[15] == "5":
        f2()
    elif a[0] == "F" and a[11] == "0" and a[12] == "9" and a[14] == "5" and a[15] == "0":
        f3()
    elif a[0] == "F" and a[11] == "1" and a[12] == "0" and a[14] == "4" and a[15] == "5":
        f4()
    elif a[0] == "F" and a[11] == "1" and a[12] == "1" and a[14] == "3" and a[15] == "5":
        f5()
    elif a[0] == "F" and a[11] == "1" and a[12] == "2" and a[14] == "3" and a[15] == "0":
        f6()
    elif a[0] == "F" and a[11] == "1" and a[12] == "3" and a[14] == "2" and a[15] == "5":
        f7()
    elif a[0] == "F" and a[11] == "1" and a[12] == "4" and a[14] == "1" and a[15] == "0":
        f8()
