from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

chrome_driver = webdriver.Chrome(options=chrome_options)

chrome_driver.get('https://terakoya.sejuku.net')

wait = WebDriverWait(chrome_driver, 30)
header_login_button = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '#root > header > div > div > div.sc-bYMpWt.ecQgNh >'
         'div.sc-jIRcFI.sc-hhOBVt.gREswC.jPXpMh')
    )
)

header_login_button.click()

email_address = input('email: ')
password = getpass('password: ')

email_input = chrome_driver.find_element(By.NAME, 'email')
password_input = chrome_driver.find_element(By.NAME, 'password')

email_input.send_keys(email_address)
password_input.send_keys(password)

form_login_button = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '#root > div.sc-iBYQkv.cvCael > div.sc-kDvujY.eCJBhf > '
         'div.sc-eDWCr.dePrRH > button')
    )
)

form_login_button.click()

timeline_button = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'li[data-e2e="navi-timeline"] a')
    )
)

timeline_button.click()

wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'a[data-e2e="study_reports"]')
    )
)

soup = BeautifulSoup(chrome_driver.page_source, 'html.parser')

latest_post = soup.find('a', {'data-e2e': 'study_reports'})

print('Latest post href: ')
print('https://terakoya.sejuku.net' + latest_post['href'])

chrome_driver.quit()