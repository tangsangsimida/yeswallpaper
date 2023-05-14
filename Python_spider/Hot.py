import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    img_href = []
    url = "https://wallhaven.cc/hot"
    parma = {
        "page":1
    }
    resp = requests.get(url=url,params=parma)
    html = BeautifulSoup(resp.text,"html.parser")
    imgs = html.find_all("a", class_ = "preview")
    for img in imgs:
        img_href.append(img.get("href"))
    print(img_href)