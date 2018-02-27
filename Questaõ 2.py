class Pilha:
    def __init__(self):
        self.itens = list()
    def isVazio(self):
        return len(self.itens) == 0
    def push(self, elemento):
            if elemento not in self.itens:
                self.itens.append(elemento)
    def pop(self):
        if not self.isVazio():
            return self.itens.pop()
    def peek(self):
        return self.itens[-1]
    def length(self):
        return len(self.itens)
pilha = Pilha()
