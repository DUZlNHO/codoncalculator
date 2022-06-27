from tkinter import *
from tkinter.ttk import *

from requests import delete
from dna import *

window = Tk()
window.geometry('1366x728')
window.columnconfigure(0, weight=100)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=100)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=100)
window.rowconfigure(0, weight=70)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)

window.title("Calculadora de Aminoácidos")

def clicked(): #button click
    dr = str(dra.get())
    ct = str(cta.get())
    seq = txt.get()
    acidos = dna(dr, ct, seq)
    lbl.configure(text=acidos)

def enter(event):
    clicked()
    
def blocktoggle(): #toggle rna selectors
    if str(dra.get()) == 'rna':
        chk3['state'] = DISABLED
        chk4['state'] = DISABLED
    else:
        chk3['state'] = NORMAL
        chk4['state'] = NORMAL

def callback(input):
    if input[-1] == 'a' or input[-1] == 'c' or input[-1] == 'g' or input[-1] == 'u' or input[-1] == 't' \
    or input[-1] == 'A' or input[-1] == 'C' or input[-1] == 'G' or input[-1] == 'U' or input[-1] == 'T' or input[-1] == ' ':
        return True
    elif input == '':
        return True
    else:
        return False

lbl = Label(window, text="", font=("Arial", 15))

#dna/rna selector
dra = StringVar()
cta = StringVar()
chk1 = Radiobutton(window, text='DNA', value='dna', variable=dra, command=blocktoggle)
chk2 = Radiobutton(window, text='RNA', value='rna', variable=dra, command=blocktoggle)
chk3 = Radiobutton(window, text='5 -> 3', value='5', variable=cta)
chk4 = Radiobutton(window, text='3 -> 5', value='3', variable=cta)

txt = Entry(window, width=20)

style = Style()
style.theme_use("default")

style.map('btnstyle.TButton',
    foreground=[('!active', 'black'),('active', 'black')],
    background=[ ('!active','white'),('active', 'grey75')],
    borderwidth=[('!active', 1),('active', 2)],
    )

#button
btn = Button(window, text="Calcular", style='btnstyle.TButton', command=clicked)

#binds
window.bind('<Return>', enter)

#positions
lbl.grid(column=0, row=0, columnspan=6)

chk1.grid(column=1, row=1, sticky=SE) #dna
chk2.grid(column=1, row=2, sticky=NE) #rna
chk3.grid(column=2, row=1, sticky=SW) #5 -> 3
chk4.grid(column=2, row=2, sticky=N+W+E) #3 -> 5

txt.grid(column=3, row=2, sticky=N+W+E)
reg = window.register(callback)
txt.config(validate="key", validatecommand=(reg, '%P'))

btn.grid(column=4, row=2, sticky=N)

window.mainloop()