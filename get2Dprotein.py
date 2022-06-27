import requests
from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient

def getIMGlink(name):
    try:
        url = "https://pubchem.ncbi.nlm.nih.gov/#query=" + name

        client = ScrapingAntClient(token='e7eb3bc105974718bcb69e57558c757b')

        page_content = client.general_request(url).content

        soup = BeautifulSoup(page_content, 'html.parser')
        id = soup.find("a", tabindex="-1")
        id = id['href']
        id = id[::-1]
        id = id[:id.find('/')]
        id = id[::-1]

        imglink = 'https://pubchem.ncbi.nlm.nih.gov/image/imagefly.cgi?cid=' + id + '&width=1000&height=1000'
        return imglink
    except:
        return "https://bitsofco.de/content/images/2018/12/Screenshot-2018-12-16-at-21.06.29.png"

if __name__ == '__main__':
    print(getIMGlink('oxytocin'))