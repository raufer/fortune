from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'zeropoint.logos@gmail.com'
passwordStr = '0Silver9!'

url = 'https://accounts.google.com/signin/oauth/oauthchooseaccount?response_type=code&redirect_uri=https%3A%2F%2Fsso.accounts.dowjones.com%2Flogin%2Fcallback&scope=email%20profile&state=VrdPo6YovN5sJJmj_NsjmjbQ9n3Um3pi&client_id=61387583289.apps.googleusercontent.com&savelogin=on&o2v=1&as=JK9-t4vYsXUzvvz2Pc8e2g&flowName=GeneralOAuthFlow'

browser = webdriver.PhantomJS()
browser.get(url)

import pdb
a = browser.find_element_by_xpath("//body")
print(a.get_attribute('innerHTML'))
raise ValueError

username = browser.find_element_by_id('Email')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('next')
nextButton.click()

# wait for transition then continue to fill items
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'Passwd')))
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('signIn')
signInButton.click()

