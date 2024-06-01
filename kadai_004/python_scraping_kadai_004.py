from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

chrome_driver = webdriver.Chrome(options=chrome_options)

chrome_driver.get('https://www.nikkei.com/markets/worldidx/chart/nk225/?type=6month')

wait = WebDriverWait(chrome_driver, 30)
chart = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, 'highcharts-series-group')
    )
)

chart_width = chart.size['width']
chart_height = chart.size['height']

actions = ActionChains(chrome_driver)

print(chart.location['x'])

start_x = chart.location['x'] + chart_width // 2
start_y = chart.location['y'] + chart_height // 2

