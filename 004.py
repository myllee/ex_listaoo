class pessoa() :
    def __init__(self, nome,idade,peso,altura) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self, anos) :
        self.idade += anos
        if self.idade < 21 :
            self.crescer(0.5 * anos)
    def engordar(self, quilos = 1):
        self.peso += quilos
    def emagrecer (self, quilos) :
        self.peso

        
    
