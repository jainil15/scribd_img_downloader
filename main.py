import requests
from bs4 import BeautifulSoup
import time

import json
import threading

import shutil

# URL of the webpage you want to scrape
url = input('Enter embeds url: ')


# firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument("--headless")
# firefox_options.add_argument('--no-sandbox')
# firefox_options.add_argument('--disable-dev-shm-usage')
# service = Service(executable_path="./geckodriver.exe")
# driver = webdriver.Firefox(service=service, options=firefox_options)

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")
index = 1
file_location = f"C:/D/{index}.jpg"
x = soup.find_all("img")
file_location = f"C:/D/{index}.jpg"
print(x[0]["src"])
reqimg = requests.get(x[0]["src"], stream=True)
with open(file_location, 'wb') as f:
    f.write(reqimg.content)
index += 1
for i in x[1:]:
    file_location = f"C:/D/{index}.jpg"
    print(i["orig"])
    reqimg = requests.get(i["orig"], stream=True)
    with open(file_location, 'wb') as f:
        f.write(reqimg.content)
    index += 1
soup = BeautifulSoup(response.text, "lxml")
x = soup.find_all("script")
x1 = x[40].text.split("\n")
images = []
index = 4

for i in x1:
    if "contentUrl" in i.strip():
        tempr = requests.get(i[17:].strip()[1:-1])
        temps = BeautifulSoup(tempr.text, "lxml")
        images.append(temps.find("img")['orig'][2:-3])

        reqimg = requests.get(temps.find("img")['orig'][2:-3], stream=True)
        file_location = f"./{index}.jpg"

        with open(file_location, 'wb') as f:
            f.write(reqimg.content)
        index += 1





