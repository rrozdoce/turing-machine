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
        return self.items.pop() if not self.eh_vazio() else None
    
    def peek(self):
        return self.items[-1] if not self.eh_vazio() else None
    
    def __str__(self):
        return str(self.items)

class TuringMachine:
    SIMBOLO_VAZIO = ''

    def __init__(self, estados=None, alfabeto=None, transicoes=None, estado_inicial=None, estados_de_aceitacao=None):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes if transicoes is not None else {}
        self.estado_inicial = estado_inicial
        self.estados_de_aceitacao = estados_de_aceitacao
        self.pilha_esquerda = Pilha()  # Pilha para os símbolos à esquerda da cabeça
        self.pilha_direita = Pilha()  # Pilha para os símbolos à direita da cabeça
        self.estado_atual = self.estado_inicial
        self.simbolo_atual = None
        self.palavra = None

    def ler_entradas_usuario(self):
        self.estados = input("Informe os estados (separados por vírgula): ").split(",")
        self.alfabeto = input("Informe o alfabeto (separados por vírgula): ").split(",")
        self.alfabeto.append(self.SIMBOLO_VAZIO)
        self.transicoes = {}

        print("Informe as transições no formato 'prox_estado,novo_simbolo,direcao' (ex: 'q1,1,D'):")
        for estado in self.estados:
            for simbolo in self.alfabeto:
                entrada = input(f"D({estado},{'ε' if simbolo == self.SIMBOLO_VAZIO else simbolo}): ").strip()
                if entrada:
                    prox_estado, novo_simbolo, direcao = entrada.split(',')
                    self.transicoes[(estado, simbolo)] = (prox_estado, novo_simbolo, direcao)
                else:
                    self.transicoes[(estado, simbolo)] = None

        self.estado_inicial = input("Informe o estado inicial: ").strip()
        self.estados_de_aceitacao = input("Informe o(s) estado(s) de aceitação (separados por vírgula): ").split(",")
        self.palavra = list(input("Informe a palavra a ser verificada: ")) # Solicita  a palavra para ser verifiacada na maquina de turing

    def mover_direita(self, simbolo_atual):
        self.pilha_esquerda.push(simbolo_atual)
        return self.pilha_direita.pop() if not self.pilha_direita.eh_vazio() else self.SIMBOLO_VAZIO

    def mover_esquerda(self, simbolo_atual):
        self.pilha_direita.push(simbolo_atual)
        return self.pilha_esquerda.pop() if not self.pilha_esquerda.eh_vazio() else self.SIMBOLO_VAZIO
    
    def __str__(self):
        return f"Esquerda: {self.pilha_esquerda}, Direita: {self.pilha_direita}, Estado Atual: {self.estado_atual}"


"""
Após o preenchimento, self.transicoes poderá ficar assim:
{
    ('q0', '1'): ('q0', '1', 'D'),
    ('q0', '0'): ('q1', '1', 'E'),
    ('q1', '1'): ('q_accept', '1', '|'),  # Onde 'N' pode representar "não mover"
    # ... demais transições
}

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
"""