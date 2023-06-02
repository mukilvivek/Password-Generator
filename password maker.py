from tkinter import *
import secrets
import string


letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars
length = 10

while True:
    password = ''
    for i in range(length):
        password += ''.join(secrets.choice(alphabet))
    if (any(char in special_chars for char in password) and any(char in digits for char in password) and sum(char in letters for char in password)>=7 and password[0].isalpha()):
          break

password = password.lower()
password = password.capitalize()
#print(password)


root = Tk()
#e=Entry(root)
#e.pack()

def Clicker():
    myLabel2 = Label( text=password)
    myLabel2.pack()

myButton = Button( text="Click here to generate password", command=Clicker)
myButton.pack()

#myLabel = Label(root, text="Hello World!")
#myLabel1 = Label(root, text="My name is Mukil")
#myLabel.grid(row=0,column=0)
#myLabel1.grid(row=1,column=0)
root.mainloop()