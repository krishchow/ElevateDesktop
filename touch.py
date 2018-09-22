from selenium import webdriver
import time as T
import tkinter as tk
from threading import Thread
import sqlite3
import hashlib
from random import choice
from string import ascii_letters
import os
import tkinter.ttk as ttk
from Crypto.Cipher import AES
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

def registerPlatform(username, password, platform,key):
    conn = sqlite3.connect(r'data.db')
    cur = conn.cursor()
    while len(password)%16 != 0:
        password += ' '
    
    obj = AES.new(key)
    ciph = obj.encrypt(password)

    cur.execute('INSERT INTO platformLogins VALUES ("{0}","{1}","{2}")'.format(username, ciph.hex(), platform))
    conn.commit()
    conn.close()
    print('user created')
    return True

def addAccount(ID):
    top = tk.Toplevel()
    top.title('Please Input Account Details')
    header = tk.Frame(top)
    tk.Label(header,text="Please Input Account Details").pack(side='left')
    header.pack(side='top')
    combobox = tk.Frame(top,width=150)
    tkvar = tk.StringVar(top)
    choices = ['Presto','Library','Volunteer Toronto']
    radios = []
    def setVal():
            usernameEntry.config(state='normal')
            passwordEntry.config(state='normal')
            #conn = sqlite3.connect(r'data.db')
            #cur = conn.cursor()
            #cur.execute('SELECT username FROM platformLogins WHERE (id="{0}" AND platformID="{1}");'.format(ID,tkvar.get()))
            #val = list(cur.fetchone())
            #if val:
            #    usernameEntry.insert(0,val[0])
            return
    for i in choices:
        r = tk.Radiobutton(combobox, text=i, variable=tkvar, value=i, command=setVal)
        radios.append(r)
    for i in radios:
        i.pack(side='top',anchor='w')
    
    combobox.pack(side='left',fill='y')
    username = tk.Frame(top)
    tk.Label(username, text='Username:',width=15).pack(side='left')
    usernameEntry = tk.Entry(username,state='disabled')
    usernameEntry.pack(side='left')
    username.pack(side='top')
    password = tk.Frame(top)
    tk.Label(password, text='Password:',width=15).pack(side='left')
    passwordEntry = tk.Entry(password,state='disabled',show="*")
    passwordEntry.bind("<Enter>", lambda e: passwordEntry.configure(show=''))
    passwordEntry.bind("<Leave>", lambda e: passwordEntry.configure(show='*'))
    passwordEntry.pack(side='left')
    password.pack(side='top')
    
    def end():
        if not tkvar.get():
            return False
        val = registerPlatform(usernameEntry.get(),passwordEntry.get(),tkvar.get(),ID)
        if val:
            top.destroy()
            return
    
    tk.Button(top, text='Register',command=end).pack(side='top')

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
    #root.iconbitmap(img())
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
    passwordEntry = tk.Entry(password, show='*')
    passwordEntry.bind("<Enter>", lambda e: passwordEntry.configure(show=''))
    passwordEntry.bind("<Leave>", lambda e: passwordEntry.configure(show='*'))
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
    tk.Button(root, text="Exit",command=exit,anchor='e').pack(side='bottom')
    root.mainloop()

def loadMain(ID):
    root = tk.Tk()
    #root.iconbitmap(img())
    root.geometry('500x500')
    mainFrame = tk.Frame(root)
    header = tk.Label(mainFrame, text="Welcome the Toronto Library")
    header.pack()
    mainFrame.pack(side='top')
    bottomFrame = tk.Frame(root)
    def t():
        root.destroy()
        loadLogin()
    tk.Button(bottomFrame, text="Log Out", command=t).pack(side='right')
    tk.Button(bottomFrame, text="Add A New Account", command=lambda id=ID: addAccount(id)).pack(side='left')
    bottomFrame.pack(side='bottom',fill='x')
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
