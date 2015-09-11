''' 
    Analisa dados de inflamação
'''

import numpy as np 

global dados # variável global

dados = np.loadtxt(fname='inflammation.csv',
                    delimiter=",")

def get_dados():
    ''' Retorna os dados sobre inflamação '''

    return dados 

def get_media():
    '''Retorna a média da temperatura por dia'''
    return dados.mean(axis=0) # axis => eixo

def get_max():
    ''' Retorna a temperatura máxima por paciente'''

    return dados.max(axis=1)

