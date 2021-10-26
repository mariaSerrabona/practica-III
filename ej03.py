#programa que calcula la nota a partir de las calificaciones

#PSEUDOCÓDIGO
'''este programa pide por parámetro el número de respuestas correctas, incorrectas y en blanco de un examen.
Para ello, empleamos al función input() que hace que se puedan pedir parámetros por consola.
Una vez tenemos pedidos todos los números, tendremos que transformarlos en varibales del tipo int, puesto que,
de serie, al pasar un parámetro por consola, se tomará como una cadena de texto, en lugar de como un número.
Una vez hecho esto, asiganamos a cada tipo de resspuesta su poderación correspondiente, obteniendo al final una calificación
que finalmente se imprimirá por pantalla con la ayuda de la fujnción print'''


num_correctas=input("Introduzca el número de respuestas correctas: ")
num_correctas=int(num_correctas)

num_incorrectas=input("Introduzca el número de respuestas incorrectas: ")
num_incorrectas=int(num_incorrectas)

num_blanco=input("Introduzca el número de respuestas en blanco: ")
num_blanco=int(num_blanco)

nota=(num_correctas*3)+(num_incorrectas*-1)+(num_blanco*0)

nota=str(nota)

print("la calificación final es de: "+ nota+" puntos")

