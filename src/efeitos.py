"""
Script que implementa a PARTE I do enunciado do Projecto 1.
O script deve ser chmado da seguinte forma:
    python[3] efeitos.py palavra1 [palavra2] ...[palavraN]

Projecto realizado por:
    Carlos Pinto
    João Leigo
"""
import sys
import time
import subprocess
from docopt import docopt

# constantes globais declaradas
PAUSE = 0.5
ONOFF = 'on'
FRAMELEN = 40
    
doc="""
The Script implements PARTE I from the Projecto 1.

Usage:
    efeitos.py [-i SLEEP] PALAVRA [PALAVRA ...]

Option:
    -i SLEEP, --interval=SLEEP      Sets interval
"""
args = docopt(doc)

#Definição das Funções
def cls():
    """
    A função deteta o Sistema Operativo, e executa o comando apropriado para limpar o ecrã.
    Esta função é um procedimento que não recebe inputs e não devolve nada.
    """
    if sys.platform in ('linux', 'darwin', 'unix'):
        subprocess.run(['clear'])
    elif sys.platform == 'win32':
        subprocess.run(['cls'], shell=True)

def fdiagonal_principal(frase: str, efeito:str = ONOFF):
    """
    Exibe o texto dado pelo parâmetro frase, na diagonal principal.
    Este procedimento não devolve nada.
    """
    espaco = ''
    
    for l in frase:
        print(espaco, l, end ='')
        espaco += ' '
        if (str.lower(efeito) == 'on'):
            time.sleep(PAUSE)
        print()
    print('---')

def fdiagonal_principal_inv(frase:str, efeito:str = ONOFF):
    """
    Exibe o texto dado pelo parâmetro frase, na diagonal principal,
    mas de trás para a frente.
    Este procedimento não devolve nada.
    """
    espaco = ''
    
    for l in frase[::-1]:
        print(espaco, l, end ='')
        espaco += ' '
        if (str.lower(efeito) == 'on'):
            time.sleep(PAUSE)
        print()
    print('---')


def fdiagonal_secundaria_inv(frase: str, efeito:str ='on'):
    """
    Exibe o texto dado pelo parâmetro frase, na diagonal secundária,
    mas de tràs para a frente. [FUNÇÃO NÃO UTILIZADA NO ENUNCIADO]
    Este procedimento não devolve nada.
    """
    for i, l in enumerate(frase[::-1]):
        espaco = ' ' * (lenf - i)
        print(espaco, l, end ='')
        if (str.lower(efeito) == 'on'):
            time.sleep(PAUSE)
        print()
    print('---')

def fdiagonal_secundaria_bk(frase:str, efeito:str = 'on'):
    """
    Exibe o texto dado pelo parâmetro frase, na diagonal secundária,
    a partir da última palavra até à primeira.
    Este procedimento não devolve nada.
    """
    lista = args['PALAVRA'][::-1]
    frase = ' '.join(lista)
    for i, l in enumerate(frase):
        espaco = ' ' * (lenf - i)
        print(espaco, l, end ='')
        if (str.lower(efeito) == 'on'):
            time.sleep(PAUSE)
        print()
    print('---')
    
def fdiagonais_cruzadas(frase:str, efeito:str = 'on'):
    """
    Exibe o texto dado pelo parâmetro frase, nas diagonais,
    principal e secundária, cruzando-se a meio da string.
    Este procedimento não devolve nada.
    """
    t = len(frase)

    for i, l in enumerate(frase):
        for k in range(t):
            print(l, end='') if(i == k or i + k == t-1) else print (' ', end='')
        print()
        if (str.lower(efeito) == 'on'):
            time.sleep(PAUSE)
    print('---')

#Funções para criar efeito texto deslizante

def clean_frame(t_grelha:int) -> list:
    grelha=[]
    for i in range(t_grelha):
        grelha.append(' ')
    return grelha

def mount_frase_in_list(frase:str) -> list:
    """
    Pega na frase, preenche o resto com espaços e transforma numa lista
    """
    frase = frase + (FRAMELEN - len(frase)) * ' '
    return list(frase)

def step_foward(frame:list) ->list:
    """
    Devolve a lista com a frase um índice mais à frente,
    caso o caracter a mover já não caiba na lista,
    move para primeira posição. 
    """
    new_frame = clean_frame(FRAMELEN)
    
    for i in range(FRAMELEN):
        if (i < (FRAMELEN-1)):
            new_frame[i+1] = frame[i]
        else:
            new_frame[0] = frame[i]
    return new_frame

def roda_frase(frase:str, i:float = 1):
    """
    Implementa animação de frases, as quais rodam numa frame,
    em ciclo repetitivo até ser interrompido pelo utilizador.
    """
    while True:
        cls()
        frase = ''.join(step_foward(mount_frase_in_list(frase)))
        print(frase)
        time.sleep(i)


def avanca():
    """
    Espera que itilizador pressione Enter e em sequência limpa ecrã
    """
    input("pressione Enter para continuar")
    cls()


#execução começa aqui:
if __name__ == '__main__':

    frase = ' '.join(args['PALAVRA'])
    lenf = (len(frase))
    i = float(args['--interval']) if args['--interval'] else 1

    fdiagonal_principal(frase)
    avanca()
    fdiagonal_principal_inv(frase)
    avanca()
    fdiagonais_cruzadas(frase)
    avanca()
    fdiagonal_secundaria_bk(frase)
    avanca()
    roda_frase(frase, i)



    


