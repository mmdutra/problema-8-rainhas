import random
import copy
from itertools import permutations

def ataques(cromossomo):
    ataques = 0
    tamanho = len(cromossomo)
    for i in range(tamanho)
        for j in range(tamanho):
            if (abs(i-j) == abs(cromossomo[i] - cromossomo[j]) and i != j):
                ataques = ataques + 1
               
    return -1 * ataques//2

def criarFilho(pai, corte):
    filho = [None] * (len(pai))
    for i in range(corte):
        filho[i] = pai[i]
    return filho

def popularFilho(p1, p2, pos, f):
    size = len(p1)
    for i in range(pos, size):
        for j in range(size):
            if p2[j] not in f:
                f[i] = p2[j]
    return f

def cruzar(p1, p2):
    size = len(p1)
    pos = random.randint(0, size - 1)
    f1 = criarFilho(p1, pos)
    f2 = criarFilho(p2, pos)
    f1 = popularFilho(p1, p2, pos, f1)
    f2 = popularFilho(p2, p1, pos, f2)
           
    return f1, f2

def gerarIndividuo(tamanho):
    new_list = []

    while len(new_list) < tamanho:
        new_element = random.randint(0, tamanho-1)
        if new_element not in new_list:
            new_list.append(new_element)

    return new_list

def gerarPopulacaoInicial(tamanhoTabuleiro):
    tamanhoPopulacao = tamanhoTabuleiro * 2
    populacao = []
    for i in range(tamanhoPopulacao):
        individuo = gerarIndividuo(tamanhoTabuleiro)
        populacao.append(individuo)
   
    return populacao
   
print(gerarPopulacaoInicial(7))