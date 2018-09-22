from selenium import webdriver
import time as T
import tkinter as tk
from threading import Thread
import sqlite3
import hashlib
from random import choice
from string import ascii_letters
def launchBrowser(url):
    #flags
    b = webdriver.Chrome()
    return b

def register(un,pw):
    conn = sqlite3.connect(r'data.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM auth WHERE username="{0}"'.format(un))
    if cur.fetchone():
        print('fail:userexists')
        return False
    userID = ''
    while userID == '':
        userID=''.join(choice(ascii_letters) for i in range(16))
        cur.execute('SELECT * FROM auth WHERE id="{0}"'.format(userID))
        if cur.fetchone():
            userID = ''

    salt = ''.join(choice(ascii_letters) for i in range(12))
    m = hashlib.sha256()
    m.update(bytes(pw, 'utf-8'))
    m.update(bytes(salt, 'utf-8'))
    salted = m.hexdigest()
    cur.execute('INSERT INTO auth VALUES ("{0}","{1}","{2}","{3}")'.format(un,salt,salted,userID))
    conn.commit()
    conn.close()
    print('user created')
    return True

def registerUser():
    top = tk.Toplevel()
    top.title('Please Register')
    header = tk.Frame(top)
    tk.Label(header,text="Please Register").pack(side='left')
    header.pack(side='top')
    username = tk.Frame(top)
    tk.Label(username, text='Username:',width=15).pack(side='left')
    usernameEntry = tk.Entry(username)
    usernameEntry.pack(side='left')
    username.pack(side='top')
    password = tk.Frame(top)
    tk.Label(password, text='Password:',width=15).pack(side='left')
    passwordEntry = tk.Entry(password)
    passwordEntry.pack(side='left')
    password.pack(side='top')
    def end():
        val = register(usernameEntry.get(),passwordEntry.get())
        if val:
            top.destroy()
            return
    tk.Button(top, text='Register',command=end).pack(side='top')
    

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
    cur.execute('SELECT salt FROM auth WHERE (username="{0}");'.format(username))
    val = cur.fetchone()
    if not val:
        print('not found')
        return False
    val = list(val)[0]
    m = hashlib.sha256()
    m.update(bytes(password, 'utf-8'))
    m.update(bytes(val, 'utf-8'))
    salted = m.hexdigest()
    cur.execute('SELECT id FROM auth WHERE (username="{0}" and saltedhash="{1}");'.format(username, salted))
    done = cur.fetchone()
    if done:
        return done
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
            loadMain(list(val)[0])
            return
    buttonFrame = tk.Frame(root)
    tk.Button(buttonFrame, text='Login',command=end).pack(side='left')
    tk.Button(buttonFrame, text='Register',command=registerUser).pack(side='right')
    buttonFrame.pack(side='top')
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
