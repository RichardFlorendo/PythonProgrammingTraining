'''import SecondFile
import datetime
import calendar


#from SecondFile import subject

#SecondFile.display_name("John Doe")

studentName = SecondFile.display_name
studentName("Johnny Does")

dateNow = datetime.date.today()
print(dateNow)

isLeapYear = calendar.isleap(2023)

if isLeapYear:
    print("2023 is a leap year")
else:
    print("2023 is not a leap year")'''

import tkinter as tk
from PIL import ImageTk, Image

form = tk.Tk()
form.title("Rotate Image")

imageName = "dog.jpg"
openImage = Image.open(imageName)
rotatedImage = openImage.rotate(90)

img = ImageTk.PhotoImage(rotatedImage)

labelWidget = tk.Label(form, image=img)
labelWidget.pack()

form.mainloop()