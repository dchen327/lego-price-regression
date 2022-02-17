import requests
from bs4 import BeautifulSoup

URL = 'https://brickset.com/browse/sets/byyear/'
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

month_groups = soup.find_all('dl', class_='monthlist')

for month_group in month_groups:
    print(month_group)
    break

    # sep by indiv (/sets/) and theme (/sets/theme/)
    