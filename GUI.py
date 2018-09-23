import tkinter as tk
import tkinter.ttk as ttk
from touch import checkUser,registerPlatform,register
from browserFunctions import loadFirst,loadSecond,loadThird
from manageDB import DBManager
from GUIHelper import *
import sqlite3
import os

class Application():
    def __init__(self):
        self.sessionID = ''
        self.db = DBManager()
        self.db.CreateTables()
        self.root = tk.Tk()
        self.root.style = ttk.Style()
        self.root.style.theme_use('clam')
        self.root.geometry('500x500')
        s = ttk.Style()
        s.configure('Main.TButton', foreground=foreground, background=blueBackground)
        ttk.Style().layout("Main.TButton", [("Button.focus", None),("Button.background", {"children":[("Button.button", {"children":[("Button.padding", {"children":[("Button.label", {"side": "left", "expand": 1})]})]})]})])
        ttk.Style().map("Main.TButton", foreground=[('active', 'white')], background=[('active', '#013243')])
        self.bg = background
        self.loadLogin()
        tk.mainloop()

    def renderLogin(self):
        root = tk.Frame(self.root, background=self.bg)
        mainFrame = tk.Frame(root, background=self.bg)
        header = ttk.Label(mainFrame, text="Please Login", font=("Times", 24, "bold"))
        header.pack()
        mainFrame.pack(side='top', background=self.bg)
        username = tk.Frame(root)
        ttk.Label(username, text='Username:',width=10,background=self.bg).pack(side='left')
        usernameEntry = ttk.Entry(username)
        usernameEntry.pack(side='left')
        username.pack(side='top',fill='x')
        password = tk.Frame(root, background=self.bg)
        ttk.Label(password, text='Password:',width=10,background=self.bg).pack(side='left')
        passwordEntry = ttk.Entry(password, show='*')
        passwordEntry.bind("<Enter>", lambda e: passwordEntry.configure(show=''))
        passwordEntry.bind("<Leave>", lambda e: passwordEntry.configure(show='*'))
        passwordEntry.pack(side='left')
        password.pack(side='top',fill='x')

        def end():
            val = checkUser(usernameEntry.get(),passwordEntry.get())
            if val:
                print(val)
                root.pack_forget()
                self.loadMain(list(val)[0])
                return
        buttonFrame = tk.Frame(root, background=self.bg)
        ttk.Button(buttonFrame, text='Login',command=end,style='Main.TButton').pack(side='left')
        ttk.Button(buttonFrame, text='Register',command=lambda d = self.db: registerUser(d),style='Main.TButton').pack(side='right')
        buttonFrame.pack(side='top')
        ttk.Button(root, text="Exit",command=exit,anchor='e',style='Main.TButton').pack(side='bottom')
        root.pack(fill='both',expand=True)
    
    def loadMain(self, ID):
        root = tk.Frame(self.root, background=self.bg)
        mainFrame = tk.Frame(root, background=self.bg)
        header = ttk.Label(mainFrame, text="Welcome the Toronto Library",background=self.bg, font=("Times", 24, "bold"))
        header.pack()
        mainFrame.pack(side='top')
        bottomFrame = tk.Frame(root, background=self.bg)
        def t():
            root.pack_forget()
            self.loadLogin()
        ttk.Button(bottomFrame, text="Log Out", command=t,style='Main.TButton').pack(side='right')
        ttk.Button(bottomFrame, text="Add A New Account", command=lambda id=ID: addAccount(id,self.db),style='Main.TButton').pack(side='left')
        bottomFrame.pack(side='bottom',fill='x')
        bodyFrame = tk.Frame(root, background=self.bg)
        button1 = ttk.Button(bodyFrame,text="Presto",command=lambda id=ID: loadFirst(id),style='Main.TButton')
        button2 = ttk.Button(bodyFrame,text="Library",command=lambda id=ID: loadSecond(id),style='Main.TButton')
        button3 = ttk.Button(bodyFrame,text="Volunteer Toronto",command=lambda id=ID: loadThird(id),style='Main.TButton')
        button1.pack(pady=20);button2.pack(pady=20);button3.pack(pady=20)
        bodyFrame.pack(fill='both')
        root.pack(fill='both',expand=True)

    def loadLogin(self):
        width = 10 if os.name=='nt' else 8
        root = tk.Frame(self.root, background=self.bg)
        mainFrame = tk.Frame(root, background=self.bg)
        header = ttk.Label(mainFrame, text="Please Login", font=("Times", 24, "bold"),background=self.bg)
        header.pack()
        mainFrame.pack(side='top')
        username = tk.Frame(root, background=self.bg)
        ttk.Label(username, text='Username:',width=width,background=self.bg).pack(side='left')
        usernameEntry = ttk.Entry(username)
        usernameEntry.pack(side='right')
        username.pack(side='top')
        password = tk.Frame(root, background=self.bg)
        ttk.Label(password, text='Password:',width=width,background=self.bg).pack(side='left')
        passwordEntry = ttk.Entry(password, show='*')
        passwordEntry.bind("<Enter>", lambda e: passwordEntry.configure(show=''))
        passwordEntry.bind("<Leave>", lambda e: passwordEntry.configure(show='*'))
        passwordEntry.pack(side='right')
        password.pack(side='top')

        def end():
            val = checkUser(usernameEntry.get(),passwordEntry.get())
            if val:
                print(val)
                root.pack_forget()
                self.loadMain(list(val)[0])
                return
        buttonFrame = tk.Frame(root, background=self.bg)
        ttk.Button(buttonFrame, text='Login',command=end,style='Main.TButton').pack(side='left',pady=5)
        ttk.Button(buttonFrame, text='Register',command=lambda d=self.db: registerUser(d),style='Main.TButton').pack(side='right',pady=5)
        buttonFrame.pack(side='top')
        ttk.Button(root, text="Exit",command=exit,style='Main.TButton').pack(side='bottom')
        root.pack(fill='both',expand=True)

if __name__ == '__main__':
    background = '#ffffff'
    foreground = '#ffffff'
    blueBackground = '#0968a3'
    a = Application()
