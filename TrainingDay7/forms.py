import tkinter as tk

'''form1 = tk.Tk()
form1.title("My First Form")
form1.mainloop()

form2 = tk.Tk()
form2.title("My Second Form")
myLabel2 = tk.Label(form2, text="This is a Label")
myLabel2.pack()

form2.mainloop()

form3 = tk.Tk()
form3.title("My Third Form")
myLabel3 = tk.Label(form3, text="This is a Label", width=25, height=10, bg="red", font="TimesNewRoman 10 bold italic")
myLabel3.pack()

myLabel31 = tk.Label(form3, text="This is also a Label", bg="blue", fg="white", font="30", justify="right")
myLabel31.pack()

form3.mainloop()'''

'''def setFullName():
    fName = firstEntry.get()
    lName = secondEntry.get()

    thirdEntry.insert(0, fName + " " + lName)


form4 = tk.Tk()
form4.title("Entry Text Boxes")
firstLabel = tk.Label(form4, text="First Name:")
firstEntry = tk.Entry(form4, relief="raised")
firstLabel.grid(row=0, column=0)
firstEntry.grid(row=0, column=1)

secondLabel = tk.Label(form4, text="Last Name:")
secondEntry = tk.Entry(form4, relief="groove")
secondLabel.grid(row=1, column=0, padx=15, pady=15)
secondEntry.grid(row=1, column=1, padx=15, pady=15)

thirdLabel = tk.Label(form4, text="Full Name:")
thirdEntry = tk.Entry(form4, relief="ridge")
thirdLabel.grid(row=2, column=0, padx=15, pady=15)
thirdEntry.grid(row=2, column=1, padx=15, pady=15)

fullNameBtn = tk.Button(form4, text="Full Name", command=setFullName)
fullNameBtn.grid(columnspan=2, padx=15, pady=15)
form4.mainloop()'''


def registerUser():
    doneForm = tk.Tk()
    form.title("Successfully Registered!")
    fName = fNameEntry.get()
    lName = lNameEntry.get()
    user = userNameEntry.get()
    email = emailEntry.get()

    myLabel = tk.Label(doneForm, text="You have been successfully registered, " + fName + lName + "!")
    myLabel.pack()

    myLabel2 = tk.Label(doneForm, text="Please verify your email at:  " + email)
    myLabel2.pack()

    myLabel3 = tk.Label(doneForm, text="Please login using your username '" + user + "' after verifying your Email Address")
    myLabel3.pack()


form = tk.Tk()
form.title("Registration Form")
fNameLabel = tk.Label(form, text="First Name:")
fNameEntry = tk.Entry(form)
fNameLabel.grid(row=0, column=0, padx=10, pady=10)
fNameEntry.grid(row=0, column=1, padx=10, pady=10)

lNameLabel = tk.Label(form, text="Last Name:")
lNameEntry = tk.Entry(form)
lNameLabel.grid(row=1, column=0, padx=10, pady=10)
lNameEntry.grid(row=1, column=1, padx=10, pady=10)

userNameLabel = tk.Label(form, text="UserName:")
userNameEntry = tk.Entry(form)
userNameLabel.grid(row=2, column=0, padx=10, pady=10)
userNameEntry.grid(row=2, column=1, padx=10, pady=10)

passNameLabel = tk.Label(form, text="PassWord:")
passNameEntry = tk.Entry(form)
passNameLabel.grid(row=3, column=0, padx=10, pady=10)
passNameEntry.grid(row=3, column=1, padx=10, pady=10)

emailLabel = tk.Label(form, text="Email Address:")
emailEntry = tk.Entry(form)
emailLabel.grid(row=4, column=0, padx=10, pady=10)
emailEntry.grid(row=4, column=1, padx=10, pady=10)

contactLabel = tk.Label(form, text="Contact Number:")
contactEntry = tk.Entry(form)
contactLabel.grid(row=5, column=0, padx=10, pady=10)
contactEntry.grid(row=5, column=1, padx=10, pady=10)

fullNameBtn = tk.Button(form, text="Register", command=registerUser)
fullNameBtn.grid(columnspan=2, padx=15, pady=15)
form.mainloop()
