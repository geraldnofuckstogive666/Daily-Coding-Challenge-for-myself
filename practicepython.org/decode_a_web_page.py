#https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html


"""
Docstring for practicepython.org.decode_a_web_page

Note: this is a 4-chili exercise, not because it introduces a concept 
(although it introduces a new library), but because this exercise is more
like a project. Feel free to skip this and come back when you’re more ready!

Use the BeautifulSoup and requests Python packages to print out a list of
all the article titles on the New York Times homepage.
"""
import requests
from bs4 import BeautifulSoup


url = "https://www.nytimes.com/"
response = requests.get(url)


if response.status_code == 200:
    url_doc = response.text
else:
    print(response.status_code)

soup = BeautifulSoup(url_doc, 'html.parser')
classes = ["indicate-hover css-1ixq7yl",   "indicate-hover css-91bpc3",  
        "indicate-hover css-1a5fuvt", "indicate-hover css-aew41b",  "indicate-hover css-uzitgk"]

for n in classes:
    titles = soup.find_all('p', class_=n)

    for title in titles:
        print(title.get_text(strip=True))
