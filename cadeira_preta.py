"""
============================================================
Arquivo de exemplo com funções utilitárias
Autor: Pedro-Caixa
Descrição:
    Este arquivo demonstra:
    - Como documentar um arquivo (header file)
    - Como implementar funções básicas em Python
    - Como usar docstrings padronizadas
============================================================
"""

print("Um Header File é um arquivo onde são colocadas funções e atributos separados")

def cadeira()
 '''Esse é um doc string de uma linha só'''
    print("Esse é um docstring")

# coloque o header deste arquivo


# implemente as funções abaixo e coloque as docstrings


# Segue atividade, implemente os métodos abaixo:

def maximo(nums):
    """
    Retorna o maior valor dentro de uma lista de números.
    
    Parâmetros:
        nums (list): Lista de números (int ou float).
    
    Retorna:
        int ou float: O maior valor encontrado na lista.
    """
    maior = nums[0]
    for num in nums[1:]:
        if num > maior:
            maior = num
    return maior

def e_par(n: int) -> bool:
    """
    Verifica se um número é par.
    
    Parâmetros:
        n (int): Número inteiro a ser verificado.
    
    Retorna:
        bool: True se for par, False caso contrário.
    """
    return n % 2 == 0


def fatorial(n: int) -> int:
    """
    Calcula o fatorial de um numero de forma iterativa.
    
    Parâmetros:
        n (int): Número inteiro não-negativo.
    
    Retorna:
        int: O valor de n! (fatorial de n).
    """
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
