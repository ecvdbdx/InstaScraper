from bs4 import BeautifulSoup
import selenium.webdriver as webdriver

url = "https://www.instagram.com/explore/tags/plage/"

driver = webdriver.PhantomJS()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

for x in soup.findAll('section'):
    print(x)