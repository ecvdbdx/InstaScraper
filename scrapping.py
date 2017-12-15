from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import urllib.request
import base64

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

url = "https://www.instagram.com/amelieglutenfit/"
folder = "/Users/ecv/Documents/Guilhem/InstaScraper/images/"

#Clarifai API
app = ClarifaiApp(api_key='c0f37a56c5a64c0895f0b76395e89483')
# get the general model
model = app.models.get("general-v1.3")

driver = webdriver.PhantomJS()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser');

#Crawl Instragram images and save on the computer
for x in soup.findAll('section'):
    for m in x.findAll('main'):
        for a in m.findAll('article'):
            for i in m.findAll('img'):
                link = i.get("src").replace("s150x150", "s640x640/sh0.08")
                filename = link.split('/')[-1]
                urllib.request.urlretrieve(link, folder+filename)

                url = folder + filename
                image = ClImage(file_obj=open(url, 'rb'))
                response = model.predict([image])

                print(response['outputs'][0]['data']['concepts'])

#Convert image to Base64
# with open(folder+"22430356_1623510141041943_6432977156678090752_n.jpg", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())
#     print(encoded_string)