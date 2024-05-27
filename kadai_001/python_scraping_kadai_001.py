import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.yahoo.co.jp/articles/e9fa1c74d121e5c63749c71bd750593aa0352b00')

soup = BeautifulSoup(response.text, 'html.parser')
article_body_element = soup.select_one('#uamods div.article_body p.yjSlinkDirectlink')
print(article_body_element.text)

