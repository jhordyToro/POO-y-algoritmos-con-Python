
class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)
        self._giro = timon(izquierda="40°", derecha="40°")

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en_movimiento'


    def izquierda(self, tipo='40°'):
        if tipo == "40°":
            self._giro.izquierda('40°')
        else:
            self._giro.derecha('40°')


class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass

class timon:

    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def izquierda(self, grados):
        pass
    def derech(self, grados):
        pass
