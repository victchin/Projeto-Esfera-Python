# CÓDIGO QUE SERVE PARA DESCOBRIR A ÁREA DE UMA ESFERA
import math

class Esfera:
    def __init__(self, cor, raio):
        # Atributos
        self.cor = cor
        self.raio = raio

    def volume(self):
        # Equação para identificar o volume da esfera
        vol = (4/3)*math.pi*(self.raio**3)
        return vol
    def area(self):
        # Equação para identificar a área da esfera
        ar = 4*math.pi*(self.raio**2)
        return ar

# Instânciação e Atribuição de valores
boll1 = Esfera("Vermelha", 4)
boll2 = Esfera("Azul", 7)

# Saida
print(f"O volume da bola 1 é: {boll1.volume()} cm³")
print(f"A área superficial da bola 1 é: {boll1.area()} cm² \n")

print(f"O volume da bola 2 é: {boll2.volume()} cm³")
print(f"A área superficial da bola 2 é: {boll2.area()} cm²")
