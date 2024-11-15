from tkinter import *
root = Tk()

root.title("PRIVATE VARIABLE LOGIN PAGE")
root.geometry('600x500')

label = Label(root, text = "Name: ")
label.place(relx=0.4, rely=0.1,anchor=CENTER)
name_txt = Entry(root)
name_txt.place(relx=0.6, rely = 0.1, anchor=CENTER)

label1 = Label(root, text = "Password: ")
label1.place(relx=0.4, rely=0.25,anchor=CENTER)
password_txt = Entry(root)
password_txt.place(relx=0.6, rely = 0.25, anchor=CENTER)

label2 = Label(root, text = "Captcha: ")
label2.place(relx=0.4, rely=0.4,anchor=CENTER)
Captcha_txt = Entry(root)
Captcha_txt.place(relx=0.6, rely = 0.4, anchor=CENTER)

label3 = Label(root)
label3.place(relx=0.5,rely=0.7,anchor=CENTER)

label4 = Label(root)
label4.place(relx=0.5,rely=0.8,anchor=CENTER)

label5 = Label(root)
label5.place(relx=0.5,rely=0.9,anchor=CENTER)

class userDB():
    def __init__(self):
        self.__username = "Vihaan"
        self.__password = "Vihaan77#$"
        self.captcha = "GHr657"
        
    def showUser(self):
        label3["text"] = "Name: "+self.__username
        label4["text"] = "Password: "+self.__password
        label5["text"] = "Captcha: "+self.captcha
user = userDB()
def addUser():
    global user
    user.username = name_txt.get()
    user.password = password_txt.get()
    user.captcha = Captcha_txt.get()
    print("Details Updated")
btn = Button(root, text="Update Login Details", command=addUser)
btn.place(relx=0.3,rely=0.5,anchor = CENTER)
btn1 = Button(root, text="Show Profile", command=user.showUser)
btn1.place(relx=0.7,rely=0.5,anchor = CENTER)
root.mainloop()