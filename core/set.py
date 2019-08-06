from setting.settings import *
import tkinter

def run():
    win = tkinter.Tk()
    win.geometry("200x200+20+90")
    win.title("设置")

    lb0 = tkinter.Label(text="模式: ")

    mode = tkinter.IntVar(value=1)
    rb0 = tkinter.Radiobutton(win, text="键盘模式", variable=mode, value=0)
    rb1 = tkinter.Radiobutton(win, text="鼠标模式", variable=mode, value=1)

    sound = tkinter.IntVar(value=1)
    cb0 = tkinter.Checkbutton(win, text="音乐", onvalue=1, offvalue=0, variable=sound)

    lb0.grid(row=0, column=0, padx=2, pady=2)
    rb0.grid(row=0, column=1, pady=2)
    rb1.grid(row=0, column=2, pady=2)
    cb0.grid(row=1, column=0, pady=2)


    win.mainloop()