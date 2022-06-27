import os
import math
from imgpaths import *
from PIL import Image

def genimg(seq):
    abs = os.path.dirname(__file__) + '/'

    mid = abs + 'dnasprites/middle.png'

    canvas = Image.new('RGB', (1920, len(seq)*80 + 130), '#cccccc')
    dnacanvas = Image.new('RGB', (389, len(seq)*80), '#cccccc')
    rnacanvas = Image.new('RGB', (389, len(seq)*80), '#cccccc')
    seqdna = ''
    seqrna = seq

    for i in seq:
        if i == 'u':
            seqdna += 't'
        else:
            seqdna += i

    positions = '..'

    dnalist = []
    rnalist = []
    for index, base in enumerate(seqdna):
        if (math.floor(index/8)) % 2 == 0:
            if base == 'a':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    dnalist.append(abs + at4vd)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    dnalist.append(abs + at3vd)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    dnalist.append(abs + at2vd)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    dnalist.append(abs + at1vd)
            if base == 't':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    dnalist.append(abs + ta4vd)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    dnalist.append(abs + ta3vd)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    dnalist.append(abs + ta2vd)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    dnalist.append(abs + ta1vd)
            if base == 'g':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    dnalist.append(abs + gc4vd)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    dnalist.append(abs + gc3vd)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    dnalist.append(abs + gc2vd)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    dnalist.append(abs + gc1vd)
            if base == 'c':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    dnalist.append(abs + cg4vd)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    dnalist.append(abs + cg3vd)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    dnalist.append(abs + cg2vd)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    dnalist.append(abs + cg1vd)
        else:
            if base == 'a':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    dnalist.append(abs + ta4vd)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    dnalist.append(abs + ta3vd)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    dnalist.append(abs + ta2vd)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    dnalist.append(abs + ta1vd)
            if base == 't':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    dnalist.append(abs + at4vd)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    dnalist.append(abs + at3vd)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    dnalist.append(abs + at2vd)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    dnalist.append(abs + at1vd)
            if base == 'g':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    dnalist.append(abs + cg4vd)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    dnalist.append(abs + cg3vd)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    dnalist.append(abs + cg2vd)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    dnalist.append(abs + cg1vd)
            if base == 'c':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    dnalist.append(abs + gc4vd)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    dnalist.append(abs + gc3vd)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    dnalist.append(abs + gc2vd)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    dnalist.append(abs + gc1vd)
    positions = '..'
    for index, base in enumerate(seqrna):
        if (math.floor(index/8)) % 2 == 0:
            if base == 'a':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    rnalist.append(abs + a_4vr)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    rnalist.append(abs + a_3vr)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    rnalist.append(abs + a_2vr)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    rnalist.append(abs + a_1vr)
            if base == 'u':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    rnalist.append(abs + u_4vr)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    rnalist.append(abs + u_3vr)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    rnalist.append(abs + u_2vr)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    rnalist.append(abs + u_1vr)
            if base == 'g':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    rnalist.append(abs + g_4vr)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    rnalist.append(abs + g_3vr)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    rnalist.append(abs + g_2vr)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    rnalist.append(abs + g_1vr)
            if base == 'c':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    rnalist.append(abs + c_4vr)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    rnalist.append(abs + c_3vr)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    rnalist.append(abs + c_2vr)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    rnalist.append(abs + c_1vr)
        else:
            if base == 'a':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    rnalist.append(abs + a4vr)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    rnalist.append(abs + a3vr)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    rnalist.append(abs + a2vr)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    rnalist.append(abs + a1vr)
            if base == 'u':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    rnalist.append(abs + u4vr)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    rnalist.append(abs + u3vr)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    rnalist.append(abs + u2vr)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    rnalist.append(abs + u1vr)
            if base == 'g':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    rnalist.append(abs + g4vr)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    rnalist.append(abs + g3vr)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    rnalist.append(abs + g2vr)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    rnalist.append(abs + g1vr)
            if base == 'c':
                if (positions[-2] == '.' and positions[-1] == '.') or (positions[-2] == '2' and positions[-1] == '3') or (positions[-2] == '3' and positions[-1] == '4'):
                    positions += '4'
                    rnalist.append(abs + c4vr)
                elif (positions[-2] == '4' and positions[-1] == '4') or (positions[-2] == '.' and positions[-1] == '4') or (positions[-2] == '1' and positions[-1] == '2'):
                    positions += '3'
                    rnalist.append(abs + c3vr)
                elif (positions[-2] == '4' and positions[-1] == '3') or (positions[-2] == '1' and positions[-1] == '1'):
                    positions += '2'
                    rnalist.append(abs + c2vr)
                elif (positions[-2] == '3' and positions[-1] == '2') or (positions[-2] == '2' and positions[-1] == '1'):
                    positions += '1'
                    rnalist.append(abs + c1vr)

    for i in range(0,len(dnalist)+len(dnalist)-1, 9): 
        dnalist[i:i]=[mid]

    while dnalist[-1] == mid:
        dnalist.pop()

    for i in range(0,len(rnalist)+len(rnalist)-1, 9): 
        rnalist[i:i]=[mid]

    while rnalist[-1] == mid:
        rnalist.pop()

    dnalist = dnalist[1:]
    rnalist = rnalist[1:]

    positions = positions[2:]
    positionsnew = ''
    for index, pos in enumerate(positions):
        if pos == '4' and positions[index - 1] == '4':
            positionsnew += '04'
        else:
            positionsnew += pos
    
    while positionsnew[0] == '0':
        positionsnew = positionsnew[1:]

    positionsnew = positionsnew[0:]
    height = len(dnalist) * 68 
    for index, path in enumerate(dnalist):
        if positionsnew[index] == '0':
            dnacanvas.paste(Image.open(path), (163, 68 * index), mask=Image.open(path))
        elif positionsnew[index] == '4':
            dnacanvas.paste(Image.open(path), (111, 68 * index), mask=Image.open(path))
        elif positionsnew[index] == '3':
            dnacanvas.paste(Image.open(path), (64, 68 * index), mask=Image.open(path))
        elif positionsnew[index] == '2':
            dnacanvas.paste(Image.open(path), (17, 68 * index), mask=Image.open(path))
        elif positionsnew[index] == '1':
            dnacanvas.paste(Image.open(path), (0, 68 * index), mask=Image.open(path))

    for index, path in enumerate(rnalist):
        if path[-6] == '_':
            if positionsnew[index] == '4':
                rnacanvas.paste(Image.open(path), (111, 68 * index), mask=Image.open(path))
            elif positionsnew[index] == '3':
                rnacanvas.paste(Image.open(path), (64, 68 * index), mask=Image.open(path))
            elif positionsnew[index] == '2':
                rnacanvas.paste(Image.open(path), (17, 68 * index), mask=Image.open(path))
            elif positionsnew[index] == '1':
                rnacanvas.paste(Image.open(path), (0, 68 * index), mask=Image.open(path))
        else:
            if positionsnew[index] == '0':
                rnacanvas.paste(Image.open(path), (163, 68 * index), mask=Image.open(path))
            elif positionsnew[index] == '4':
                rnacanvas.paste(Image.open(path), (195, 68 * index), mask=Image.open(path))
            elif positionsnew[index] == '3':
                rnacanvas.paste(Image.open(path), (195, 68 * index), mask=Image.open(path))
            elif positionsnew[index] == '2':
                rnacanvas.paste(Image.open(path), (195, 68 * index), mask=Image.open(path))
            elif positionsnew[index] == '1':
                rnacanvas.paste(Image.open(path), (195, 68 * index), mask=Image.open(path))

    dnacanvas = dnacanvas.crop((0, 0, 389, height))
    rnacanvas = rnacanvas.crop((0, 0, 389, height))
    canvas.paste(dnacanvas, (380, 200))
    canvas.paste(rnacanvas, (1150, 200))
    canvas.save('static/img/output.png', 'PNG')
    return positionsnew


