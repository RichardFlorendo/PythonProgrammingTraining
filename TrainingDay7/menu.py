import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
def openfile():
    fileName = filedialog.askopenfilename(initialdir="/",
                                          title="Open File",
                                          filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    try:
        if fileName:
            the_file = open(fileName)
            for line in the_file.readlines():
                text_line = parseline(line)
                textArea.insert(tk.END, text_line + '\n')

            the_file.close()
        elif fileName == '':
            messagebox.showinfo("Cancel", "You clicked Cancel")
    except IOError:
        messagebox.showinfo("Error", "Could not open file")
    print(fileName)


def parseline(the_line):
    parsed_line = the_line.strip()
    space_pos = parsed_line.rfind(' ')
    new_text_line = parsed_line[space_pos:] + ", " + parsed_line[:space_pos]
    return new_text_line.strip()


form = tk.Tk()
form.title("Python Menus")

menuBar =tk.Menu(form)

fileMenuItems = tk.Menu(menuBar, tearoff=0)
fileMenuItems.add_command(label="Open", command=openfile)
fileMenuItems.add_command(label="Save", command=openfile)
fileMenuItems.add_command(label="Save As", command=openfile)
fileMenuItems.add_command(label="Close", command=openfile)
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
#Continued on Day 8