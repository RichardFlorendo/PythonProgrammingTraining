import tkinter as tk
from tkinter import *
from tkinter import messagebox

'''filename = ''


def closefile():
    textArea.delete('1.0', tk.END)


def savefileas():
    save_text_as = filedialog.asksaveasfile(mode='w', defaultextension='.txt')

    if save_text_as:
        text_to_save = textArea.get('1.0', 'end-1c')
        save_text_as.write(text_to_save)
        save_text_as.close()
    else:
        messagebox.showinfo("Error", "Cancelled")


def savefile():
    global filename

    if filename:
        text_area_text = textArea.get('1.0', 'end-1c')
        save_text = open(filename, 'w')
        save_text.write(text_area_text)
        save_text.close()
    else:
        messagebox.showinfo("Error", "No File Open")


def openfile():
    global filename

    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Open File",
                                          filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))

    textArea.delete('1.0', tk.END)
    try:
        if filename:
            the_file = open(filename)
            for line in the_file.readlines():
                # text_line = parseline(line)
                textArea.insert(tk.END, line + '\n')

            the_file.close()
        elif filename == '':
            messagebox.showinfo("Cancel", "You clicked Cancel")
    except IOError:
        messagebox.showinfo("Error", "Could not open file")
    print(filename)


def parseline(the_line):
    parsed_line = the_line.strip()
    space_pos = parsed_line.rfind(' ')
    new_text_line = parsed_line[space_pos:] + ", " + parsed_line[:space_pos]
    return new_text_line.strip()


form = tk.Tk()
form.title("Python Menus")

menuBar = tk.Menu(form)

fileMenuItems = tk.Menu(menuBar, tearoff=0)
fileMenuItems.add_command(label="Open", command=openfile)
fileMenuItems.add_command(label="Save", command=savefile)
fileMenuItems.add_command(label="Save As", command=savefileas)
fileMenuItems.add_command(label="Close", command=closefile)
fileMenuItems.add_separator()
fileMenuItems.add_command(label="Quit", command=form.quit)
menuBar.add_cascade(label="File", menu=fileMenuItems)

editMenu = tk.Menu(menuBar, tearoff=0)
editMenu.add_command(label="Cut", command=openfile)
editMenu.add_command(label="Copy", command=openfile)
editMenu.add_command(label="Paste", command=openfile)
editMenu.add_command(label="Edit", command=openfile)
menuBar.add_cascade(label="Edit", menu=editMenu)

textArea = tk.Text(form, height=12, width=80, wrap=tk.WORD)
textArea.pack()

scrollV = tk.Scrollbar(form, orient=tk.VERTICAL)
scrollV.config(command=textArea.yview)
textArea.configure(yscrollcommand=scrollV.set)
scrollV.pack(side=tk.RIGHT, fill=tk.Y)

scrollH = tk.Scrollbar(form, orient=tk.HORIZONTAL)
scrollH.config(command=textArea.yview)
textArea.configure(yscrollcommand=scrollH.set)
scrollH.pack(side=tk.BOTTOM, fill=tk.X)

form.config(menu=menuBar)

form.mainloop()
'''

'''def aedtousd():
    aed = float(aedentry1.get())

    result = aed * 0.26
    usdentry1.insert(0, f"{result} USD")


def usdtoaed():
    usd = float(aedentry1.get())

    result = usd * 3.67
    usdentry2.insert(0, f"{result} AED")


form = tk.Tk()
form.title('Currency Converter')

toplabel = tk.Label(form, text='Currency Converter')
toplabel.grid(row=0, column=3)

sublabel1 = tk.Label(form, text='AED to USD Converter')
sublabel1.grid(row=1, column=1, padx=20, pady=20)

aedlabel1 = tk.Label(form, text='Dirhams', bg="red", foreground="white")
aedlabel1.grid(row=2, column=0, padx=10, pady=10)
aedentry1 = tk.Entry(form)
aedentry1.grid(row=2, column=1, padx=10, pady=10)

usdlabel1 = tk.Label(form, text='Dollars', bg="blue", foreground="white")
usdlabel1.grid(row=3, column=0, padx=10, pady=10)
usdentry1 = tk.Entry(form)
usdentry1.grid(row=3, column=1, padx=10, pady=10)

convertbutton1 = tk.Button(form, text='Convert', command=aedtousd)
convertbutton1.grid(row=4, columnspan=2, padx=15, pady=15)


sublabel2 = tk.Label(form, text='USD to AED Converter')
sublabel2.grid(row=1, column=5, padx=20, pady=20)

aedlabel2 = tk.Label(form, text='Dollars', bg="blue", foreground="white")
aedlabel2.grid(row=2, column=4, padx=10, pady=10)
aedentry2 = tk.Entry(form)
aedentry2.grid(row=2, column=5, padx=10, pady=10)

usdlabel2 = tk.Label(form, text='Dirhams', bg="red", foreground="white")
usdlabel2.grid(row=3, column=4, padx=10, pady=10)
usdentry2 = tk.Entry(form)
usdentry2.grid(row=3, column=5, padx=10, pady=10)

convertbutton2 = tk.Button(form, text='Convert', command=usdtoaed)
convertbutton2.grid(row=4, column=5, padx=15, pady=15)

form.mainloop()'''


def CelstoFahr():
    cel = float(celentry1.get())
    result = (cel * 9/5) + 32
    fahrentry1.insert(0, f"{result}")


def FahrtoCels():
    fahr = float(fahrentry2.get())
    result = (fahr - 32) * 5/9
    celentry2.insert(0, f"{result}")


form = tk.Tk()
form.title('Convert Between Celsius and Fahrenheit')
form.geometry('700x300')
form.config(bg='white')

Topform = Frame(form, width=700, bd=1, relief=SOLID)
Topform.pack()

l = Label(Topform, text="Celsius and Fahrenheit Converter")
l.pack()

BottomForm = Frame(form, width=700, bg='white')
BottomForm.pack()

BottomLeft = Frame(BottomForm, width=250, bd=1, relief=SOLID)
BottomLeft.pack(side=LEFT, pady=10)

BottomRight = Frame(BottomForm, width=250, bd=1, relief=SOLID)
BottomRight.pack(side=RIGHT, padx=10, pady=10)


label1 = Label(BottomLeft, text="Celsius to Fahrenheit")
label1.grid(row=0, column=0, padx=15, pady=15)

cellabel1 = Label(BottomLeft, text="Celsius")
cellabel1.grid(row=1, column=0, padx=10, pady=10)
celentry1 = Entry(BottomLeft)
celentry1.grid(row=1, column=1, padx=10, pady=10)

fahrlabel1 = Label(BottomLeft, text="Fahrenheit")
fahrlabel1.grid(row=2, column=0, padx=10, pady=10)
fahrentry1 = Entry(BottomLeft)
fahrentry1.grid(row=2, column=1, padx=10, pady=10)

convertbutton1 = Button(BottomLeft, text="Convert", command=CelstoFahr)
convertbutton1.grid(row=3, column=1, padx=15, pady=15)


label2 = Label(BottomRight, text="Fahrenheit to Celsius")
label2.grid(row=0, column=0, padx=15, pady=15)

fahrlabel2 = Label(BottomRight, text="Fahrenheit")
fahrlabel2.grid(row=1, column=0, padx=10, pady=10)
fahrentry2 = Entry(BottomRight)
fahrentry2.grid(row=1, column=1, padx=10, pady=10)

cellabel2 = Label(BottomRight, text="Celsius")
cellabel2.grid(row=2, column=0, padx=10, pady=10)
celentry2 = Entry(BottomRight)
celentry2.grid(row=2, column=1, padx=10, pady=10)

convertbutton2 = Button(BottomRight, text="Convert", command=FahrtoCels)
convertbutton2.grid(row=3, column=1, padx=15, pady=15)

form.mainloop()