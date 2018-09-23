import tkinter as tk
import tkinter.ttk as ttk
from touch import checkUser,registerPlatform,register
from browserFunctions import loadFirst,loadSecond,loadThird
import sqlite3

class Application():
    def __init__(self):
        self.root = tk.Tk()
        self.root.style = ttk.Style()
        self.root.style.theme_use('clam')
        self.root.geometry('500x500')
        s = ttk.Style()
        s.configure('Main.TButton', foreground=foreground, background='#F2F1EF')
        ttk.Style().layout("Main.TButton", [("Button.focus", None),("Button.background", {"children":[("Button.button", {"children":[("Button.padding", {"children":[("Button.label", {"side": "left", "expand": 1})]})]})]})])
        self.bg = background
        self.loadLogin()
        tk.mainloop()

    def renderLogin(self):
        root = tk.Frame(self.root)
        mainFrame = tk.Frame(root)
        header = ttk.Label(mainFrame, text="Please Login", font=("Times", 24, "bold"))
        header.pack()
        mainFrame.pack(side='top')
        username = tk.Frame(root)
        ttk.Label(username, text='Username:',width=10,background=self.bg).pack(side='left')
        usernameEntry = ttk.Entry(username)
        usernameEntry.pack(side='left')
        username.pack(side='top',fill='x')
        password = tk.Frame(root)
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
        buttonFrame = tk.Frame(root)
        ttk.Button(buttonFrame, text='Login',command=end,style='Main.TButton').pack(side='left')
        ttk.Button(buttonFrame, text='Register',command=registerUser,style='Main.TButton').pack(side='right')
        buttonFrame.pack(side='top')
        ttk.Button(root, text="Exit",command=exit,anchor='e',style='Main.TButton').pack(side='bottom')
        root.pack(fill='both',expand=True)
    
    def loadMain(self, ID):
        root = tk.Frame(self.root)
        mainFrame = tk.Frame(root)
        header = ttk.Label(mainFrame, text="Welcome the Toronto Library",background=self.bg, font=("Times", 24, "bold"))
        header.pack()
        mainFrame.pack(side='top')
        bottomFrame = tk.Frame(root)
        def t():
            root.pack_forget()
            self.loadLogin()
        ttk.Button(bottomFrame, text="Log Out", command=t,style='Main.TButton').pack(side='right')
        ttk.Button(bottomFrame, text="Add A New Account", command=lambda id=ID: addAccount(id),style='Main.TButton').pack(side='left')
        bottomFrame.pack(side='bottom',fill='x')
        bodyFrame = tk.Frame(root)
        button1 = ttk.Button(bodyFrame,text="Presto",command=lambda id=ID: loadFirst(id),style='Main.TButton')
        button2 = ttk.Button(bodyFrame,text="Library",command=lambda id=ID: loadSecond(id),style='Main.TButton')
        button3 = ttk.Button(bodyFrame,text="Childcare",command=lambda id=ID: loadThird(id),style='Main.TButton')
        button1.pack(pady=20);button2.pack(pady=20);button3.pack(pady=20)
        bodyFrame.pack(fill='both')
        root.pack(fill='both',expand=True)

    def loadLogin(self):
        root = tk.Frame(self.root)
        mainFrame = tk.Frame(root)
        header = ttk.Label(mainFrame, text="Please Login", font=("Times", 24, "bold"),background=self.bg)
        header.pack()
        mainFrame.pack(side='top')
        username = tk.Frame(root)
        ttk.Label(username, text='Username:',width=8,background=self.bg).pack(side='left')
        usernameEntry = ttk.Entry(username)
        usernameEntry.pack(side='right')
        username.pack(side='top')
        password = tk.Frame(root)
        ttk.Label(password, text='Password:',width=8,background=self.bg).pack(side='left')
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
        buttonFrame = tk.Frame(root)
        ttk.Button(buttonFrame, text='Login',command=end,style='Main.TButton').pack(side='left',pady=5)
        ttk.Button(buttonFrame, text='Register',command=registerUser,style='Main.TButton').pack(side='right',pady=5)
        buttonFrame.pack(side='top')
        ttk.Button(root, text="Exit",command=exit,style='Main.TButton').pack(side='bottom')
        root.pack(fill='both',expand=True)

def addAccount(ID):
    top = tk.Toplevel()
    top.title('Please Input Account Details')
    header = tk.Frame(top)
    ttk.Label(header,text="Please Input Account Details",background=background).pack(side='left')
    header.pack(side='top')
    combobox = tk.Frame(top,width=150)
    tkvar = tk.StringVar(top)
    choices = ['Presto','Library','Volunteer Toronto']
    radios = []
    def setVal():
            usernameEntry.config(state='normal')
            passwordEntry.config(state='normal')
            usernameEntry.delete('0','end')
            conn = sqlite3.connect(r'data.db')
            cur = conn.cursor()
            cur.execute('SELECT username FROM platformLogins WHERE (id="{0}" AND platformID="{1}");'.format(ID,tkvar.get()))
            val = cur.fetchone()
            if val:
                usernameEntry.insert(0,list(val)[0])
            return
    for i in choices:
        r = tk.Radiobutton(combobox, text=i, variable=tkvar, value=i, command=setVal)
        radios.append(r)
    for i in radios:
        i.pack(side='top',anchor='w')
    
    combobox.pack(side='left',fill='y')
    username = tk.Frame(top)
    ttk.Label(username, text='Username:',width=15,background=background).pack(side='left')
    usernameEntry = ttk.Entry(username,state='disabled')
    usernameEntry.pack(side='left')
    username.pack(side='top')
    password = tk.Frame(top)
    ttk.Label(password, text='Password:',width=15,background=background).pack(side='left')
    passwordEntry = ttk.Entry(password,state='disabled',show="*")
    passwordEntry.bind("<Enter>", lambda e: passwordEntry.configure(show=''))
    passwordEntry.bind("<Leave>", lambda e: passwordEntry.configure(show='*'))
    passwordEntry.pack(side='left')
    password.pack(side='top')
    
    def end():
        if not tkvar.get():
            return False
        conn = sqlite3.connect(r'data.db')
        cur = conn.cursor()
        cur.execute('SELECT salt FROM auth WHERE id="{0}";'.format(ID))
        salt = list(cur.fetchone())[0]
        val = registerPlatform(usernameEntry.get(),passwordEntry.get(),tkvar.get(),salt,ID)
        if val:
            top.destroy()
            return
    
    ttk.Button(top, text='Register',command=end,style='Main.TButton').pack(side='right')

def registerUser():
    top = tk.Toplevel()
    top.title('Please Register')
    header = tk.Frame(top)
    ttk.Label(header,text="Please Register",background=background).pack(side='left')
    header.pack(side='top')
    username = tk.Frame(top)
    ttk.Label(username, text='Username:',width=15,background=background).pack(side='left')
    usernameEntry = ttk.Entry(username)
    usernameEntry.pack(side='left')
    username.pack(side='top')
    password = tk.Frame(top)
    ttk.Label(password, text='Password:',width=15,background=background).pack(side='left')
    passwordEntry = ttk.Entry(password)
    passwordEntry.pack(side='left')
    password.pack(side='top')
    def end():
        val = register(usernameEntry.get(),passwordEntry.get())
        if val:
            top.destroy()
            return
    ttk.Button(top, text='Register',command=end,style='Main.TButton').pack(side='top')

if __name__ == '__main__':
    background = '#ffffff'    
    foreground = '#000000'
    a = Application()