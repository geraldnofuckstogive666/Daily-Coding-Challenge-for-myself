#https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
"""
Docstring for practicepython.org.decode_a_web_page_two


Using the requests and BeautifulSoup Python libraries, print to the screen 
the full text of the article on this website: 
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to 
print out the text to the screen so that you can read the full article 
without having to click any buttons.

"""

# Importing Modules
from bs4 import BeautifulSoup
import requests

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
response = requests.get(url)

if response.status_code == 200:
    data = response.text
else:
    print(f"Response from the server: {response.status_code}")

soup = BeautifulSoup(data, 'html.parser')

for line in soup.find_all("p"):
    print(line.get_text(strip=True))






