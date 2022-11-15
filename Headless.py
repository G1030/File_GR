from click import option
from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.edge.options import Options

options = Options()
options.headless = True
web_driver = webdriver.Chrome(options=options)
web_driver.get('https://www.guvi.in')
data = [web_driver.title, web_driver.current_url]

print(data)

web_driver.quit()
