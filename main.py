import random
import copy
from itertools import permutations

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

def gerarPopulacaoInicial(tamanhoTabuleiro):
    tamanhoPopulacao = tamanhoTabuleiro * 2
    populacao = []
    solucaoBasica = []
    for i in range(tamanhoPopulacao):
        solucaoBasica.append(i)

    permutacoes = permutations(solucaoBasica, tamanhoTabuleiro)
   
    individuos = []

    contador = 0
    for i in range(tamanhoPopulacao):
        sorteado = 0
        solucao = []
        for elem in permutacoes:
            contador += 1
            genes = []
            for gene in elem:
                genes.append(gene)
            individuos.append(genes)
       
        populacao.append(individuos[random.randint(0, contador)])
    return populacao
   

print(gerarPopulacaoInicial(7))
