from selenium import webdriver
import time as T
import tkinter as tk
from threading import Thread
import sqlite3

def launchBrowser(url):
    #flags
    b = webdriver.Chrome()
    return b

def loginUser(arr):
    top = tk.Toplevel()
    top.title('Please Login')
    header = tk.Frame(top)
    tk.Label(header,text="Please Login").pack(side='left')
    header.pack(side='top')
    username = tk.Frame(top)
    tk.Label(username, text='Username:').pack(side='left')
    usernameEntry = tk.Entry(username)
    usernameEntry.pack(side='left')
    username.pack(side='top')
    password = tk.Frame(top)
    tk.Label(password, text='Password:').pack(side='left')
    passwordEntry = tk.Entry(password)
    passwordEntry.pack(side='left')
    password.pack(side='top')
    def end():
        val = checkUser(usernameEntry.get(),passwordEntry.get())
        if val:
            top.destroy()
            arr.append(val[2])
            return
    tk.Button(top, text='Login',command=end).pack(side='top')
    

def registerUser():
    #return None
    pass

def loadFirst(session):
    print(1)
    pass

def loadFirstHelper(session):
    pass

def loadSecond(session):
    print(2)
    pass

def loadThird(session):
    print(3)
    pass

def checkUser(username, password):
    conn = sqlite3.connect(r'data.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM auth WHERE (username="{0}" AND password="{1}");'.format(username,password))
    val = cur.fetchone()
    if val:
        print(val)
        return val
    else:
        return False

def loadLogin():
    root = tk.Tk()
    root.geometry('500x500')
    mainFrame = tk.Frame(root)
    header = tk.Label(mainFrame, text="Please Login", font=("Times", 24, "bold"))
    header.pack()
    mainFrame.pack(side='top')
    username = tk.Frame(root)
    tk.Label(username, text='Username:',width=15).pack(side='left')
    usernameEntry = tk.Entry(username)
    usernameEntry.pack(side='left')
    username.pack(side='top',fill='x')
    password = tk.Frame(root)
    tk.Label(password, text='Password:',width=15).pack(side='left')
    passwordEntry = tk.Entry(password)
    passwordEntry.pack(side='left')
    password.pack(side='top',fill='x')

    def end():
        val = checkUser(usernameEntry.get(),passwordEntry.get())
        if val:
            print(val)
            root.destroy()
            loadMain(val[2])
            return
    tk.Button(root, text='Login',command=end).pack(side='top')
    root.mainloop()

def loadMain(ID):
    root = tk.Tk()
    root.geometry('500x500')
    mainFrame = tk.Frame(root)
    header = tk.Label(mainFrame, text="Welcome the Toronto Library")
    header.pack()
    mainFrame.pack(side='top')
    bodyFrame = tk.Frame(root)
    button1 = tk.Button(bodyFrame,text="hi",command=lambda id=ID: loadFirst(id))
    button2 = tk.Button(bodyFrame,command=lambda id=ID: loadSecond(id))
    button3 = tk.Button(bodyFrame,command=lambda id=ID: loadThird(id))
    button1.pack();button2.pack();button3.pack()
    bodyFrame.pack(fill='both')
    tk.mainloop()



loadLogin()
#b = webdriver.Chrome()



T.sleep(10)
#b.quit()
