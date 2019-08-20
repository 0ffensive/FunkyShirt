import selenium
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-data-dir=C:\\Users\\ofcra\\AppData\\Local\\Chromium\\User Data\\Default")
options.add_argument("profile-directory=Название_папки_с_нужным_профилем")

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://secure2.e-konsulat.gov.pl")