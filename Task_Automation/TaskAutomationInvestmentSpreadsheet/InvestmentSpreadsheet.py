from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

service = Service(ChromeDriverManager().install())

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:/Users/Rikel/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("profile-directory=Default")
chrome_options.add_argument("--remote-debugging-port=9222")  # Habilita o DevTools para evitar erros
chrome_options.add_argument("--no-sandbox")  # Necessário em alguns ambientes
chrome_options.add_argument("--disable-dev-shm-usage")  # Evita problemas em ambientes limitados de memória
chrome_options.add_argument("--disable-extensions")  # Desabilita extensões (pode interferir)

browser = webdriver.Chrome(service=service,options=chrome_options)
browser.maximize_window()

browser.get("https://docs.google.com/spreadsheets")
browser.get("https://www.binance.com")

time.sleep(10)

