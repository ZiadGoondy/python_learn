import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

# 1.Use requests to fetch Url:
page = requests.get("https://wuzzuf.net/search/jobs/?q=data+science&a=hpb")

# 2.Save Page Content:
src = page.content

# 3.Create beautifulsoup object to parse content:
soup = BeautifulSoup(src, "lxml")

# 4.Find elements Containing info: [JopTitles, JopSkills, CompanyNames, LocationNames]
JopTitles = soup.find_all("h2", {"class": "css-m604qf"})
CompanyNames = soup.find_all("a", {"class": "css-17s97q8"})
LocationNames = soup.find_all("span", {"class": "css-5wys0k"})
JopSkills = soup.find_all("div", {"class": "css-y4udm8"})


# 5.Create lists to store info
JopTitle = []
CompanyName = []
LocationName = []
Skills = []
Links = []
JopDescription = []

# 6.Extract useful info from lists:
for i in range(len(JopTitles)):
    JopTitle.append(JopTitles[i].text)
    CompanyName.append(CompanyNames[i].text)
    LocationName.append(LocationNames[i].text)
    Skills.append(JopSkills[i].text)
    Links.append(JopTitles[i].find("a").attrs['href'])

Basic_url = "https://wuzzuf.net"
Links = [Basic_url + Link for Link in Links]


for Link in Links:
    page1 = requests.get(Link)
    src = page1.content
    soup = BeautifulSoup(src, "lxml")
    JopDescriptions = soup.find("div", {"class": "css-1uobp1k"})
    JopDescription.append(JopDescriptions.text)

print(JopDescription)
# 7.Create CSV file and fill it with Data
file_list = [JopTitle, CompanyName, LocationName, Skills, Links, JopDescription]
exported = zip_longest(*file_list)
with open("jop_file.csv", "w") as my_file:
    wr = csv.writer(my_file)
    wr.writerow(["Jop Title", "Company Name", "Location", "Skills", "Links", "JopDescription"])
    wr.writerows(exported)

# 8.Get Data From InnerPages


