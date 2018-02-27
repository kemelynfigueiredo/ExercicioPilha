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
            
            
            
        
