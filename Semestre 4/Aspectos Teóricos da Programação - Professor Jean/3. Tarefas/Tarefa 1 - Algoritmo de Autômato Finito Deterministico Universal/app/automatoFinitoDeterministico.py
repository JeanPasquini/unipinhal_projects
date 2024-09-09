class AFD:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

    def processar_entrada(self, entrada):
        estado_atual = self.estado_inicial
        for simbolo in entrada:
            if simbolo in self.transicoes[estado_atual]:
                if self.transicoes[estado_atual][simbolo] == '-':
                    return False
                else:
                    estado_atual = self.transicoes[estado_atual][simbolo]
            else:
                return False
        return estado_atual in self.estados_finais