"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import sys

def mimic_dict(filename):
  """Retorna o dicionario imitador mapeando cada palavra para a lista de
  palavras subsequentes."""
    # +++ SUA SOLUÇÃO +++
  with open(filename, 'r') as arquivo:
    dados = arquivo.read()
    lista = dados.lower().replace('\n', ' ').split()
    dic = {}
    dic.update({'':[lista[0],]})
    dic.update({lista[-1]:['',]})
    for i in range(1,len(lista)-1):
     if dic.get(lista[i]) is None:
        dic.update({lista[i]: [lista[i - 1],]})
        dic.update({lista[i]: [lista[i + 1],]})
     else:
        lista1 = dic[lista[i]]
        if lista[i - 1] in lista1:
          pass
        else:
          dic[lista[i]].append(lista[i - 1])
        if lista[i + 1] in lista1:
          pass
        else:
          dic[lista[i]].append(lista[i + 1])

    print (dic)
    return dic


def print_mimic(mimic_dict, word):
  """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
    # +++ SUA SOLUÇÃO +++
  #print (len(mimic_dict[word]))
  if str(mimic_dict[word]) != '[\'\']':
      if len(mimic_dict[word]) == 1:
        palavra = random.choice(mimic_dict[word])
        print(str(palavra) , end = ' ')
      else:
        palavra = random.choice(mimic_dict[word])
        #print(str(palavra))
        print(str(palavra) , end = ' ')
      print_mimic(mimic_dict, str(palavra))
  else:
      print('\n')
  return


# Chama mimic_dict() e print_mimic()
def main():
  if len(sys.argv) != 2:
    print('Utilização: ./14_mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
