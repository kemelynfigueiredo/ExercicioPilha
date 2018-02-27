class Pilha():
    def __init__(self):
        self.itens = list()
    def push(self,elemento):
        if self.maxi(10):
            self.itens.append(elemento)
    def isVazio(self):
        return len(self.itens)== 0         
    def pop(self):
        if not self.isVazio():
            return self.itens.pop()
    def maxi(self, maximo):
        if len(self.itens) == maximo:
            return False
        return True
    def desempilhar(self):
        a = 0
        while not self.isVazio():
            a+=self.itens.pop()
        return a
    def exibir(self):
        for i in range(len(self.itens)):
            print (self.itens[i])
p = Pilha()
for i in range(16):
    if i % 3 == 0:
        p.push(i)
p.exibir()

p = Pilha()
for i in range(16):
    if i % 3 == 0:
        p.push(i)
    elif i % 4 == 0:
        p.pop()
p.exibir()
