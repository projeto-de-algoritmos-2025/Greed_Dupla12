class Aula:
    def __init__(self, nome, inicio, fim):
        self.nome = nome
        self.inicio = inicio
        self.fim = fim

    def __repr__(self):
        return f"{self.nome} ({self.inicio}-{self.fim})"
