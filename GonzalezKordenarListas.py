# ----------------------------------------------------------------------------------------
# PROGRAMA: Métodos de ordenamiento
# ----------------------------------------------------------------------------------------
# Descripción: Este programa presenta un menú con 3 tipos de ordenamiento: Burbuja,
# Seleccion e Inserción. El programa se encarga de generar una lista aleatoria y ordenarla
# con el método de ordenamiento que el usuario seleccione. EL usuario debe ingresar
# úncamente la longitud de la lista.

# ----------------------------------------------------------------------------------------
# Autor: Katherine Xiomar González Santacruz
# Version: 1.0
# [25.09.2022]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
from GonzalezKmetodosOrdenamiento import *

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# Variables de entrada: (str) opcionIngresada
# pre-condiciones: opcionIngresada debe ser '1', '2', '3', ó '0'
#                  opcionIngresada != '0'

# Variables auxiliares: (str) opcion
#                       opcion != '0'
#
# Explicación: opción es una variable auxiliar que guarda la opción ingresada por el usuario,
#              y se encarga de detener el ciclo cuando la opción seleccionada es '0'.
#              Si opcion es '0', el programa dejará de ejecutarse.
#              Si opcionIngresada es '1', se ejecuta la función burbuja() del módulo importado
#              Si opcionIngresada es '2', se ejecuta la función seleccion() del módulo importado
#              Si opcionIngresada es '3', se ejecuta la función insercion() del módulo importado
#              Si opcionIngresada es '0', se detiene el programa.
#
# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------
# Salida: Mensaje (str) mostrando la lista aleatoria generada en desorden y la lista ordenada
# con el método de ordenamiento que seleccionó el usuario.

# Si opcionIngresada es un valor diferente de '0', '1', '2', ó 3 mostrar un mensaje
# en pantalla, y solicitar el valor nuevamente.
# Si opcion == '0' , fin del programa.

# ----------------------------------------------------------------------------------------

opcion = ''
longitudLista = 10

def condicionInput (opcionIngresada):
    return opcionIngresada == '1' or opcionIngresada == '2' or \
           opcionIngresada == '3' or opcionIngresada == '0'


while (opcion != '0'):
    print('\n')
    print('Programa Ordenar Elementos de una Lista generada aleatoriamente.')
    print('Seleccione método de ordenamiento: ')
    print('1. Burbuja')
    print('2. Selección')
    print('3. Inserción')
    print('0. Salir')
    opcion = validarInput('Ingrese opción: ', condicionInput)
    if ( opcion != '0' ):
        longitudLista = longitudIngresada('Ahora ingrese la longitud de la lista que desea ordenar (de 1 a 20): ')

    print('\n')
    if (opcion == '1'):
        burbuja(longitudLista)
    elif (opcion == '2'):
        seleccion(longitudLista)
    elif (opcion == '3'):
        insercion(longitudLista)

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------
