import pandas as pd
def peptide(code):
    site = "http://hordb.cpu-bioinfor.org/mysqli.php?searvalue="
    url = site + code
    response = pd.read_html(url)

    table = response[0]
    for k in range(len(table)):
        if table.iloc[k,3] == 'Human':
            return table.iloc[k,1], table.iloc[k,0]
    return table.iloc[0,1], table.iloc[0,0]  # nome, codigohor

if __name__ == "__main__":
    print(peptide("CYIQNCPLG"))

