import Master
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from Crypto.Cipher import AES
from threading import Thread
import sqlite3


def getUnencrypted(session,p):
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
    obj = AES.new(bytes(salt,'utf-8'),AES.MODE_ECB)
    PASS = obj.decrypt(PASS)
    PASS = str(PASS).replace('b','')
    PASS = PASS.replace("'",'').strip()
    return [val[0], PASS]

def launchBrowser(url):
    b = Master.createBrowser()
    b.get(url)
    return b

def loadFirst(session,reg=False):
    print(1)
    if reg:
        t = Thread(target=loadFirstRegistration, args=(session))
        t.start()
    else:
        t = Thread(target=loadFirstHelper, args=(session,"Presto"))
        t.start()

def loadFirstRegistration():
    browser = launchBrowser("https://www.prestocard.ca/en")
    browser.find_element_by_class_name('modalLogin').find_element_by_xpath('.//a').click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'SignIn_Username')))
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element_by_id('createaccount-btn').click()



def loadFirstHelper(session,p):
    login = getUnencrypted(session,p)
    if not login:
        browser = launchBrowser("https://www.prestocard.ca/en")
        return
    browser = launchBrowser("https://www.prestocard.ca/en")
    browser.find_element_by_class_name('modalLogin').find_element_by_xpath('.//a').click()
    username  = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'SignIn_Username')))
    browser.find_element_by_id('SignIn_Username').click()
    username = browser.find_element_by_id('SignIn_Username')
    username.send_keys(login[0])
    browser.find_element_by_id('SignIn_Password').click()
    password = browser.find_element_by_id('SignIn_Password')
    password.send_keys(login[1])
    browser.find_element_by_id('btnsubmit').click()


def loadSecond(session):
    print(2)
    t = Thread(target=loadSecondtHelper, args=(session,"Library"))
    t.start()

def loadSecondtHelper(session,p):
    login = getUnencrypted(session,p)
    if not login:
        browser = launchBrowser("https://www.torontopubliclibrary.ca/signin")
        return
    
    browser = launchBrowser("https://www.torontopubliclibrary.ca/signin")
    username  = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'userId')))
    browser.find_element_by_id('userId').click()
    username = browser.find_element_by_id('userId')
    username.send_keys(login[0])
    browser.find_element_by_id('password').click()
    password = browser.find_element_by_id('password')
    password.send_keys(login[1])
    browser.find_element_by_xpath('//*[@value="Sign In"]').click()


def loadThird(session):
    print(3)
    t = Thread(target=loadThirdHelper, args=(session,"Volunteer Toronto"))
    t.start()


def loadThirdHelper(session,p):
    login = getUnencrypted(session,p)
    if not login:
        browser = launchBrowser("https://www.volunteertoronto.ca/login.aspx")
        return
    
    browser = launchBrowser("https://www.volunteertoronto.ca/login.aspx")
    username  = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'u')))
    browser.find_element_by_id('u').click()
    username = browser.find_element_by_id('u')
    username.send_keys(login[0])
    browser.find_element_by_id('p').click()
    password = browser.find_element_by_id('p')
    password.send_keys(login[1])
    browser.find_element_by_name('btn_submitLogin').click()