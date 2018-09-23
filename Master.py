import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base64 import b64decode
from ast import literal_eval
from os.path import isfile, abspath
from os import name
import zlib
from selenium.webdriver.chrome.options import Options as ChromeOptions      

def loadChromeDriver():
    if isfile('chromedriver.exe'):
        return
    if isfile('chromedriver.dat'):
        file = list(open('chromedriver.dat'))
        data = literal_eval(file[0])
        n = 'chromedriver.exe'
        Icon = data
        icondata = zlib.decompress(b64decode(Icon))
        tempFile = n
        iconfile = open(tempFile,"wb")
        iconfile.write(icondata)
        iconfile.close()
        print('built ChromeDriver')
        return
    if not isfile('chromedriver.dat'):
        print('ERROR:NO DATA FILE')

def createBrowser(headless=False, blockImages=False, hideConsole = False):
    loadChromeDriver()
    chromeOptions = ChromeOptions()
    if blockImages: prefs = {"profile.managed_default_content_settings.images":2}; chromeOptions.add_experimental_option("prefs",prefs)
    if headless: chromeOptions.add_argument("--headless"); chromeOptions.add_argument("--window-size=1920x1080")
    chrome_serv = webdriver.myService('path--to--exe.exe')
    chromeOptions.add_argument("disable-infobars")
    chromeOptions.add_argument("--window-size=1920,1080")
    if name == 'posix':
        browser = webdriver.myWebDriver(chrome_options=chromeOptions)
        return browser
    #chrome_serv.service_args = ["hide_console", ]
    if isfile('chromedriver.exe'):
        drive = abspath("chromedriver.exe")
        if hideConsole:
            browser = webdriver.myWebDriver(executable_path=drive, chrome_options=chromeOptions, service_args=chrome_serv.service_args)
        else:
            browser = webdriver.myWebDriver(executable_path=drive, chrome_options=chromeOptions)
        
    else:
        if hideConsole:
            browser = webdriver.myWebDriver(chrome_options=chromeOptions, service_args=chrome_serv.service_args)
        else: browser = webdriver.myWebDriver(chrome_options=chromeOptions)
    return browser
