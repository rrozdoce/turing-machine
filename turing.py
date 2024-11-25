# implementação da máquina de turing
# entrada: estados_finais,estados_iniciais,estados etc...
# entrega: 21/11/2024
# Nome: Felipe Echeverria Vilhalva RGM: 45611

class TuringMachine:
    SIMBOLO_CERQUILHA = '#'

    def __init__(self, estados=None, alfabeto=None, transicoes=None, estado_inicial=None, estados_de_aceitacao=None):
        self.estados = estados
        self.alfabeto = alfabeto if alfabeto is not None else []
        self.transicoes = transicoes if transicoes is not None else {}
        self.estado_inicial = estado_inicial
        self.estados_de_aceitacao = estados_de_aceitacao
        self.pilha = []  # Pilha para os símbolos da cabeça
        self.indice_atual_pilha = 0
        self.tamanho_pilha = 0
        self.estado_atual = self.estado_inicial
        self.simbolo_atual = None
        self.palavra = None
    
    def getPalavra(self):
        return self.palavra

    def ler_entradas_usuario(self):
        self.estados = input("Informe os estados (separados por vírgula): ").split(",")
        self.alfabeto = input("Informe o alfabeto (separados por vírgula): ").split(",")
        self.alfabeto.append(self.SIMBOLO_CERQUILHA)  # Adiciona o símbolo da cerquilha ao alfabeto
        self.alfabeto.append('x') # adiciona o x no alfabeto(para verificar transicoes com ele)
        self.alfabeto.append('L|') # adiciona o simbolo L|(fim ou inicio da fita) no alfabeto(para verificar transicoes com ele)
        self.transicoes = {}

        print("Informe as transições no formato 'prox_estado,novo_simbolo,direcao' (ex: 'q1,1,D'). Use '_' para manter o mesmo símbolo:")
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
        self.palavra = list(input("Informe a palavra a ser verificada: "))  # Solicita a palavra para verificação
        self.coloca_palavra_pilha()
    
    def coloca_palavra_pilha(self):
        for letra in self.palavra:
            self.pilha.append(letra)
        self.pilha.append('L|')

    # para imprimir as transicoes(debugg)
    def imprimir_transicoes(self): 
        print("\nTransições da Máquina de Turing:")
        for transicao in self.transicoes.items():
            print(transicao)
    
    # para imprimir o alfabeto(debugg)
    def imprimir_alfabeto(self):
        print("\nAlfabeto da Máquina de Turing:")
        print(", ".join(self.alfabeto))
    
    def ler_fita(self) -> bool:
        # Lê o primeiro símbolo antes do loop
        self.simbolo_atual = self.pilha[0]
        self.estado_atual = self.estado_inicial
        
        while True:
            # Verifica se o estado atual é de aceitação
            if self.estado_atual in self.estados_de_aceitacao:
                # Máquina aceitou a entrada!
                return True

            # Verifica se há transição válida
            if (self.estado_atual, self.simbolo_atual) not in self.transicoes:
                # Máquina rejeitou a entrada! Não há transição válida.
                return False

            # Executa a transição
            prox_estado, novo_simbolo, direcao = self.transicoes[(self.estado_atual, self.simbolo_atual)]
            print(f"Transição: ({self.estado_atual}, {self.simbolo_atual}) => {prox_estado}, {novo_simbolo}, {direcao}")
            print(f"{self}")
            print()
            
            self.estado_atual = prox_estado
            if novo_simbolo != '_':
               self.simbolo_atual = novo_simbolo

            if direcao == 'D':
                if self.indice_atual_pilha + 1 < len(self.pilha):
                   self.pilha[self.indice_atual_pilha] = self.simbolo_atual
                   self.indice_atual_pilha = self.indice_atual_pilha + 1 # vai para direita do array
                   self.simbolo_atual = self.pilha[self.indice_atual_pilha] # proximo simbolo da palavra
            elif direcao == 'E':
                if self.indice_atual_pilha - 1 >= 0:
                    self.pilha[self.indice_atual_pilha] = self.simbolo_atual
                    self.indice_atual_pilha = self.indice_atual_pilha - 1 # vai para esquerda do array
                    self.simbolo_atual = self.pilha[self.indice_atual_pilha]

    def __str__(self):
        return f"Simbolo atual: {self.simbolo_atual}, Pilha: {self.pilha}"

turing = TuringMachine()

turing.ler_entradas_usuario()

print('\nFita da maquina de turing: ')

resposta = turing.ler_fita()

if resposta:
    print(f"Palavra {''.join(turing.getPalavra())} aceita!")
else:
    print(f"Palavra {''.join(turing.getPalavra())} rejeitada!")