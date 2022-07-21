import os
from PIL import Image

def genacids(acids):
    abs = os.path.dirname(__file__) + '/aminoacids/ready/'

    canvas = Image.new('RGB', (1000, len(acids)*999), '#cccccc')

    for index, acid in enumerate(acids):
        canvas.paste(Image.open(abs + acid + '.jpg'), (0, index*999))
    
    if __name__ == '__main__':
        canvas.show()
    
    canvas.save(abs + '../../static/img/acids.jpg')

if __name__ == '__main__':
    acidos = ['metionina', 'leucina', 'isoleucina', 'triptofano', 'stop']
    genacids(acidos)
