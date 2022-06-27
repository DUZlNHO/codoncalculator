from flask import *
from genstructure import *
from getpeptide import *
from translate import *
from get3dprotein import *
from get2Dprotein import *
import os

app = Flask(__name__)

acidos = []
codes = []
pepditios = []
peptidios_traduzido = []
imglink = []

@app.route("/" , methods=["GET", "POST"])
def index():
    global acidos
    global peptidio
    acidos = []
    peptidio = ''
    return render_template('index.html')

@app.route("/calc", methods=["POST", "GET"])
def calc():
    global acidos, codes, pepditios, peptidios_traduzido, imglink
    abs = os.path.dirname(__file__) + '/'
    dr = request.form['dr']
    try:
        ct = request.form['ct']
    except:
        ct = 5
    seq = request.form['seq']

    def lower(x):
        x = x.lower().replace(' ', '')
        return x

    if dr == 'dna':
        if ct == '5':
            cadeia = ''
            dna = seq
            dna = lower(dna)
            for acido in dna:
                if acido == 't':
                    cadeia += 'u'
                else:
                    cadeia += acido
        else:
            cadeia = ''
            dna = seq
            dna = lower(dna)
            for acido in dna:
                if acido == 'a':
                    cadeia += 'u'
                elif acido == 'c':
                    cadeia += 'g'
                elif acido == 'g':
                    cadeia += 'c'
                elif acido == 't':
                    cadeia += 'a'
    else:
        cadeia = seq
        cadeia = lower(cadeia)

    codons = [cadeia[p:p + 3] for p in range(0, len(cadeia), 3)]

    with open(abs + 'db/proteinas.txt', 'r') as proteinas:
        proteinaslinhas = proteinas.readlines()

    for codon in codons:
        for prot in proteinaslinhas:
            if codon == prot[0:3]:
                acidos.append(prot[4:].strip())

    with open(abs + 'db/fastaproteins.txt', 'r') as proteinas:
        proteinaslinhas = proteinas.readlines()
    code = ''

    for codon in codons:
        for prot in proteinaslinhas:
            if codon == prot[0:3]:
                code += prot[4:].strip()

    imagem = genstructure(cadeia)

    codes = []
    temp = ''
    counting = True

    for each in code:
        if each == '*':
            counting = False
            codes.append(temp)
            temp = ''
        elif each == 'M':
            if counting:
                temp += each
            else:
                counting = True
                temp = ''
        else:
            if counting:
                temp += each
            else:
                continue
    if counting:
        codes.append(temp)

    results_html = '<!DOCTYPE html><html><head><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><title>Aminoácidos</title><meta name="description" content=""><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><link rel="stylesheet" href="{{ url_for(\'static\', filename=\'css/results3.css\') }}"><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous"><style>* {margin: 0;padding: 0;}body {background-color: lightgreen;}.item1 {background-color: lightblue;width: 80%;height: 2000px;position: relative;left: 50%;transform: translateX(-50%);}.item1>iframe {border: 0;border-radius: 20px;width: 100%;height: 100%;}</style></head><body><!--[if lt IE 7]><p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="#">upgrade your browser</a> to improve your experience.</p><![endif]--><nav id="bar"><ul><li id="back">    <h1 id="back"><a href="http://127.0.0.1:5000">Voltar</a></h1></li><li>    <h1><a href="http://127.0.0.1:5000/results">DNA/RNA</a></h1></li><li>    <h1><a href="http://127.0.0.1:5000/results2">Aminoácidos</a></h1></li><li>    <h1><a href="http://127.0.0.1:5000/results3">Peptídio</a></h1></li></ul></nav><div id="carouselExampleControls" class="carousel slide" data-interval="false"><div class="carousel-inner">'

    with open(abs + 'templates/results3.html', 'w') as res:
        res.write(results_html)

    print(codes)

    if request.form.get('peptidio'):
        peptidios = []
        for index, sequence in enumerate(codes):
            peptidios.append(peptide(sequence)[0])
            print(peptidios)
            head = get3Dprotein(sequence)[0]
            code_pdb = get3Dprotein(sequence)[1]
            with open(abs + 'static/result' + str(index) + '.html', 'w') as template:  # iframes
                template.write('<!DOCTYPE html><html>' + head + '<style>*{margin:0;padding:0;}img{position:absolute;left:50%;transform:translateX(-50%);width:90%;}</style><body><protvista-uniprot-structure accession="' + code_pdb + '"></protvista-uniprot-structure><img src="' + getIMGlink(peptidios[index]) + '"></body></html>')
            with open(abs + 'templates/results3.html', 'a') as res:  # html results3
                if index == 0:
                    res.write('<div class="carousel-item active"><div class="item1"><iframe src="{{ url_for(\'static\', filename=\'result' + str(index) + '.html\') }}" frameborder="0" allowfullscreen></iframe></div></div>')
                else:
                    res.write('<div class="carousel-item"><div class="item1"><iframe src="{{ url_for(\'static\', filename=\'result' + str(index) + '.html\') }}" frameborder="0" allowfullscreen></iframe></div></div>')
        results1_html = '</div><a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev"><span class="carousel-control-prev-icon" aria-hidden="true"></span><span class="sr-only">Anterior</span></a><a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next"><span class="carousel-control-next-icon" aria-hidden="true"></span><span class="sr-only">Próximo</span></a></div><script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script><script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script><script src=""></script></html>'
        with open(abs + 'templates/results3.html', 'a') as res:
            res.write(results1_html)
        print(codes)
        print(peptidios)
        print(imagem)
        return render_template('results.html')
    else:
        print(code)
        print(imagem)
        return render_template('results.html')

@app.route("/results", methods=["POST", "GET"])
def results():
    return render_template('results.html')

@app.route("/results2", methods=["POST", "GET"])
def results2():
    return render_template('results2.html', acidos=acidos)

@app.route("/results3", methods=["POST", "GET"])
def results3():
    return render_template('results3.html')

if __name__ == "__main__":
    app.run()