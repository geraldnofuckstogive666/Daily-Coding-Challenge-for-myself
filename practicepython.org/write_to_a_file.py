#https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
import requests
from bs4 import BeautifulSoup


def data_scraper() -> list[str]:
    url = "https://www.nytimes.com/"
    response = requests.get(url)
    if response.status_code == 200:
        url_doc = response.text
    else:
        print(response.status_code)
        return
    
    soup = BeautifulSoup(url_doc, 'html.parser')
    classes = ["indicate-hover css-1ixq7yl",   "indicate-hover css-91bpc3",  
            "indicate-hover css-1a5fuvt", "indicate-hover css-aew41b",  "indicate-hover css-uzitgk"]

    articles = []
    
    for n in classes:
        titles = soup.find_all('p', class_=n)
        for title in titles:
            article = title.get_text(" ",strip=True)
            articles.append(article)

    return articles



def write_to_file(filename: str,data: list[str]) -> None:
    if not data:
        print("No data to write.")
        return
    
    with open(filename +'.txt', 'w') as open_file:
        open_file.write('\n'.join(data))


def main():
    user_input = input("Output file name: ").strip()
    if not user_input:
        print("Invalid filename.")
        return
    
    data = data_scraper()
    write_to_file(user_input,data)


if __name__ == "__main__":
    main()
