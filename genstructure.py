import os
from structurepaths import *
from PIL import Image

def genstructure(seq):
    abs = os.path.dirname(__file__)

    seqdna = ''
    seqrna = seq

    for i in seq:
        if i == 'u':
            seqdna += 't'
        else:
            seqdna += i

    canvas = Image.new('RGB', (2500, len(seq)*460 + 80 + 600), '#cccccc')
    canvas.paste(Image.open(abs + '/dnastructure/header.png'), (0, 0))
    dnacanvas = Image.new('RGB', (1250, len(seq)*460 + 80), '#cccccc')
    rnacanvas = Image.new('RGB', (1250, len(seq)*460 + 80), '#cccccc')

    for index, letter in enumerate(seqdna):
        if index == 0:
            dnacanvas.paste(Image.open(abs + eval('ds' + letter)), (0, 0), mask=Image.open(abs + eval('ds' + letter)))
        elif index == len(seqdna) - 1:
            dnacanvas.paste(Image.open(abs + eval('de' + letter)), (0, index*460), mask=Image.open(abs + eval('de' + letter)))
        else:
            dnacanvas.paste(Image.open(abs + eval('dm' + letter)), (0, index*460), mask=Image.open(abs + eval('dm' + letter)))
    
    for index, letter in enumerate(seqrna):
        if index != len(seqrna) - 1:
            rnacanvas.paste(Image.open(abs + eval('rs' + letter)), (0, index*460), mask=Image.open(abs + eval('rs' + letter)))
        else:
            rnacanvas.paste(Image.open(abs + eval('re' + letter)), (0, index*460), mask=Image.open(abs + eval('re' + letter)))
    
    canvas.paste(dnacanvas, (0, 0 + 600))
    canvas.paste(rnacanvas, (1750, 0 + 600))

    if __name__ == '__main__':
        canvas.show()

    canvas.save(abs + '/static/img/output.png')

if __name__ == '__main__':
    genstructure('gugugugucaugcucgauguucguagcuuuuuuuuucgaucgu')