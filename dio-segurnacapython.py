#!/usr/bin/env python
# coding: utf-8

# ## Desenvolendo um gerador de Senha
# Dio - Segurança da informação com Python
# 
# ಥ_ಥ
# 
# (。_。)
# 

# In[8]:


# importando bibliotecas
import random
import string


# In[12]:


# criando o objeto com o tamanho da senha  a ser criada
tamanho = int(input('Digite o tamanho de senha que você deseja:     '))
# criando o objeto com o formato da senha  a ser criada
# so munuscula usar o ascii_lowercase # para letras maisculas ascii_uppecase

chars = string.ascii_letters + string.digits + 'ç@#$%&*()-+=,.:;/?'

# usa a classe os.urandom, pra gerar numeros aleatorios apartir de fontes do sistema operacional

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars)
              for i in range(tamanho)))


# ## Desenvolvendo um comparador de Hashs

# In[13]:


#importando bibliotecas
import hashlib


# In[17]:


# Criando os arquivos a serem comparados
arquivo1 = 'a.txt'
arquivo2 = 'b.txt'


# In[23]:


hash1 = hashlib.new('ripemd160') #vai passar uma string que indicara qual algoritmo de encrypt deve usar
hash2 = hashlib.new('ripemd160')


# In[24]:


hash1.update(open(arquivo1, 'rb').read())
hash2.update(open(arquivo2, 'rb').read())


# In[31]:


# comparando os hashs
if hash1.digest() != hash2.digest():
    print(f'O arquivo {arquivo1} é diferente do {arquivo2}.')
    print(f'O Hash do arquivo {arquivo1} é igual ao {hash1.hexdigest()}')
    print(f'O Hash do arquivo {arquivo2} é igual ao {hash1.hexdigest()}')
else:
    print(f'O arquivo {arquivo1} é igual ao {arquivo2} ')
    print(f'O Hash dos arquivos {arquivo1} e {arquivo2} é igual ao {hash1.hexdigest()}')


# ## Trabalhando com Threads e IP's

# In[55]:


#thread
import time
def carro(velocidade, piloto):
    if velocidade <= 0:
        print('A velocidade não pode ser negativa')
    else:    
        trajeto = 0
        while trajeto <= 100:
           
        
            trajeto += velocidade
            time.sleep(0.5)
            print(f'Piloto : {piloto} --  km:{trajeto} \n')
            
            



# In[46]:


#Importanto a Biblioteca
from threading import Thread


# In[57]:


# fazer o multithreading
t_carro1 = Thread(target=carro, args=[10, 'Bruno'])
t_carro2 = Thread(target=carro, args=[20, 'Python'])

t_carro1.start()
t_carro2.start()


# In[59]:


# Manipulação de Ip's
import ipaddress


# In[66]:


#Ip aleatorio em string
ip = '192.168.0.1'
endereco = ipaddress.ip_address(ip)
print(endereco)
print(endereco + 100)
print(endereco + 256)


# In[78]:


iprede = '192.168.0.0/24' 
rede =  ipaddress.ip_network(iprede)
print(rede)


# In[77]:


ipredeerro = '192.168.0.100/24' 
redeerro =  ipaddress.ip_network(ipredeerro, strict = False)
print(redeerro)


# In[79]:


for ip in rede:
    print(ip)


# In[ ]:




