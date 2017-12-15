from bs4 import BeautifulSoup
import selenium.webdriver as webdriver

url = "https://www.instagram.com/amelieglutenfit/"

driver = webdriver.PhantomJS()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

for x in soup.findAll('section main '):
    print(x)