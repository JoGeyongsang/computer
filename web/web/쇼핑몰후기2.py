from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='D:\web\chromedriver.exe')
options=webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
browser=webdriver.Chrome(service=service, options=options)

url='http://itempage3.auction.co.kr/DetailView.aspx?itemno=B877816140'
browser.get(url)

review_button = browser.find_element(By.CSS_SELECTOR, 'li#tap_moving_2 a')
review_button.click()

elements=browser.find_elements(By.CSS_SELECTOR, 'ul.list__review p.text')
for element in elements:
    print(element.text)