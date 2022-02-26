

# class persona:
#     def __init__(self, nombre, edad, apellido):
#         self.nombre = nombre
#         self.edad = edad
#         self.apellido = apellido
    
# class Pablo(persona):
#     def __init__(nombre, edad, apellido):
#         super().__init__(nombre, edad, apellido)
#         print (f"hola mi nombre es {nombre} tengo {edad} y me apellido {apellido}")

# class Estefa(persona):
    
#     def __init__(self):
#        super().__init__()
    
#     def mensaje(self, nombre="estefa", edad=17, apellido="enrrique"): 
#         return print (f"hola mi nombre es {nombre} tengo {edad} y me apellido {apellido}")

# if __name__ == "__main__":
#     print(Pablo(nombre="pablo", edad="22", apellido="toro"))


class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)


if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())

    


    