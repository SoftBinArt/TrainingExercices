"""
Script que implementa a PARTE III do enunciado do Projecto 1.
O script deve ser chmado da seguinte forma:
    ccypher.py -e [-s SHIFT] FILE
    ccypher.py -d -s SHIFT FILE

Projecto realizado por:
    Carlos Pinto
    João Leigo
"""
from random import randint
from docopt import docopt

doc="""
Given a file the program cifers the file making a shift in char.
If no shift is given the program gives a random one.
The output is writen in FILE.pdf.

Usage:
    ccypher.py -e [-s SHIFT] FILE
    ccypher.py -d -s SHIFT FILE

Options:
    -e , --encript                  encripts file
    -d , --decript                  decripts file    
    -s SHIFT, --shift=SHIFT         shift to use in cyphering 
"""
args = docopt(doc)

file = args['FILE']
with open(file, 'rt') as file:
    if(args['--shift'] == None):
        desloc = randint(1,255)
        print(desloc, '<-password')
    else:
        desloc = int(args['--shift'])
    
    
    desloc = (-1 * desloc) if args['--decript'] == True else desloc
    
    text = file.read()
    with open(args['FILE'] + '.pdf', 'wt') as dest_file:
        for c in text:
            if (ord(c) + (desloc)) < 0:
                cypher = (255 - (ord(c) + desloc))
            else:
                cypher = (ord(c) + (desloc)) % 255
            dest_file.write(chr(cypher))



