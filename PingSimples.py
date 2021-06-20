
import OS
#criando variavel do Ip pingavel
print('#' * 60)
ip_ou_host = input("Digite o Ip ou Host ao ser verificado: ")
print('-' * 60)
OS.system('ping -n 6 {}'.format(ip_ou_host))

