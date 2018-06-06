import random

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setName(self, name):
        self.name = name
    
    def setAge(self, age):
        self.age = age
    
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class PessoaFisica(Person):
    def __init__(self, CPF, name, age):
        super().__init__(name, age)
        self.cpf = CPF

    def getCPF():
        return self.cpf

    def setCPF(self, CPF):
        self.cpf = CPF

readname = input("Name:")
readage = input("Age:")
CPF = random.randrange(0, 999999999, 1)
pessoafisica = PessoaFisica(CPF, readname, readage)

print(pessoafisica.name)        
print(pessoafisica.age)        
print(pessoafisica.cpf)        