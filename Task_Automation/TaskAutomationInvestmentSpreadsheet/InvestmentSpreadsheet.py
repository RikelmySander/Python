from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

#DISCLAIMER!!!
#Do not run the program if Chrome is open, there is a chance of an error!

service = Service(ChromeDriverManager().install())

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:/Users/Rikel/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("profile-directory=Default")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")

browser = webdriver.Chrome(service=service,options=chrome_options)
browser.maximize_window()

browser.get("https://docs.google.com/spreadsheets/d/1si_MSSYsT39iIHF2FbGzCPaPanOmL4iI4mwPsxr9hNA/edit?gid=0#gid=0")
#opening financial data in the new guide
browser.get("https://www.binance.com")
list_NameCripto = browser.find_elements(classes = )
#get values of investments
#add in a list
#add values a list
list_ValuesCripto = []
#scroll through the list and distribute the information vertically in the spreadsheet

#browser.get("https://www.binance.com")

time.sleep(10)

