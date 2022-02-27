#algoritmo del morral el cual trata de ver el mejor resultado para meter en la mochila

def morral(tamano_morral, pesos, valores, n, contador):
    contador += 1
    print(contador)
    if n == 0 or tamano_morral == 0:
        return 0

    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1, contador)

    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1, contador),
                morral(tamano_morral, pesos, valores, n - 1, contador))


if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = int(input("de que tamaño quieres que sea el morral? ")) 
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n, contador=1)
    print(resultado)