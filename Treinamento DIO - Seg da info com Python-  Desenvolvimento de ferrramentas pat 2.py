#!/usr/bin/env python
# coding: utf-8

# # Desenvolvimento de ferramentas
# 

# ## Desenvolver um gerador de Hash

# In[4]:


#Bibliotecas
import hashlib as hs


# In[5]:


resultado = hs.md5(b'Python Security') 
#o b antes da string converte em bytes
print('O hash da string é: ', resultado.hexdigest())


# In[15]:


string = input('Digite o texto a ser gerado a HASH:  \n ')
menu = int(input('''#### MENU  -  ESCOLHA O TIPO DE HASH #### 

                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                
                Digite o número do HASH a ser Gerado \n'''))
if menu == 1:

    string_resultado = hs.md5(string.encode('utf-8'))
    print(f'O hash MD5 da string {string} é:  {string_resultado.hexdigest()}')
    
elif menu == 2:
    string_resultado = hs.sha1(string.encode('utf-8'))
    print(f'O hash SHA1 da string {string} é:  {string_resultado.hexdigest()}')

elif menu == 3:
    string_resultado = hs.sha256(string.encode('utf-8'))
    print(f'O hash SHA256 da string {string} é:  {string_resultado.hexdigest()}')
    
elif menu == 4 :
    string_resultado = hs.sha512(string.encode('utf-8'))
    print(f'O hash SHA512 da string {string} é:  {string_resultado.hexdigest()}')
else:
    print('Opção inválida!')


# ## Desenvolver um gerador de wordlist
# usado para gerar lista de palavras pra testagem ofesinvas com força bruta.

# In[17]:


#Importar bibliotecas
import itertools as it


# In[26]:


wordlistresult = it.permutations('SHINeeisBACK',  5)
for i in wordlistresult:
    print(''.join(i))


# In[34]:


# personalizando a wordlist
WLstring = input('Digite a String a ser permutada \n ')
wlrestultado = it.permutations(WLstring, len(WLstring))
for i in wlrestultado:
    print(''.join(i))


# ## Desenvolvendo um Web Scraping
# Usando no teste de invasão  
# o webscraping ajuda no primeiro passe, que é a footprint

# In[44]:


#Importar a Biblioteca
from bs4 import BeautifulSoup as bs
import requests as rs
import string


# In[39]:


url = rs.get('https://www.climatempo.com.br/').content
soup = bs(url, 'html.parser')


# In[70]:


#print(soup.prettify())
temperatura = soup.find("Temperatura")
print(temperatura)
print(soup.title.string)
print(soup.a)
print(soup.p.string)
print(soup.find('admin'))


# ## Desenvolver um Web Crawler
# Encontrar, ler e indexar páginasde um site , tb conhecido como spider ou robot.  
# 
# usado em SEO, data mining e em processos de pentest
# 
# 

# In[87]:


# Importar Bibliotecas
import operator as op
from collections import Counter 


# In[90]:


def start(url):
    wordlist = []
    source_code = rs.get(url).text

    soup = bs(source_code, 'html.parser')

    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%&*()_+-="[]{}|\<>:;?,.'

    for i in range(0, len(symbols)):
        word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)


    create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count = {}
    
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    for key, value in sorted(word_count.items(),
                             key=op.itemgetter(1)):

        print('% s : % s' % (key, value))

    c = Counter(word_count)

    top = c.most_common(18)
    print(top)

if __name__ == '__main__':
    start('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')    


# In[89]:





# In[ ]:




