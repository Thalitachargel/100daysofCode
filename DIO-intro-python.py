#!/usr/bin/env python
# coding: utf-8

#  # Introdução a programação em Python 🐱‍💻
#    ## Digital Inovation One

# ## Modulo 6
# 🐍 Organizando conjuntos e subconjuntos de elementos em Python
# 

# In[3]:


# O que é conjunto:
conjunto = {1, 2, 3, 4}
print(type(conjunto))


# In[4]:


# Conjunto não permite duplicidade
conjunto_Duplo = {1, 2, 3, 4, 4, 2}
print(conjunto_Duplo)


# In[5]:


# adincionando elementos ao conjunto
conjunto.add(5)
conjunto


# In[7]:


# removento elemento
conjunto.discard(2)
conjunto


# ### Operações com conjuntos

# In[11]:


# União entre conjuntos
conj1 = {1, 2, 3, 4, 5}
conj2 = {5, 6, 7, 8}
print( f'conjunto 1 ={ conj1} e conjunto 1 = {conj2}')
conj_uniao = conj1.union(conj2)
conj_uniao


# In[12]:


# Intersecção entre conjuntos
conj_interseccao = conj1.intersection(conj2)
conj_interseccao


# In[16]:


# Diferença
conj_diferencaA = conj1.difference(conj2)
conj_diferencaB = conj2.difference(conj1)
print(f"conj1 ≠ conj2 = {conj_diferencaA} e conj2  ≠ conj1 = {conj_diferencaB}")


# In[20]:


# diferença simétrica (o não tem nos dos conjuntos, ou seja,
# todos os elementos que não são compartilhados entre os conjuntos)
conj_dif_simetrico = conj1.symmetric_difference(conj2)
conj_dif_simetrico


# ### Pertinencia

# In[33]:


# Is subset - Se um conjunto é um subconjunto de outro
conjA = {1, 2, 3}
conjB = {1, 2, 3, 4, 5}
conj_subset = conjA.issubset(conjB)
conj_subset2 = conjB.issubset(conjA)
conj_subset2
if conj_subset == True:
    print("Conjunto A é subset do Conjunto B")
else:
    print("Conjunto B é subset do Conjunto A")

if conj_subset2 == True:
    print("Conjunto A é subset do Conjunto B")
else:
    print("Conjunto B é subset do Conjunto A")


# In[36]:


# Super conjunto
conj_superset = conjA.issuperset(conjB)
conj_superset1 = conjB.issuperset(conjA)

if conj_superset == True:
    print("Conjunto A é superconjunto do Conjunto B")
else:
    print("Conjunto B é superconjunto do Conjunto A")
    
if conj_superset1 == True:
    print("Conjunto A é superconjunto do Conjunto B")
else:
    print("Conjunto B é superconjunto do Conjunto A")


# In[46]:


# convertendo uma lista em conjunto
lista = ['cachorro', 'gato', 'gato', 'elefante']
conj_animais = set(lista)
print(conj_animais, type(lista), type(conj_animais))


# In[51]:


# converter de volta a lista
#lista_animais = list(conj_animais)
#print(lista_animais, type(lista_animais))


# ## Módulo 7 - Construindo Métodos, Funções e Classes em Python

# In[56]:


# condicional IF, else
a = int(input("Primeiro Valor: "))
b = int(input("Segundo valor: "))


if a > b:
    print(f'O primeiro valor, {a}, é maior que o segundo valor, {b}.')
else:
    print(f'O segundo valor, {b}, é maior que o primeiro valor, {a}.')


# In[58]:


# E Elif

a = int(input("Primeiro Valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro Valor: "))

if a > b and a > c:
    print(f'O maior numero é o primerio, {a}.')
elif b > a and b > c:
    print(f'O maior numero é o segundo, {b}.')
else:
    print(f'O maior numero é o terceiro, {c}.')


# In[62]:


# Exercício
# saber se o numero digitado é par
n = int(input("Digite um número:"))
if n == 0:
    print("Digite um número diferente de zero!")
elif n % 2 == 0:
    print(f'O número {n} é par.')
else:
    print(f'O número {n} é impar')


# In[63]:


# função é tudo aquilo que retorna valor
# Método é Definição e não retorna valor

def soma(a, b):
    return a + b  # como tem retorno, vira uma função


print(soma(1, 2))
print(soma(3, 4))


# In[64]:


def subtracao(a, b):
    return a - b


print(subtracao(10, 2))


# In[76]:


# Classe

def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return (a / b)


print(multiplicacao(10, 2))
print(divisao(50, 5))

# Transformando em classe


class Calculadora:

    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b


calculadora = Calculadora(10, 2)
print(calculadora.a, calculadora.b)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())


# In[79]:


# Calculadora 2
class Calculadora2:

    def __init__(self):
        pass
    
    
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b
    
calculadora2 = Calculadora2()

print(calculadora2.soma(10,2))
print(calculadora2.subtracao(5,3))
print(calculadora2.multiplicacao(100,2))
print(calculadora2.divisao(10,5))


# In[95]:


# criar uma televisão usando Class

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1
        else:
            print("A tv está desligada")

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1
        else:
            print("A tv está desligada")


televisao = Televisao()
print(f'A televisão está ligada: {televisao.ligada}')
televisao.power()
print(f'A televisão está ligada: {televisao.ligada}')
televisao.power()
print(f'A televisão está ligada: {televisao.ligada}')
print(f'Canal {televisao.canal}')
televisao.aumenta_canal()
televisao.power()
televisao.aumenta_canal()
televisao.aumenta_canal()
print(f'Canal {televisao.canal}')
televisao.diminui_canal()
print(f'Canal {televisao.canal}')


# ### Módulo 8 - Lidando com módulos, importação de classes, métodos e lambdas

# In[100]:


#modulo - são os arquivos py
#import ClasseTelevisao #O exercicio proposto só funciona no PY;.


# In[108]:


def contador_de_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador


if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contador_de_letras(lista))

list1=['cachorro', 'gato', 'elefante']    
total_de_letras_lista = contador_de_letras(list1)
print(f'Total letras da lista {list1} é {total_de_letras_lista}')


# In[107]:


list1=['cachorro', 'gato', 'elefante']    
total_de_letras_lista = contador_de_letras(list1)
print(total_de_letras_lista)


# In[110]:


#Função anonima
# convertendo o contador em uma função anonima

lista_animais = ['cachorro', 'gato', 'elefante']
#contador_letras = lambda lista # paramentro : [Len (x) for x in lista] #devolução
#passe o for de x pela lista, e retorne o len de x em forma de lista
contador_letras = lambda lista : [len(x) for x in lista]
contador_letras(lista_animais)


# In[115]:


soma2 = lambda a, b:  a + b


soma2(2, 3)


# In[127]:


#criando um dicionario de lambdas
calculadora3 ={ 'soma': lambda a, b: a + b,
               'subtracao': lambda a, b : a - b,
               'multiplicacao': lambda a, b: a * b,
               'divisao': lambda a, b : a / b}
type(calculadora3)


# In[128]:


cal3 = calculadora3['soma']


# In[129]:


cal3(2,3)


# ### Modulo 9 - Gere, copie, mova e escreva

# ### Módulo 10 Aprenda a utilizar data e hora
# 

# In[183]:


#Importanto a biblioteca
from datetime import date, time, datetime, timedelta


# In[135]:


data_atual = date.today()
data_atual


# In[137]:


#Formatando data atual
data_atual.strftime('%d/%m/%y')


# In[138]:


data_atual.strftime('%d/%m/%Y')


# In[139]:


data_atual.strftime('%d * %m * %y')


# In[140]:


data_atual.strftime('%d ~%m~%y')


# In[143]:


data_atual_str = data_atual.strftime('%A/%B/%Y')
data_atual_str


# In[145]:


type(data_atual) #datetime.date
type (data_atual_str) #string


# In[186]:


# time
def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A  %B  %Y')
    dia1 = data_atual.day
    print(data_atual_str, dia1)


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))


def trabalhando_com_datetime():
    data_atual = datetime.now()
    dia = data_atual.strftime('%d  %m  %y')
    hora = data_atual.strftime('%H, %M %S')
    completa = data_atual.strftime('%c')
    print(data_atual, dia, hora, completa)
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta',
             'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2008, 5, 25, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_str = '21/03/1985 12:20:22'
    data_con = datetime.strptime(data_str, '%d/%m/%Y %H:%M:%S')
    print(data_str)
    #subtração de data e hora
    nova_data = data_con - timedelta(days = 365, hours = 2)
    print(nova_data.strftime('%d -  %m - %Y'))
    
    



if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()


# ### Módulo 11 Gerenciando e criando excessões

# In[187]:


# forçando um erro
divisao = 10 / 0


# In[189]:


try:
    divisao = 10 / 0
except  ZeroDivisionError:
    print('Não é possivel dividir por zero')


# In[191]:


# forçar erro
lista = [1, 10]
numero = lista[3]


# In[198]:


try:
    lista = [1, 2]
    numero = lista[3]
except IndexError:
    print("Erro ao acessar indice inesistente")
except:
    print('Erro desconhecido')


# In[204]:


try:
    x = alma
    print(alma)
except BaseException as ex:
    print(f'Erro desconhecido. Erro tipo: {ex}.')


# In[211]:


#else
arquivo = open('teste.txt', 'w')
try:
    texto = arquivo.read()
    print('fechar arquivo')
    arquivo.close()
  
    
except ZeroDivisionError:
    print("não é possivel dividr por zero")
except ArithmeticError:
    print("Erro de op aritmetica")
except IndexError:
    print("Erro ao acessar indice inesistente")
except BaseException as ex:
    print(f'Erro desconhecido. Erro tipo: {ex}.')
else:
    print('Executa quando não ocorre exceção')


# In[213]:


arquivo = open('teste.txt', 'w')
try:
    texto = arquivo.read()
    print('fechar arquivo')
    
  
    
except ZeroDivisionError:
    print("não é possivel dividr por zero")
except ArithmeticError:
    print("Erro de op aritmetica")
except IndexError:
    print("Erro ao acessar indice inesistente")
except BaseException as ex:
    print(f'Erro desconhecido. Erro tipo: {ex}.')
else:
    print('Executa quando não ocorre exceção')

arquivo.close()


# In[223]:


#Exercicio
while True:
    try:
        nota = int(input("Digite uma nota entre 0 e 10: "))
        print(nota)
        if x > 10: 
            
        break
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas Numeros.")
       


# In[222]:


#criando classe de excessão
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message
        
        
    


# In[ ]:


while True:
    try:
        nota = int(input("Digite uma nota entre 0 e 10: "))
        print(nota)
        if nota > 10: 
            raise InputError('O valor não pode ser maior que 10')
        elif nota < 0:
            raise InputError('O valor não pode ser negativo')
        break
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas Numeros.")
    except InputError as ex:
        print(ex)


# ### Modulo 12 e final: Instalando pacotes e request

# In[230]:


pip list


# In[235]:


#bibliotecas ou pacotes
get_ipython().system('pip install requests')


# In[236]:


pip freeze


# In[240]:


import requests


# In[250]:


#testando o requests
response = requests.get('https://viacep.com.br/ws/70165900/json/')
print(response.status_code) # sucesso = 200
print(response.text)
print(response.json()) #em formato de dicionário
print(type(response.text))


# In[252]:


dado_cep = response.json()
print(dado_cep['logradouro'])
print(dado_cep['complemento'])


# In[256]:


def pokemon(nome_pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nome_pokemon}')
    dados_pokemon = response.json()
    return dados_pokemon
pokemon('ditto')    


# In[257]:


#request de sites comuns
def retorna_response(url):
    response = requests.get(url)
    return response.txt
    


# In[262]:


print(retorna_response('https://recruit.navercorp.com/global/recruitMain'))


# In[ ]:




