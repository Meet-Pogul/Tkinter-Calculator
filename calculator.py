from tkinter import *
import math


def click(event):
    print(root.winfo_height(), root.winfo_width())
    text = event.widget.cget("text")
    try:
        if text == '=':
            text = scvalue.get()
            if 'sq' in text:
                l = text.index('sq')
                flag = 0
                a = ""
                for i in text[l+2:]:
                    if i == '(':
                        flag += 1
                    elif i == ')':
                        if flag == 1:
                            a += i
                            break
                        flag -= 1
                    a += i
                    l += 1
                a = str(math.sqrt(eval(a)))
                text = text[:text.index("sq")] + \
                    a + text[l+3:]
                try:
                    if text[text.index(a)-2].isnumeric() or text[text.index(a)+len(a)].isnumeric():
                        raise Exception
                except IndexError:
                    pass
            value = eval(text)

        elif text == 'C':
            value = ""
        elif text == '1/x':
            value = eval(scvalue.get())
            value = 1/value
        elif text == '+/-':
            value = eval(scvalue.get())
            value = -value
        else:
            value = scvalue.get() + text
    except Exception as e:
        print(e)
        value = "Syntax Error"
    finally:
        scvalue.set(value)


def createButton(tex, fontsize):
    b = Button(f1, text=str(tex), padx=19, pady=15,
               font=("Times New Roman", fontsize, "bold"))
    b.pack(side=LEFT, pady=3, padx=3)
    b.bind("<Button-1>", click)


root = Tk()
root.geometry("405x500")
root.resizable(width=False, height=False)
root.title("Calculator")
root.wm_iconbitmap("Calculator.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font=("Times New Roman", 30, "bold"))
screen.pack(fill=X, ipadx=8, pady=10, padx=10)
charpos = {1: ('+', '//'), 4: ('-', '('), 7: ('*', ')')}

f1 = Frame(root, bg="grey")
for j in ["%", "1/x", "sq", "/", "C"]:
    createButton(j,16)
f1.pack(padx=10)

for i in range(7, 0, -3):
    f1 = Frame(root, bg="grey")
    for j in range(3):
        createButton(i+j,20)

    for j in range(2):
        createButton(charpos[i][j],20)

    f1.pack(padx=10)


f1 = Frame(root, bg="grey")
for j in ["00", "0", ".", "=", "+/-"]:
    createButton(j,17)
f1.pack(padx=10)

root.mainloop()
