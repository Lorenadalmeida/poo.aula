# Programação Orientada a Objetos (POO) é um paradigma que organiza o código 
#em torno de objetos, que combinam dados
#Em python tudo é objeto 
# Conceitos Fundamentais da POO

# Classe: Um molde ou blueprint para criar objetos.
class celular:

# Objeto: Uma instância de uma classe.
  def __init__(self, preço, marca):

# Atributos: Dados associados a um objeto.
    self.preço = preço 
    self.marca = marca

# Métodos: Funções que definem o comportamento de um objeto.
  def apresentar(self):
     return f"Esse é o celular {self.marca} e custa {self.preço} reais"
# Encapsulamento: Controle de acesso aos atributos e métodos.
celular1 = celular
print(celular1.marca)
# herança: Reutilização de código ao criar novas classes baseadas em outras.

# Polimorfismo: Capacidade de usar métodos de forma intercambiável entre
# classes relacionadas.


# Definindo uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo
        self.idade = idade  # Atributo

    def apresentar(self):  # Método
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# Criando um objeto (instância da classe)
pessoa1 = Pessoa("Ana", 25)

# Acessando atributos e métodos
print(pessoa1.nome)  # Saída: Ana
print(pessoa1.apresentar())  # Saída: Olá, meu nome é Ana e tenho 25 anos.
