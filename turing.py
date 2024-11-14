# implementação da máquina de turing
# entrada: estados_finais,estados_iniciais,estados etc...
# entrega: 21/11/2024

# implementar uma LIFO - Last In, First Out
class Pilha:
    def __init__(self):
        self.items = []

    def eh_vazio(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.eh_vazio():
            return self.items.pop()
        return None # Retorna None se a pilha estiver vazia
    
    def peek(self):
        if not self.eh_vazio():
            return self.items[-1]
        return None # Retorna se a pilha estiver vazia
    
    def __str__(self):
        return str(self.items)

pilha_esquerda = Pilha() # Pilha para os simbolos a esquerda da cabeça
pilha_direita = Pilha() # Pilha para os simbolos a direita da cabeça

# Função para mover a cabeça para a direita
def mover_direita(simbolo_atual):
    pilha_esquerda.push(simbolo_atual) # Empurra o simbolo atual para a pilha direita
    if not pilha_direita.eh_vazio():
        return pilha_direita.pop() # Pega o proximo simbolo a direita
    
    return None # Fita vazia a direita

# Função para mover a cabeça para a esquerda
def mover_esquerda(simbolo_atual):
    pilha_direita.push(simbolo_atual) # Empurra o simbolo atual para a pilha direita
    if not pilha_esquerda.eh_vazio():
        return pilha_esquerda.pop() # Pega o proximo simbolo a esquerda
    return None # Fita vazia a esquerda

# Exemplo de uso
def teste():
    
   # Inicializa a "fita" com símbolos à direita da cabeça
   for symbol in "abc":  # Fita: "abc"
       pilha_direita.push(symbol)
   
   # Cabeça começa lendo o primeiro símbolo
   current_symbol = pilha_direita.pop()  # Começa lendo "a"
   print("Símbolo atual:", current_symbol)

   # Movendo para a direita
   current_symbol = mover_direita(current_symbol)
   print("Movido para a direita. Símbolo atual:", current_symbol)

   # Movendo para a esquerda
   current_symbol = mover_esquerda(current_symbol)
   print("Movido para a esquerda. Símbolo atual:", current_symbol)

class Turing:
    def __init__(self):
        pass