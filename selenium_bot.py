from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def account_info():
    with open('account_info.txt', 'r') as f:
        info = f.read().split()
        email = info[0]
        password = info[1]
    return email, password

email, password = account_info()

tweet = "This is a tweet"

PATH = "/home/diptangshudey/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("http://twitter.com/login")

email_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
password_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
login_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div'
profile_xpath = '/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]'
tweet_text = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
tweet_button = '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]'
tweet_1 = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]'
tweet_page = '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section'
time.sleep(2)

driver.find_element_by_xpath(email_xpath).send_keys(email)
time.sleep(0.5)
driver.find_element_by_xpath(password_xpath).send_keys(password)
time.sleep(0.5)
driver.find_element_by_xpath(login_xpath).click()
time.sleep(5)

driver.find_element_by_xpath(tweet_text).send_keys('#hobbist Selenium test 4')
time.sleep(1)
driver.find_element_by_xpath(tweet_button).click()

time.sleep(2)

driver.find_element_by_xpath(profile_xpath).click()

time.sleep(1)
driver.find_element_by_xpath(tweet_1).click()

time.sleep(30)

driver.refresh()

try:
    if 'reply 1' in driver.find_element_by_xpath(tweet_page).text and '@DiptangshuDey' in driver.find_element_by_xpath(tweet_page).text:
        print('It works')
    else:
        print("It didn't work")
finally:
    driver.close()
