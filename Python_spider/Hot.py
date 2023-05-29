import requests
from bs4 import BeautifulSoup
from concurrent.futures  import ThreadPoolExecutor
import os

'''
 get  img list and into the url , get the img url
'''
def get_img(url):
    resp = requests.get(url=url)
    if resp.status_code==200:
        soup = BeautifulSoup(resp.text,"html.parser")
        img_url = soup.find("img",id = "wallpaper")
        img_url_end = (img_url["src"])
        print(img_url_end)
        resp = requests.get(img_url_end).content
        #             获取当前文件夹路径,           文件名->网站图片本身的id,不会造成重名现象
        with open(fr"{os.getcwd()}/img_download/{url[-6:]}.jpg","wb") as f:
            f.write(resp)
    else:
        return ;
    # print(f"/home/tangsang/Desktop/yeswallpaper/Python_spider/{url[-6:]}.{type}]")


if __name__ == "__main__":
    img_each_url = []
    img_href = []
    url = "https://wallhaven.cc/hot"
    # 一共有28页img
    for page in range(1,28):
        parma = {
            "page":f"{page}"
        }
        resp = requests.get(url=url,params=parma)
        html = BeautifulSoup(resp.text,"html.parser")
        imgs = html.find_all("a", class_ = "preview")
        for j in imgs:
            img_each_url.append(j["href"])
        # 拿到图片的url

        # 实现多线程下载列表中的图片----> img_href
        with ThreadPoolExecutor(max_workers=100) as t:
            t.map(get_img,img_each_url)
        print(f"end~~~~~~~~~page---->{page}")
        print(f"end~~~~~~~~~page---->{page}")
        print(f"end~~~~~~~~~page---->{page}")
        print(f"end~~~~~~~~~page---->{page}")