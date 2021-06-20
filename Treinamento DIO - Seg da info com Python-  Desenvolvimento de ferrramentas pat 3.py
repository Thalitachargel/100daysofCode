#!/usr/bin/env python
# coding: utf-8

# # Desenvolvimento de Ferramentas
# 

# ## Verificador de telefone

# In[8]:


#Biblioteca
#!pip install phonenumbers
import phonenumbers as ph
from phonenumbers import geocoder as geo


# In[14]:


phone = input('Digite o telefone no formato : +551199999999 \n')
phone_numbers = ph.parse(phone)
print(geo.description_for_number(phone_numbers, 'pt'))


# ## Desenvolvendo um ocultador de arquivos
# se comunica com o C# e permite trabalhar com liguagem de baixo nível

# In[16]:


#bibliotecas
import ctypes as ct


# In[18]:


#definir o atributo de aqruivo oculto
atributo_ocultar = 0x02
retorno = ct.windll.kernel32.SetFileAttributesW('Ocultar.txt', atributo_ocultar)

if retorno:
    print('arquivo foi ocultado')
else:
    print('Arquivo não foi ocultado')


# ## Desenvolvendo um verificador de IP Externo:

# In[19]:


#importar biblioteca
import re
import json
from urllib.request import urlopen as up


# In[20]:


url = 'https://ipinfo.io/json'
resposta = up(url)
dados = json.load(resposta)


# In[23]:


ip = dados['ip']
org = dados['org']
cid = dados['city']


# In[28]:


print('Detalhes do IP exeterno: \n')
#print(f'IP: {ip}\nOrg:{org}\nCidade: {cid}.')


# ## Ferramenta Gráfica para abrir no navegador:

# In[32]:


#bibliotecas
import webbrowser as wb
from tkinter import * 


# In[33]:


root = Tk( ) # quando tem espaço é none

root.title('Abrir Browser')
root.geometry('300x200')


# In[ ]:


def google():
    wb.open('www.google.com')
    
mygoogle = Button(root, text = 'Abrir o google', command = google).pack(pady=20)


# In[ ]:


root.mainloop()


# In[ ]:




