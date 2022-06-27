import requests
from bs4 import BeautifulSoup
from getpeptide import *

def get3Dprotein(code):
    codigohor = peptide(code)[1]

    url_base = "http://hordb.cpu-bioinfor.org/all%20information.php?id=" + codigohor
    url_base_txt = requests.get(url_base).text
    url_base_soup = BeautifulSoup(url_base_txt, 'html.parser')
    code_pdb = url_base_soup.find_all('a', target="_blank")[0].text

    url = 'https://www.uniprot.org/uniprot/' + code_pdb
    html_txt = requests.get(url).text
    soup = BeautifulSoup(html_txt, 'html.parser')
    head = soup.find('head')
    head = str(head)
    print(codigohor, code_pdb)

    return head, code_pdb

if __name__ == '__main__':
    get3Dprotein('CYIQNCPLG')
