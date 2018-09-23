import time as T
import sqlite3
import hashlib
from random import choice
from string import ascii_letters
import os
from Crypto.Cipher import AES
#from browserFunctions import *

def register(un,pw,db):
    db.cur.execute('SELECT * FROM auth WHERE username="{0}"'.format(un))
    if db.cur.fetchone():
        print('fail:userexists')
        return False
    userID = ''
    while userID == '':
        userID=''.join(choice(ascii_letters) for i in range(16))
        db.cur.execute('SELECT * FROM auth WHERE id="{0}"'.format(userID))
        if db.cur.fetchone():
            userID = ''
    allC = str(ascii_letters)
    allC += '0123456789'
    salt = ''.join(choice(allC) for i in range(16))
    m = hashlib.sha256()
    m.update(bytes(pw, 'utf-8'))
    m.update(bytes(salt, 'utf-8'))
    salted = m.hexdigest()
    db.cur.execute('INSERT INTO auth VALUES ("{0}","{1}","{2}","{3}")'.format(un,salt,salted,userID))
    db.conn.commit()
    print('user created')
    return True

def registerPlatform(username, password, platform,salt,ID):
    conn = sqlite3.connect(r'data.db')
    cur = conn.cursor()
    while len(password)%16 != 0:
        password += ' '
    obj = AES.new(bytes(salt,'utf-8'), AES.MODE_ECB)
    ciph = obj.encrypt(bytes(password,'utf-8'))
    ciph = ciph.hex()

    cur.execute('INSERT INTO platformLogins VALUES ("{0}","{1}","{2}","{3}")'.format(username, ciph, platform,ID))
    conn.commit()
    conn.close()
    print('user created')
    return True
    
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