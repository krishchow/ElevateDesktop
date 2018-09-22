from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from Crypto.Cipher import AES
from threading import Thread
import sqlite3


def launchBrowser(url):
    chrome_options = Options()
    chrome_options.add_argument("disable-infobars")
    b = webdriver.Chrome(chrome_options=chrome_options)
    b.get(url)
    return b

def loadFirst(session):
    print(1)
    t = Thread(target=loadFirstHelper, args=(session,"Presto"))
    t.start()
    

def loadFirstHelper(session,p):
    conn = sqlite3.connect(r'data.db')
    cur = conn.cursor()
    cur.execute('SELECT username,password FROM platformLogins WHERE (id="{0}" AND platformID="{1}");'.format(session,p))
    val = cur.fetchone()
    if not val:
        return False
    val = list(val)
    cur.execute('SELECT salt FROM auth WHERE id="{0}";'.format(session))
    salt = list(cur.fetchone())
    if not salt:
        return False
    salt = salt[0]
    PASS = bytes.fromhex(val[1])
    obj = AES.new(salt)
    PASS = obj.decrypt(PASS)
    PASS = str(PASS).replace('b','')
    PASS = PASS.replace("'",'')
    print(type(PASS))
    print(PASS)
    browser = launchBrowser("https://www.prestocard.ca/en")
    browser.find_element_by_class_name('modalLogin').find_element_by_xpath('.//a').click()
    username  = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'SignIn_Username')))
    browser.find_element_by_id('SignIn_Username').click()
    username = browser.find_element_by_id('SignIn_Username')
    username.send_keys(val[0])
    browser.find_element_by_id('SignIn_Password').click()
    password = browser.find_element_by_id('SignIn_Password')
    print(PASS)
    password.send_keys(PASS)
    browser.find_element_by_id('btnsubmit').click()


def loadSecond(session):
    print(2)
    pass

def loadThird(session):
    print(3)
    pass
