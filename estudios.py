#NOMENCLATURA UNIVERSAL
#camelCase == 'fechaDeNacimiento' 'VARIABLES'
#snake_case = fecha_de_nacimiento 'EN BASES DE DATOS'
#SCREAMING_SNAKE_CASE == FECHA_DE_NACIMIENTO 'CONSTANTES'
#kebab-case = fecha-de-nacimiento
#l33t = P445WORD para contraseñas
# Notacion Hungara = strNombre

#CONCATENACION DE TEXTOS
#nombre = 'lucas'
#edad = 30
#presentacion = 'hola mundo, soy ' + nombre + ' y tengo ' + str(edad) + ' años'
#print(presentacion)

#CONCATENACIÓN CON TERMINO BOOLEANO
#edad = 20
#if edad >= 18:
#    print('es mayor de edad')
#else:
#    print('es menor de edad')

#nombre = input('¿Cómo te llamas?')
 #   print('Hola' + nombre)
#edad = int(input('¿Cuántos años tienes?'))
#if edad >= 18:
 #   print('es mayor de edad')
#else:
 #   print('es menor de edad')

#?')
#esHijoDelDueño = respuestaHijoDelDueño == 'si'
#puedePasar = masDe12 or esHijoDelDueño

#if puedePasar:
#    print('usted puede pasar a la montaña rusa')
#else:
#    print('no puede pasar')


#CALCULAR SI UN NUMERO ES PAR O IMPAR (RESTO)
#numero = int(input('ingrese un número'))

#if numero % 2 == 0:
#    print('el numero es par')
#else:
#    print('el numero es impar')

#QUE ES UNA FUNCIÓN. funcion es una abreviación del codigo en pequeños paquetes que realizan una accion

#validamos la tarjeta de credito
#nos conectamos con un servicio externo para realizar la transacción.
#actualizamos el pedido.

#podemos crear una funcion simple con menos lineas de codigo.

# Calculadora de IMC
# IMC = Peso / (Altura x Altura)
# < 19: delgadez
# entre 20 y 25: normal
# entre 26 y 30: sobrepeso
# > de 30: obesidad


#def calcularIMC(peso, alturaEnMetros):
#    imc = peso / (alturaEnMetros * alturaEnMetros)
#    return imc

#def pedirElIMC():
#    peso = int(input('ingrese su peso en kg'))

#    alturaEnCm = int(input('ingrese su altura en cm'))
#    alturaEnMetros = alturaEnCm / 100
#    imc = calcularIMC(peso, alturaEnMetros)

#    print('su IMC es de ' + str(imc))

#    if imc < 20:
#    print('estado de delgadez')
#    if imc >= 20 and imc < 26:
#    print('peso normal')
#    if imc >= 26 and imc < 30:
#    print('sobre peso')
#    if imc >= 30:
#    print('obesidad')

#BUCLES: WHILE
# DIAGRAMA DE FLUJO WHILE==MIENTRAS
#           INCIAR
#              |EJECUTA CONDICION( SÍ SE CUMPLE O NO SE CUMPLE (VERDADERO O FALSO
#    |-----<CONDICION<-----|
#  NO(SE CUMPLE)|          |
#   TERMINA     SI         |
#               CODIGO>----|

#contador = 0
#while contador < 5:
#    contador += 1
#    if contador == 3:
#        continue
#    print("el valor de contador es: " + str(contador))

#seguirChateando = True
#while seguirChateando:
#    texto = input('>')
#    if texto == 'salir':
#        seguirChateando = False
#    texto = texto.replace(':)', '☺')
#    texto = texto.replace(':(', '☹️')
#    texto = texto.replace(':*', '😚')
#    texto = texto.replace(':p', '😛')
#    print(texto)


#QUE SON LOS ARRAYS ? ARRAYS = ARREGLOS
#EN UN LENGUAJE DE PROGRA TENEMOS DIFERENTES TIPOS DE DATOS.
#BOLEANOS: TRUE/FALSE
#NUMERO: 1024 INTEGER
#TEXTOS: "Hola Mundo"
#CUANDO CREAMOS ESTOS DATOS LO ESTAMOS GUARDANDO EN UNA VARIABLE.
#ARRAYS ES UNA VARIABLE QUE NOS PERMITE GUARDAR MUCHOS DATOS EN LE MISMO LUGAR
#DIVIDA EN VARIOS CASILLERO CON CADA CASILLERO UN DATOS DISTINTOS.
# 0,1,2... EL 0 CUENTA 0=a 1=b STACK OVERFLOW ES BUSCAR UN DATO EN UN CASILLERO INEXISTENTE
#H|O|L|A| |M|U|N|D|O|
#0|1|2|3|4|5|6|7|8|9|

#arreglo = ['banada', 'melon', 'sandía', 'pera']

#arreglo.remove('sandía')
#arreglo.append('kiwi')
#for fruta in arreglo:
#    print("la fruta es:" + fruta)

#arreglo.reverse() lanza el print al reves.
#arreglo.remove("melon") remueve el texto indicado en comillas
#arreglo.append() permite agregar una nueva fruta.

#para hacer un recorrido en las letras de la variable texto.
#texto = "hola mundo"
#for letra in texto:
#    print("letra:" + letra)

#Funcion range me permite inspeccionar un rango de letras o numeros.
#for numero in range(10):
#   print(numero)

#diccionario = {
#    "programar": "programar es transformar el cafe en código",
#    "POO" : "Programación Orientada a Objetos",
#    "MVC" : "Modelo Vista Controlador"
#}

numero = {
    "4" : "cuatro",
    "5" : "cinco",
    "6" : "seis",
    "7" : "siete",
    "8" : "ocho"
}
texto = input('íngrese un numero:')

textoFinal = ''
for letra in texto:
    textoFinal += numero[letra]

print(textoFinal)

#MIN 1.53.38  ENCRIPTAR Y DESENCRIPTAR DATOS SENSIBLES.


