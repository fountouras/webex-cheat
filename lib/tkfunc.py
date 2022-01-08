from tkinter import *
import time
scn = Tk()
r = False
mf = Frame(scn)
tuf = Frame(scn)
wf = Frame(scn)
tf = Frame(scn)
ff = Frame(scn)
fd = [mf, tuf, wf, tf, ff]
g = 1
def save():
    global r, m1l, m2l, m3l, m4l, m5l, m6l, m7l, m8l, tu1l, tu2l, tu3l, tu4l, tu5l, tu6l, tu7l, tu8l, w1l, w2l, w3l, w4l, w5l, w6l, w7l, w8l, t1l, t2l, t3l, t4l, t5l, t6l, t7l, t8l, f1l, f2l, f3l, f4l, f5l, f6l, f7l, f8l
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
    m4l = m4e.get()
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
    time.sleep(1)
    close()
def close():
    scn.destroy()
for frame in fd:
    frame.grid(column=g, row=0, rowspan=16)
    g += 1
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
    global n
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
scn.mainloop()