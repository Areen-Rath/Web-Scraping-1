import csv
import requests
from bs4 import BeautifulSoup

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(start_url)
soup = BeautifulSoup(page.content, "html.parser")

headers = ["Name", "Distance", "Mass", "Radius"]
star_data = []

def scrap():
    data = soup.find("div", attrs = { "class", "mw-body-content mw-content-ltr" })
    
    for i in data.find_all("tr"):
        temp_list = []
        try:
            td = i.find_all("td")
            temp_list.append(td[1].text.split("\n")[0])
            temp_list.append(td[3].text.split("\n")[0])
            temp_list.append(td[5].text.split("\n")[0])
            temp_list.append(td[6].text.split("\n")[0])
        except:
            continue
        star_data.append(temp_list)

scrap()

print(star_data)

with open("scraper.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    for star in star_data:
        try:
            csv_writer.writerow(star)
        except:
            continue