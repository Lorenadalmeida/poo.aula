# # 1 EXERCICIO 
# Crie uma classe chamada Pessoa que tenha os atributos nome e idade. 
# Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.
class Pessoa:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade
P1 = Pessoa("Ryann", 15)
P2 = Pessoa("Lorena", 17)
print(P1.nome, P1.idade)
print(P2.nome, P2.idade)

# 2 EXERCICIO
# Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:
# "Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.
class Pessoa:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

p3 = Pessoa("lorena", 17)
p3.apresentar()

#  3 EXERCICIO 
# Crie uma classe Carro com os atributos marca, modelo e ano. 
# Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações.
class Carro:
    def _init_(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

c1 = Carro("Fiat", "Uno", 2010)
c2 = Carro("Volkswagen", "Gol", 2015)
c3 = Carro("Chevrolet", "Onix", 2022)

print(c1.marca, c1.modelo, c1.ano)
print(c2.marca, c2.modelo, c2.ano)
print(c3.marca, c3.modelo, c3.ano)


# 4 - Usando a classe Carro, crie um objeto e depois 
# altere o valor de um de seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração.
class Carro:
 print("Antes:", c1.ano)
c1.ano = 2021
print("Depois:", c1.ano)


# 5 - Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método depositar(valor) 
# que aumenta o saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente). 
# Teste com depósitos e saques.

class ContaBancaria:
    def _init_(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

conta = ContaBancaria("Lorena", 100)
conta.depositar(50)
print("Saldo após depósito:", conta.saldo)
conta.sacar(30)
print("Saldo após saque:", conta.saldo)


# 6 - Modifique a classe ContaBancaria para que o método sacar retorne True 
# se a operação for bem-sucedida e False caso contrário.
#  Teste o retorno e imprima mensagens adequadas.

class ContaBancaria:
    def _init_(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

conta2 = ContaBancaria("Ryann", 100)
print(conta2.sacar(50))   # True
print(conta2.sacar(100))  # False
print("Saldo:", conta2.saldo)


# 7 - Crie uma classe Aluno com atributos nome e nota. Depois crie uma classe Turma que tenha uma 
# lista de alunos e um método adicionar_aluno(aluno). Crie alguns objetos Aluno e adicione-os à turma.
class Aluno:
    def _init_(self, nome, nota):
        self.nome = nome
        self.nota = nota

class Turma:
    def _init_(self):
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

a1 = Aluno("Ryann", 8.5)
a2 = Aluno("Sophya", 9.0)
turma = Turma()
turma.adicionar_aluno(a1)
turma.adicionar_aluno(a2)


# 8 - Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, 
# apareça algo como: "Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.

class Aluno:
    def _init_(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def _str_(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"

a3 = Aluno("Pedro", 7.5)
print(a3)
print(a2)


# 9 - Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e 
# atributos de instância nome e idade. Mostre a diferença entre acessar especie pelo objeto e pela classe.

class Cachorro:
    especie = "Canis familiaris"  # atributo de classe
    
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade

dog1 = Cachorro("Rex", 5)
dog2 = Cachorro("Bidu", 2)

print(dog1.nome, dog1.idade, dog1.especie)  
print(Cachorro.especie)                      

