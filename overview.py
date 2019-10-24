'''
num = 0

if (num % 2 == 0):
    print ('o numero eh par')
else:
    print('o numero é impar') 

while(num < 10):
    print(num)
    num = num + 1

def isPar(num):
    if (num % 2 == 0):
        return True
    return False

print(isPar(6))

lista = [1, 2, 3,4,5,6,7]

for item in lista:
    print(item)

print('-----')
for item in range(len(lista)):
    print(lista[item])
'''
class Pessoa:
    
    def __init__(self, nome, idade, hobbie):
        
        self.nome = nome
        self.idade = idade
        self.hobbie = hobbie
    
    def obter(self):
        return self.nome

p = Pessoa('johw', 26, 'violao')

print(p.obter())