from selenium import webdriver
import time as T
import tkinter as tk
from threading import Thread
import sqlite3

def launchBrowser(url):
    #flags
    b = webdriver.Chrome()
    return b

def loginUser():
    #return session
    pass

def registerUser():
    #return None
    pass

def loadFirst(session):
    print(1)
    pass

def loadFirstHelper(session):
    pass

def loadSecond():
    print(2)
    pass

def loadThird():
    print(3)
    pass

def load():
    root = tk.Tk()
    root.geometry('500x500')
    mainFrame = tk.Frame(root)
    header = tk.Label(mainFrame, text="Welcome to the Library?")
    header.pack()
    mainFrame.pack(fill='x')
    bodyFrame = tk.Frame(root)
    button1 = tk.Button(bodyFrame,text="hi",command=loadFirst)
    button2 = tk.Button(bodyFrame,command=loadSecond)
    button3 = tk.Button(bodyFrame,command=loadThird)
    button1.pack();button2.pack();button3.pack()

    bodyFrame.pack(fill='both')
    root.mainloop()

load()
#b = webdriver.Chrome()



T.sleep(10)
#b.quit()
