from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import tkinter as tk

objects = []
root = Tk()
root.withdraw()
root.title('Account_Storage_Details')
root.geometry("700x500")

# background_image=tk.PhotoImage("image1.png")
# background_label = tk.Label(root, image=background_image)
# background_label.place(x=-1, y=0, relwidth=1, relheight=1)


# photo = PhotoImage(file = "image1.png")
# w = Label(root, image=photo)
# w.grid()
# ent = Entry(root)
# ent.grid()
# ent.focus_set()

root.configure(background = "#5c0640")

class popupWindow(object):

    loop = False
    attempts = 0

    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title('Input Password')
        top.geometry('{}x{}'.format(250, 100))
        top.configure(background="#3e065c")
        top.resizable(width=False, height=False)
        self.l = Label(top, text=" Password: ", font=('times', 16, 'bold'), fg="#b51253",bg="green",justify=CENTER)
        self.l.pack()
        self.e = Entry(top, show='*', width=50)
        self.e.pack(pady=7)
        self.b = Button(top, text='Submit', command=self.cleanup, font=('times', 16),fg="purple",bg="#b51253")
        self.b.pack()

    def cleanup(self):
        self.value = self.e.get()
        access = '@moryso'

        if self.value == access:
            self.loop = True
            self.top.destroy()
            root.deiconify()
        else:
            self.attempts += 1
            if self.attempts == 5:
                root.quit()
            self.e .delete(0, 'end')
            messagebox.showerror('Incorrect Password', 'Incorrect password, attempts remaining: ' + str(5 - self.attempts))

class entity_add:

    def __init__(self, master, n, p, e):
        self.password = p
        self.name = n
        self.email = e
        self.window = master

    def write(self):
        f = open('details.txt', "a")
        n = self.name
        e = self.email
        p = self.password

        encryptedN = ""
        encryptedE = ""
        encryptedP = ""
        for letter in n:
            if letter == ' ':
                encryptedN += ' '
            else:
                encryptedN += chr(ord(letter) + 5)

        for letter in e:
            if letter == ' ':
                encryptedE += ' '
            else:
                encryptedE += chr(ord(letter) + 5)

        for letter in p:
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter) + 5)

        f.write(encryptedN + ',' + encryptedE + ',' + encryptedP + ', \n')
        f.close()


class entity_display:

    def __init__(self, master, n, e, p, i):
        self.password = p
        self.name = n
        self.email = e
        self.window = master
        self.i = i

        dencryptedN = ""
        dencryptedE = ""
        dencryptedP = ""
        for letter in self.name:
            if letter == ' ':
                dencryptedN += ' '
            else:
                dencryptedN += chr(ord(letter) - 5)

        for letter in self.email:
            if letter == ' ':
                dencryptedE += ' '
            else:
                dencryptedE += chr(ord(letter) - 5)

        for letter in self.password:
            if letter == ' ':
                dencryptedP += ' '
            else:
                dencryptedP += chr(ord(letter) - 5)

        self.label_name = Label(self.window, text=dencryptedN, font=('times', 14))
        self.label_email = Label(self.window, text=dencryptedE, font=('times', 14))
        self.label_pass = Label(self.window, text=dencryptedP, font=('times', 14))
        self.deleteButton = Button(self.window, text='X', fg='red', command=self.delete)

    def display(self):
        self.label_name.grid(row=6 + self.i, sticky=W)
        self.label_email.grid(row=6 + self.i, column=1)
        self.label_pass.grid(row=6 + self.i, column=2, sticky=E)
        self.deleteButton.grid(row=6 + self.i, column=3, sticky=E)

    def delete(self):
        answer = tkinter.messagebox.askquestion('Delete', 'Are you sure you want to delete this entry?')

        if answer == 'yes':
            for i in objects:
                i.destroy()

            f = open('details.txt', 'r')
            lines = f.readlines()
            f.close()

            f = open('details.txt', "w")
            count = 0

            for line in lines:
                if count != self.i:
                    f.write(line)
                    count += 1

            f.close()
            readfile()

    def destroy(self):
        self.label_name.destroy()
        self.label_email.destroy()
        self.label_pass.destroy()
        self.deleteButton.destroy()


def onsubmit():
    m = email.get()
    p = password.get()
    n = name.get()
    e = entity_add(root, n, p, m)
    e.write()
    name.delete(0, 'end')
    email.delete(0, 'end')
    password.delete(0, 'end')
    messagebox.showinfo('Added Entity', 'Successfully Added, \n' + 'Name: ' + n + '\nEmail: ' + m + '\nPassword: ' + p)
    readfile()


def clearfile():
    f = open('details.txt', "w")
    f.close()


def readfile():
    f = open('details.txt', 'r')
    count = 0

    for line in f:
        entityList = line.split(',')
        e = entity_display(root, entityList[0], entityList[1], entityList[2], count)
        objects.append(e)
        e.display()
        count += 1
    f.close()


m = popupWindow(root)

entity_label = Label(root, text='Add Entity', font=('times', 18))
entity_label.grid(columnspan=3, row=0)
name_label = Label(root, text='Name: ', font=('times', 16))
name_label.grid(row=1, sticky=E, padx=3)
email_label = Label(root, text='Email: ', font=('times', 16))
email_label.grid(row=2, sticky=E, padx=3)
pass_label = Label(root, text='Password: ', font=('times', 16))
pass_label.grid(row=3, sticky=E, padx=3)


name = Entry(root, font=('times', 16))
name.grid(columnspan=3, row=1, column=1, padx=2, pady=2, sticky=W)
email = Entry(root, font=('times', 16))
email.grid(columnspan=3, row=2, column=1, padx=2, pady=2, sticky=W)
password = Entry(root, show='*', font=('times', 16))
password.grid(columnspan=3, row=3, column=1, padx=2, pady=2, sticky=W)
submit = Button(root, text='Add Email', command=onsubmit, font=('times', 16))
submit.grid(columnspan=3, pady=4)


name_label2 = Label(root, text='Name: ', font=('times', 16))
name_label2.grid(row=5)
email_label2 = Label(root, text='Email: ', font=('times', 16))
email_label2.grid(row=5, column=1)
pass_label2 = Label(root, text='Password: ', font=('times', 16))
pass_label2.grid(row=5, column=2)

readfile()

root.mainloop()

if __name__ == '__main__':
    print("Account Storage")
