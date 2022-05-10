"""
Script que implementa a PARTE II do enunciado do Projecto 1.
O script deve ser chmado da seguinte forma:
    python[3] excel.py

Projecto realizado por:
    Carlos Pinto
    
"""
# aqui defini-se as funções necessárias
def  cel_n_pos(cel:str) -> int:
    """
    Dada uma célula do Excel (string), a função devolve a posição de início dos números, ou seja,
    a posição de início da linha. Devolve um inteiro.
    """
    for c in cel:
        if(ord(c) < 59):
            return cel.rindex(c)
           
def letras(cel:str) ->str:
    """
    Dada uma célula do Excel (string), a função devolve as letras, ou seja, a coluna.
    """
    return cel[:cel_n_pos(cel)]

def numeros(cel:str) -> int:
    """
    Dada uma célula do Excel (string), a função devolve os dígitos, ou seja, a linha.
    """
    return int(cel[cel_n_pos(cel):])

def line(cel:str) -> int:
    """
    Dada uma célula do Excel, a função converte a linha para o sistema de linhas,
    com índice inicial em 0.
    """
    return numeros(cel)-1

def sysconvertion(letras:str, dic:dict):
    """
    Esta função recebe as letras de uma coluna Excel,
    e um dicionário com a correspondência letra->valor
    e faz a conversão para um sistema numérico,
    considerando essa valoração dada pelo dicionário (letra: valor), nesse sistema.
    """
    inv = letras[::-1]
    total = 0
    for i, c in enumerate(inv):
        total += 26**i * dic.get(c)
    return total -1

def valida_input(cel:str) -> bool:
    """
    Valida que os caracteres digitados se encontram na parte do ASCII de 65 para cima.
    Permite verificar que não é número.
    Poderia fazer com um dicionário...de foma mais precisa, ou com uma lista, ou tuplo.
    """
    return True if (ord(cel[0]) > 64) else False
    

#aqui inicia o programa
if __name__ == '__main__':

# vou gerar automaticamente um dicionário, para auxiliar nos cálculos
    value_chars={}
    for x in range(1,27):
        value_chars.update({chr(x+64):x})
# interação com utilizador até que digite 'sair' ou insira determinados valores inválidos
    while True:
        cel = input('Indique as coordenadas: ').upper().replace(' ','')
        if cel == 'SAIR':
            print('Fim do programa')
            break
        elif valida_input(cel) != True:
            print(f'Utilização: Deverá informar a célula do excel no formato "A1" (letras da coluna seguidas do número da linha)')
            break     
    
        column = sysconvertion(letras(cel),value_chars)

        print(f'Linha: {line(cel)}  Coluna: {column}')
        print('---')


