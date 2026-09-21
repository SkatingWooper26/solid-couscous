import requests
from bs4 import BeautifulSoup

def web_scrape() -> None:
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    heading = soup.select_one("h1").text
    quote = soup.select_one("span", class_ = "text").text
    author = soup.select_one("small", class_ = "author").text
    
    print(heading)
    print(quote)
    print(author)
    
if __name__ == "__main__":
    web_scrape()