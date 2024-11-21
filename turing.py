# implementação da máquina de turing
# entrada: estados_finais,estados_iniciais,estados etc...
# entrega: 21/11/2024
# Nome: Felipe Echeverria Vilhalva RGM: 45611

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
    SIMBOLO_VAZIO = '#'

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
                entrada = input(f"D({estado},{simbolo}): ").strip()
                if entrada:  # Apenas adiciona a transição se houver entrada
                    try:
                        prox_estado, novo_simbolo, direcao = entrada.split(',')
                        self.transicoes[(estado, simbolo)] = (prox_estado, novo_simbolo, direcao)
                    except ValueError:
                        print(f"Erro: Transição inválida para D({estado},{simbolo}). Ignorada.")
                else:
                    # Transições vazias não são registradas
                    continue

        self.estado_inicial = input("Informe o estado inicial: ").strip()
        self.estados_de_aceitacao = input("Informe o(s) estado(s) de aceitação (separados por vírgula): ").split(",")
        self.palavra = list(input("Informe a palavra a ser verificada: ")) # Solicita  a palavra para ser verifiacada na maquina de turing
        self.coloca_palavra_pilha()

    def mover_direita(self, simbolo_atual):
        self.pilha_esquerda.push(simbolo_atual)
        return self.pilha_direita.pop() if not self.pilha_direita.eh_vazio() else self.SIMBOLO_VAZIO

    def mover_esquerda(self, simbolo_atual):
        self.pilha_direita.push(simbolo_atual)
        return self.pilha_esquerda.pop() if not self.pilha_esquerda.eh_vazio() else self.SIMBOLO_VAZIO
    
    def coloca_palavra_pilha(self):
        for letra in self.palavra:
            self.pilha_direita.push(letra)

    def imprimir_transicoes(self):
        print("\nTransições da Máquina de Turing:")
        for (estado, simbolo), (prox_estado, novo_simbolo, direcao) in self.transicoes.items():
            print(f"D({estado}, {simbolo}) -> ({prox_estado}, {novo_simbolo}, {direcao})")
        
    def ler_fita(self):
        # Obter o símbolo
        simbolo_atual = self.pilha_direita.pop() if not self.pilha_direita.eh_vazio() else self.SIMBOLO_VAZIO
        print(f"Estado atual: {self.estado_atual}, Símbolo: {simbolo_atual}")

        # Verificar se é estado de aceitação
        if self.estado_atual in self.estados_de_aceitacao:
            print("Palavra aceita!")
            return
        
        # Buscar a transicao
        chave_transicao = (self.estado_atual, simbolo_atual)
        if chave_transicao not in self.transicoes or not self.transicoes[chave_transicao]:
            print("Palavra rejeitada!")
            return
        
        prox_estado, novo_simbolo, direcao = self.transicoes[chave_transicao]
        self.estado_atual = prox_estado

        # Escrever o novo simbolo na fita
        if direcao == 'D':
            self.pilha_esquerda.push(novo_simbolo)
            simbolo_atual = self.mover_direita(simbolo_atual)
        elif direcao == 'E':
            self.pilha_esquerda.push(novo_simbolo)
            simbolo_atual = self.mover_esquerda(simbolo_atual)
        else:    # Não mover (N ou outro simbolo)
            self.pilha_direita.push(novo_simbolo)
        
        print(self)
    
    def __str__(self):
        return f"Esquerda: {self.pilha_esquerda}, Direita: {self.pilha_direita}, Estado Atual: {self.estado_atual}"


turing = TuringMachine()

turing.ler_entradas_usuario()

turing.imprimir_transicoes()

# implementar o x nas transicoes

#turing.ler_fita()