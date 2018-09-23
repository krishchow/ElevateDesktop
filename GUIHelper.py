import tkinter as tk
import tkinter.ttk as ttk
from touch import registerPlatform,register


background = '#ffffff'
foreground = '#000000'
def addAccount(ID,db):
    top = tk.Toplevel()
    top['bg'] = background
    top.title('Please Input Account Details')
    header = tk.Frame(top, background=background)
    ttk.Label(header,text="Please Input Account Details",background=background, font=("Times", 16, "bold")).pack(side='left')
    header.pack(side='top')
    combobox = tk.Frame(top,width=150, background=background)
    tkvar = tk.StringVar(top)
    choices = ['Presto','Library','Volunteer Toronto']
    radios = []
    def setVal():
            usernameEntry.config(state='normal')
            passwordEntry.config(state='normal')
            usernameEntry.delete('0','end')
            passwordEntry.delete('0','end')
            db.cur.execute('SELECT username FROM platformLogins WHERE (id="{0}" AND platformID="{1}");'.format(ID,tkvar.get()))
            val = db.cur.fetchone()
            if val:
                usernameEntry.insert(0,list(val)[0])
            return
    for i in choices:
        r = tk.Radiobutton(combobox, text=i, variable=tkvar, value=i, command=setVal, background=background)
        radios.append(r)
    for i in radios:
        i.pack(side='top',anchor='w')
    
    combobox.pack(side='left',fill='y')
    username = tk.Frame(top, background=background)
    ttk.Label(username, text='Username:',width=15,background=background).pack(side='left')
    usernameEntry = ttk.Entry(username,state='disabled')
    usernameEntry.pack(side='left')
    username.pack(side='top')
    password = tk.Frame(top, background=background)
    ttk.Label(password, text='Password:',width=15,background=background).pack(side='left')
    passwordEntry = ttk.Entry(password,state='disabled',show="*")
    passwordEntry.bind("<Enter>", lambda e: passwordEntry.configure(show=''))
    passwordEntry.bind("<Leave>", lambda e: passwordEntry.configure(show='*'))
    passwordEntry.pack(side='left')
    password.pack(side='top')
    
    def end():
        if not tkvar.get():
            return False
        db.cur.execute('SELECT salt FROM auth WHERE id="{0}";'.format(ID))
        salt = list(db.cur.fetchone())[0]
        val = registerPlatform(usernameEntry.get(),passwordEntry.get(),tkvar.get(),salt,ID)
        if val:
            top.destroy()
            return
    
    ttk.Button(top, text='Register',command=end,style='Main.TButton').pack(side='right')

def registerUser(db):
    top = tk.Toplevel()
    top['bg'] = background
    top.title('Please Register')
    header = tk.Frame(top, background=background)
    ttk.Label(header,text="Please Register",background=background,font=("Times", 16, "bold")).pack(side='left')
    header.pack(side='top')
    username = tk.Frame(top, background=background)
    ttk.Label(username, text='Username:',width=15,background=background).pack(side='left')
    usernameEntry = ttk.Entry(username)
    usernameEntry.pack(side='left')
    username.pack(side='top')
    password = tk.Frame(top, background=background)
    ttk.Label(password, text='Password:',width=15,background=background).pack(side='left')
    passwordEntry = ttk.Entry(password)
    passwordEntry.pack(side='left')
    password.pack(side='top')
    def end():
        val = register(usernameEntry.get(),passwordEntry.get(),db)
        if val:
            top.destroy()
            return
    ttk.Button(top, text='Register',command=end,style='Main.TButton').pack(side='top')