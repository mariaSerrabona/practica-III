#calcular la distancia que recorre ujn objeto con una velocidad y un timepo determinado


#PSEUDOCÓDIGO

# para relaizar le código del enunciado, lo primero que necesitamos es establecer las variables(velocidad, timepo y distancia)
# y establecer la relacion que las une, en este caso al ser un movimiento rectilíneor uniforme, la ecuación sera:
# distancia=tiempo*velocidad
# para luego poder concatenar el prodecto conuna cadena de texto para imprimirla,
# la transformaremos a un string y mostraremos mediante una función print el resultado

#en metros por segundo
velocidad=2

#en segundos
tiempo=4

distancia=tiempo*velocidad

distancia=str(distancia)

print("la distancia recorrida es: "+ distancia +" metros")