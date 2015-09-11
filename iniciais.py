# programa para criar histograma com a quantidade de palavras para cada letra

import io
import pprint

f = io.open('/home/casa/Área de Trabalho/python-novice-inflammation/pt_BR.dic', encoding='iso-8859-1')
palavras = f.read()
palavras = palavras.split('\n')

#print(len(palavras))

# criando o dicionário vazio
letras = {} 

for palavra in palavras:
    if palavra:
        # verificando se a inicial consta no dicionario
        inicial = palavra[0]
        if inicial not in letras:
            letras[inicial] = 1
        else:
            letras[inicial] = letras[inicial]  + 1

#pprint.pprint(letras)

# isso veio desordenado, para ordenar podemos fazer
list(letras) # exibira as keys
sorted(letras) # ordena pelos maiores

sorted(letras,key=str.upper) # antes de ordenar, processe os itens com a funcao str.upper



#### Jeito hiperfácil 

# usando Counter
#from collections import Counter

#Counter('aaabbbbbbbbccz')
# fuçar esse fulano e tentar fazer