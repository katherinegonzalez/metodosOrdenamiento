# ----------------------------------------------------------------------------------------
# MODULO: Métodos de Ordenamiento
# ----------------------------------------------------------------------------------------
# Descripción: En este módulo se encuentran las funciones de los métodos de ordenamiento:
# Burbuja, Seleccion e Inserción, adicionalmente se encuentran otras funciones auxiliares
# para realziar valdiaciones y generar la lista aleatoria.
# ----------------------------------------------------------------------------------------
# Autor: Katherine Xiomar González Santacruz
# Version: 1.0
# [25.09.2022]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
from random import randint
# ----------------------------------------------------------------------------------------
# FUNCIÓN: validarInput
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar el valor ingresado por el usuario
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) mensaje, (function) condicion
#       variable auxiliar: (bool) seguirPreguntando
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si seguir preguntando es false, el ciclo se rompe y se retorna el valor ingresado
#           por el usuario.
#           Si la condición no se cumple imprime un mensaje en pantalla
#       Valor de retorno: (str) opcionIngresada
# ----------------------------------------------------------------------------------------
def validarInput (mensaje, condicion):
    seguirPreguntando = True
    while seguirPreguntando:
        opcionIngresada = input(mensaje)
        if (condicion(opcionIngresada)):
            seguirPreguntando = False
        else:
            print('El valor ingresado no es válido')
    return opcionIngresada

# ----------------------------------------------------------------------------------------
# FUNCIÓN: esNumero
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar si el valor recibido es un número
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) número
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si es numero retorna True, de lo contrario retorna False
#       Valor de retorno: bool (True o False)
# ----------------------------------------------------------------------------------------
def esNumero(numero):
    return numero.isdigit() and int(numero) > 0 and int(numero) <= 20

# ----------------------------------------------------------------------------------------
# FUNCIÓN: longitudIngresada
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para capturar la longitud de la lista ingresada por el usuario y
# convertirla en entero
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) mensaje (mensaje a mostrar en el input)
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       Valor de retorno: int (numero)
# ----------------------------------------------------------------------------------------
def longitudIngresada(mensaje):
    numero = validarInput(mensaje, esNumero)
    return int(numero)

# ----------------------------------------------------------------------------------------
# FUNCIÓN: validarNumeroRandom
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para generar y validar cada uno de los números de una lista
# aleatoria y que no se repita dentro de la lista
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (lista) lista
#       variable auxiliar: (bool) seguirgenerandoNum
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si seguirgenerandoNum es false, el ciclo se rompe y se retorna el número random
#           generado
#           Si la condición no se cumple vuelve a generar y a validar otro número aleatorio
#       Valor de retorno: (str) numero
# ----------------------------------------------------------------------------------------
def validarNumeroRandom (lista):
    seguirgenerandoNum = True
    while seguirgenerandoNum:
        numero = randint(0, 19)
        if numero not in lista:
            seguirgenerandoNum = False
    return numero

# ----------------------------------------------------------------------------------------
# FUNCIÓN: listaAleatoria
# ----------------------------------------------------------------------------------------
# Descripción: función para generar una lista con N números aleatorios del 0 al 9 que no se repitan
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       (list) listaRandom
#       (int) longitud
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           se retorna una lista con N números aleatorios
#       Valor de retorno: (lista) listaRandom
# ----------------------------------------------------------------------------------------
def listaAleatoria(longitud):
    listaRandom = []
    for i in range(longitud):
        num = validarNumeroRandom(listaRandom)
        listaRandom.append(num)
    return listaRandom

# ----------------------------------------------------------------------------------------
# FUNCIÓN: burbuja
# ----------------------------------------------------------------------------------------
# Descripción: función que ordena una lista aleatoria con el método Burbuja
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (int) longitusLista
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Se imprime la lista ordenada
# ----------------------------------------------------------------------------------------
def burbuja(longitudLista):
    print('Método Burbuja: \n')
    lista = listaAleatoria(longitudLista)
    print('Lista Desordenada: ', lista)
    sigueDesordenado = True
    while sigueDesordenado:
        sigueDesordenado = False
        for i in range(longitudLista - 1):
            if (lista [i] > lista [i + 1]):
                elementoAnterior = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = elementoAnterior
                sigueDesordenado = True

    print('Lista Ordenada: ', lista)

# ----------------------------------------------------------------------------------------
# FUNCIÓN: seleccion
# ----------------------------------------------------------------------------------------
# Descripción: función que ordena una lista aleatoria con el método Selección
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (int) longitusLista
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Se imprime la lista ordenada
# ----------------------------------------------------------------------------------------
def seleccion (longitudLista):
    print('Método Selección: \n')
    lista = listaAleatoria(longitudLista)
    print('Lista Desordenada: ', lista)
    for i in range (longitudLista):
        posicionValorMinimo = i
        for j in range(i+1, longitudLista):
            if (lista[posicionValorMinimo] > lista[j]):
                posicionValorMinimo = j
        elementoAnterior = lista[i]
        lista[i] = lista[posicionValorMinimo]
        lista[posicionValorMinimo] = elementoAnterior
    print('Lista Ordenada: ', lista)


# ----------------------------------------------------------------------------------------
# FUNCIÓN: insercion
# ----------------------------------------------------------------------------------------
# Descripción: función que ordena una lista aleatoria con el método Inserción
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (int) longitusLista
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Se imprime la lista ordenada
# ----------------------------------------------------------------------------------------
def insercion (longitudLista):
    print('Método Inserción: \n')
    lista = listaAleatoria(longitudLista)
    print('Lista Desordenada: ', lista)
    for i in range(1, longitudLista):
        elementoActual = lista[i]
        indice = i

        while ( indice > 0 and lista[indice - 1] > elementoActual):
            lista[indice] = lista [indice - 1]
            indice = indice - 1
        lista[indice] = elementoActual
    print('Lista Ordenada: ', lista)

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------