class cachorro:
    especie = "canis lupus familliaris"
    def __init__(self, nome, raca, idade): #método construtor 
        self.especie = "canis lupus familliaris"
        self.nome = nome 
        self.raca = raca
        self.idade = idade 

        # método str 
        def _str__(self):
            return "olá"
            return f"espécie: {self.especie}\nnome: {self.nome}\nraça: {self.idade}"
