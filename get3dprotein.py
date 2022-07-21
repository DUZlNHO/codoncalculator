import requests
from bs4 import BeautifulSoup
from getpeptide import *

def get3Dprotein(code):
    codigohor = peptide(code)[1]

    url_base = "http://hordb.cpu-bioinfor.org/all%20information.php?id=" + codigohor
    url_base_txt = requests.get(url_base).text
    url_base_soup = BeautifulSoup(url_base_txt, 'html.parser')
    code_pdb = url_base_soup.find_all('a', target="_blank")[0].text

    info = url_base_soup.find_all("ul", class_="sec-infor")
    function = info[2].find_all("li")[0].text
    print(codigohor, code_pdb, function[11:], sep='\n')

    return None, code_pdb, function

if __name__ == '__main__':
    get3Dprotein('CYIQNCPLG')
