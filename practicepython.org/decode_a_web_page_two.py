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
import requests
from bs4 import BeautifulSoup

URL = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"


def fetch_page(url: str) -> str:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

def print_article_text(html: str) -> None:
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article")
    if not article:
        raise RuntimeError("Article content not found")

    for p in article.find_all("p"):
        print(p.get_text())

def main() -> None:
    html = fetch_page(URL)
    print_article_text(html)

if __name__ == "__main__":
    main()
