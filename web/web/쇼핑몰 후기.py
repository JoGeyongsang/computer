# 두번째 실습은 쇼핑몰 후기 가져오기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# 블루투스 오류 방지용
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# webdriver
# 크롬을 기준으로 현재 사용하고 있는 버전에 맞춰서 webdriver를 다운로드
service = Service(executable_path="c:\\IJH\\workspace\\chromedriver.exe")
browser = webdriver.Chrome(service=service, options=options)

url = 'https://www.naver.com'
browser.get( url )

element = browser.find_element(By.CSS_SELECTOR, 'input#query')
print('TEST')
print( element )