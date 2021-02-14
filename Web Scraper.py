import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome(executable_path='/Users/Krum/Downloads/chromedriver')
driver.get('https://www.reed.co.uk/jobs/juniour-pytnoh-developer-jobs-in-london/')
results = []
results2 = []
results3 = []
results4 = []
content = driver.page_source
soup = BeautifulSoup(content)


def check_page():
    for a in soup.findAll(attrs='posted-by'):
        name = a.find('a')
        if name not in results:
            results.append(name.text)

    for b in soup.findAll(attrs='location'):
        name = b.find('span')
        if name not in results:
            results2.append(name.text)

    for c in soup.findAll(attrs='col-sm-12 col-md-9 col-lg-9 details'):
        name = c.find('a')
        if name not in results:
            results3.append(name.text)

    for d in soup.findAll(attrs='col-sm-12 col-md-9 col-lg-9 details'):
        name = d.find('li')
        if name not in results:
            results4.append(name.text)


check_page()
element = driver.find_element_by_id("nextPage")
while True:
    element.click()
    time.sleep(5)
    results = []
    results2 = []
    results3 = []
    results4 = []
    check_page()
    try:
        element = driver.find_element_by_id("nextPage")
    except NoSuchElementException:
        break

df = pd.DataFrame({'Posted By ': results, 'Location ': results2, 'Position ': results3, 'Salary ': results4})
df.to_csv('name.csv', index=False, encoding='utf-8')
driver.quit()
