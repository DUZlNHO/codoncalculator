from flask import *
from genstructure import *
from getpeptide import *
from translate import *
from get3dprotein import *
from get2Dprotein import *
from genacids import *
import os

app = Flask(__name__)

acidos = []
codes = []
pepditios = []
peptidios_traduzido = []
imglink = []
functions = []

@app.route("/" , methods=["GET", "POST"])
def index():
    global acidos
    global peptidio
    acidos = []
    peptidio = ''
    return render_template('index.html')

@app.route("/calc", methods=["POST", "GET"])
def calc():
    global acidos, codes, pepditios, peptidios_traduzido, imglink, functions
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
    aminoacids = genacids(acidos)

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

    results_html = '<!DOCTYPE html><html lang="pt-br"><head>    <!-- Meta tags Obrigatórias -->    <meta charset="utf-8">    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">    <!-- Bootstrap CSS -->    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">    <link rel="stylesheet" href="{{ url_for(\'static\', filename=\'css/results3.css\') }}">    <title>Aminoácidos</title></head><body>    <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #00000066;">        <a class="navbar-brand" href="http://127.0.0.1:5000">Calculadora de Códons</a>        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Alterna navegação">          <span class="navbar-toggler-icon"></span>        </button>        <div class="collapse navbar-collapse" id="navbarNav">            <ul class="navbar-nav">                <li class="nav-item">                    <a class="nav-link" href="http://127.0.0.1:5000/results">DNA/RNA</a>                </li>                <li class="nav-item">                    <a class="nav-link" href="results2">Aminoácidos</a>                </li>                <li class="nav-item active">                    <a class="nav-link" href="#">Peptídios<span class="sr-only">(Página atual)</span></a>                </li>            </ul>        </div>    </nav>    <div id="carouselExampleControls" class="carousel slide" data-interval="false">        <div class="carousel-inner">'

    with open(abs + 'templates/results3.html', 'w') as res:
        res.write(results_html)

    print(codes)

    if request.form.get('peptidio'):
        peptidios = []
        for index, sequence in enumerate(codes):
            peptidename = translation(peptide(sequence)[0])
            peptidios.append(peptidename)
            print(peptidios)
            code_pdb = get3Dprotein(sequence)[1]
            functions = translation(get3Dprotein(sequence)[2])
            print('a1')
            with open(abs + 'static/result' + str(index) + '.html', 'w') as template:  # iframes
                template.write('<!DOCTYPE html><html><head><script type="text/javascript" src="js/molart.js"></script><link rel="stylesheet" href="css/iframes.css"></head><body><h1 id="titulo">' + peptidename + '</h1><br><p id="function">' + functions + '</p><br><h1 id="title3d">Projeção em 3D</h1><div id="pluginContainer"></div><br><br><br><br><br><hr><br><h1 id="title2d">Projeção em 2D</h1><img id="peptide" src="' + getIMGlink(peptidios[index]) + '"><script>window.onload = function() { const molart = new MolArt({ uniprotId: "' + code_pdb + '", containerId: "pluginContainer" }); };</script></body></html>')
            print('a2')
            with open(abs + 'templates/results3.html', 'a') as res:  # html results3
                if index == 0:
                    res.write('<div class="carousel-item active"><div class="item1"><iframe src="{{ url_for(\'static\', filename=\'result' + str(index) + '.html\') }}" frameborder="0" loading=lazy></iframe></div></div>')
                else:
                    res.write('<div class="carousel-item"><div class="item1"><iframe src="{{ url_for(\'static\', filename=\'result' + str(index) + '.html\') }}" frameborder="0" loading="lazy"></iframe></div></div>')
        results1_html = '</div><a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev" style="width: 100px;"><span class="carousel-control-prev-icon" aria-hidden="true"></span><span class="sr-only">Anterior</span></a><a class="carousel-control-next"            href="#carouselExampleControls" role="button" data-slide="next" style="width: 100px;"><span class="carousel-control-next-icon" aria-hidden="true"></span><span class="sr-only">Próximo</span></a></div>    <div class="foot">By Eduardo Henrique da Silva, IFSULDEMINAS - Campus Inconfidentes, 2022</div>    <!-- JavaScript (Opcional) -->    <script src=""></script>    <!-- jQuery primeiro, depois Popper.js, depois Bootstrap JS -->    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script></body></html>'
        print('a3')
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