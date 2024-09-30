import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://quackr.io/sitemap.xml")
time.sleep(10)
element = driver.find_element("xpath", "//*")
html = element.get_attribute("outerHTML")
# print(html)
soup = BeautifulSoup(html, "html.parser")
folders = soup.find_all(name='div', attrs={'class': 'folder'})
data_list = []
for folder in folders:
    url_data = {}

    # Извлечение элементов loc, lastmod, changefreq и priority
    loc = folder.find('span', string=lambda text: text and 'loc' in text)
    if loc:
        url_data['loc'] = loc.find_next_sibling('span').text

    lastmod = folder.find('span', string=lambda text: text and 'lastmod' in text)
    if lastmod:
        url_data['lastmod'] = lastmod.find_next_sibling('span').text

    changefreq = folder.find('span', string=lambda text: text and 'changefreq' in text)
    if changefreq:
        url_data['changefreq'] = changefreq.find_next_sibling('span').text

    priority = folder.find('span', string=lambda text: text and 'priority' in text)
    if priority:
        url_data['priority'] = priority.find_next_sibling('span').text

    if url_data:
        data_list.append(url_data)

# Вывод результатов
for data in data_list:
    print(data)
